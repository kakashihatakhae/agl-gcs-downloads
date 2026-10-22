#!/usr/bin/env python3
"""Publish verified compiled packages using this downloads repo's GITHUB_TOKEN."""
import argparse
import hashlib
import json
import re
from pathlib import Path
import shutil
import subprocess
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
REPO = 'kakashihatakhae/agl-gcs-downloads'

def checked_path(relative):
    path = (ROOT / relative).resolve()
    if not path.is_relative_to(ROOT) or '\\' in relative:
        raise ValueError('Unsafe release path')
    return path

def sha(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()

def gh(*args):
    return subprocess.check_output(['gh', *args], text=True).strip()

def assemble(info, output):
    target = output / info['file']
    if target.name != info['file'] or not info['parts']:
        raise ValueError('Invalid asset name or empty parts')
    with target.open('wb') as destination:
        for part in info['parts']:
            source = checked_path(part['path'])
            if source.stat().st_size != part['size'] or sha(source) != part['sha256']:
                raise ValueError('Part integrity mismatch: ' + part['path'])
            with source.open('rb') as stream:
                shutil.copyfileobj(stream, destination)
    if target.stat().st_size != info['size'] or sha(target) != info['sha256']:
        raise ValueError('Assembled asset integrity mismatch: ' + target.name)
    return target

def prepare(output):
    pointer = json.loads((ROOT / 'release-publisher/current.json').read_text())
    request_path = checked_path(pointer['request'])
    request = json.loads(request_path.read_text())
    version = request['version']
    if not re.fullmatch(r'\d+\.\d+\.\d+-internal\.\d+', version):
        raise ValueError('Expected an internal semantic version')
    prefix = 'AGL-Planner-' + version + '-Windows-x64'
    installer_path = checked_path(request['installer_info'])
    if not installer_path.is_file():
        subprocess.run(['git', 'sparse-checkout', 'add', '/' + str(installer_path.parent.relative_to(ROOT)) + '/'], cwd=ROOT, check=True)
    installer = json.loads(installer_path.read_text())
    if installer['file'] != prefix + '-Setup.exe' or request['archive']['file'] != prefix + '.zip':
        raise ValueError('Package filenames differ from the declared version')
    assemble(installer, output)
    archive = assemble(request['archive'], output)
    with zipfile.ZipFile(archive) as bundle:
        if bundle.testzip() is not None:
            raise ValueError('Portable ZIP CRC mismatch')
        manifest = json.loads(bundle.read('AGL-Planner-Windows-x64/agl-update.json'))
        if manifest['version'] != version or manifest['build'] != installer['build']:
            raise ValueError('ZIP and installer use different builds')
        for item in manifest['files']:
            raw = bundle.read('AGL-Planner-Windows-x64/' + item['path'])
            if len(raw) != item['size'] or hashlib.sha256(raw).hexdigest() != item['sha256']:
                raise ValueError('ZIP inventory mismatch: ' + item['path'])
    for name in ['BUILD-INFO.json', 'README-WINDOWS-my.md', 'RELEASE_NOTES.md', 'SHA256SUMS.txt']:
        shutil.copyfile(request_path.parent / 'assets' / name, output / name)
    metadata = json.loads((output / 'BUILD-INFO.json').read_text())
    if (metadata['source_revision'] != manifest['source_revision'] or metadata['version'] != version or
            metadata['installer_sha256'] != installer['sha256'] or metadata['package_sha256'] != request['archive']['sha256']):
        raise ValueError('Build provenance mismatch')
    expected = {path.name for path in output.iterdir()} - {'SHA256SUMS.txt'}
    hashes = {}
    for line in (output / 'SHA256SUMS.txt').read_text().splitlines():
        digest, name = line.split('  ', 1)
        if name not in expected or name in hashes or sha(output / name) != digest:
            raise ValueError('Release checksum mismatch: ' + name)
        hashes[name] = digest
    if set(hashes) != expected:
        raise ValueError('Incomplete checksum list')
    hashes['SHA256SUMS.txt'] = sha(output / 'SHA256SUMS.txt')
    print('All 6 assets and all application inventory hashes verified', flush=True)
    return version, hashes

def publish(output, version, hashes):
    tag = 'v' + version
    title = 'AGL Planner ' + tag + ' — Windows x64'
    notes = (output / 'RELEASE_NOTES.md').read_text().strip()
    result = subprocess.run(['gh', 'release', 'view', tag, '--repo', REPO, '--json', 'name,body,isDraft,url'], capture_output=True, text=True)
    if result.returncode:
        if not ('404' in result.stderr or 'release not found' in result.stderr.lower()):
            raise RuntimeError(result.stderr)
        subprocess.run(['gh', 'release', 'create', tag, '--repo', REPO, '--draft', '--prerelease', '--latest=false', '--title', title,
                        '--target', subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(), '--notes-file', str(output / 'RELEASE_NOTES.md')], check=True)
        release = json.loads(gh('release', 'view', tag, '--repo', REPO, '--json', 'name,body,isDraft,url'))
    else:
        release = json.loads(result.stdout)
    if release['name'] != title or release['body'].replace('\r\n', '\n').strip() != notes:
        raise ValueError('Existing release differs; refusing to replace it')
    remote = json.loads(gh('release', 'view', tag, '--repo', REPO, '--json', 'assets'))['assets']
    existing = {asset['name'] for asset in remote}
    if existing - set(hashes):
        raise ValueError('Unexpected existing assets')
    missing = sorted(set(hashes) - existing)
    if missing:
        if not release['isDraft']:
            raise ValueError('Published release is incomplete; never replace it')
        subprocess.run(['gh', 'release', 'upload', tag, '--repo', REPO] + [str(output / name) for name in missing], check=True)
    with tempfile.TemporaryDirectory(prefix='agl-remote-release-') as temporary:
        subprocess.run(['gh', 'release', 'download', tag, '--repo', REPO, '--dir', temporary], check=True)
        downloaded = {path.name for path in Path(temporary).iterdir()}
        if downloaded != set(hashes) or any(sha(Path(temporary) / name) != value for name, value in hashes.items()):
            raise ValueError('Uploaded asset SHA256 verification failed; keep draft')
    if release['isDraft']:
        subprocess.run(['gh', 'release', 'edit', tag, '--repo', REPO, '--draft=false', '--prerelease', '--latest=false'], check=True)
    print(gh('release', 'view', tag, '--repo', REPO, '--json', 'url', '--jq', '.url'))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify-only', action='store_true')
    args = parser.parse_args()
    with tempfile.TemporaryDirectory(prefix='agl-release-assets-') as temporary:
        output = Path(temporary)
        version, hashes = prepare(output)
        if not args.verify_only:
            publish(output, version, hashes)
