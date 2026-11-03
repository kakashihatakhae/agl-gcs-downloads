import importlib.util,json,sys,zipfile
from pathlib import Path
spec=importlib.util.spec_from_file_location('publisher',Path(__file__).with_name('publish.py'));module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
output=Path(sys.argv[1]);output.mkdir(parents=True,exist_ok=True)
version,hashes=module.prepare(output)
info=json.loads((output/'BUILD-INFO.json').read_text())
with zipfile.ZipFile(output/info['package_file']) as archive: archive.extractall(output)
(output/'version.txt').write_text(version)
print('WINDOWS_INSTALLER_TEST_INPUTS_VERIFIED '+version)
