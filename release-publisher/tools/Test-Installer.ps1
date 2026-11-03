param(
    [Parameter(Mandatory = $true)][string]$Installer,
    [Parameter(Mandatory = $true)][string]$Payload,
    [Parameter(Mandatory = $true)][string]$Version
)
$ErrorActionPreference = 'Stop'
$installDir = Join-Path $env:LOCALAPPDATA 'Programs\AGL Planner'
$registry = 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Uninstall\AGLPlanner'
if ((Test-Path $installDir) -or (Test-Path $registry)) {
    throw 'Use a clean Windows test account; an AGL Planner installation already exists.'
}
$process = Start-Process -FilePath (Resolve-Path $Installer).Path -ArgumentList '/S' -PassThru -Wait
if ($process.ExitCode -ne 0) { throw "Installer failed: $($process.ExitCode)" }
$manifest = Get-Content (Join-Path $Payload 'agl-update.json') -Raw | ConvertFrom-Json
foreach ($file in $manifest.files) {
    $installed = Join-Path $installDir $file.path
    if (-not (Test-Path $installed)) { throw "Missing installed file: $($file.path)" }
    if ((Get-FileHash $installed -Algorithm SHA256).Hash.ToLowerInvariant() -ne $file.sha256) {
        throw "Installed file hash mismatch: $($file.path)"
    }
}
$entry = Get-ItemProperty $registry
if ($entry.DisplayVersion -ne $Version -or $entry.InstallLocation -ne $installDir) {
    throw 'Installed Apps registration has the wrong version or location.'
}
$startMenu = Join-Path ([Environment]::GetFolderPath('Programs')) 'AGL Planner\AGL Planner.lnk'
$shell = New-Object -ComObject WScript.Shell
if (-not (Test-Path $startMenu) -or $shell.CreateShortcut($startMenu).TargetPath -ne (Join-Path $installDir 'AGL Planner.exe')) {
    throw 'Start Menu shortcut is missing or points at the wrong executable.'
}
$preserved = Join-Path $installDir 'installer-test-user-file.txt'
Set-Content $preserved 'User data must survive uninstall.'
$uninstaller = Join-Path $installDir 'Uninstall AGL Planner.exe'
# _?= runs NSIS uninstall in place and makes -Wait cover the complete uninstall.
$process = Start-Process -FilePath $uninstaller -ArgumentList "/S _?=$installDir" -PassThru -Wait
if ($process.ExitCode -ne 0) { throw "Uninstaller failed: $($process.ExitCode)" }
if ((Test-Path (Join-Path $installDir 'AGL Planner.exe')) -or (Test-Path $registry) -or (Test-Path $startMenu)) {
    throw 'Uninstall left the application, its registration or shortcut behind.'
}
if (-not (Test-Path $preserved)) { throw 'Uninstall deleted a user-created file.' }
Remove-Item $preserved
# In-place uninstall can leave its own executable until the process has exited.
Remove-Item $uninstaller -ErrorAction SilentlyContinue
Remove-Item $installDir
Write-Output 'WINDOWS_INSTALLER_FILES_HASHES_SHORTCUT_REGISTRATION_UNINSTALL_AND_USER_DATA_PASS'
