---
atomic_guid: "95e19466-469e-4316-86d2-1dc401b5a959"
title: "Remote System Discovery - adidnsdump"
framework: "atomic"
generated: "true"
attack_technique_id: "T1018"
attack_technique_name: "Remote System Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1018/T1018.yaml"
build_date: "2026-04-27 19:12:25"
executor: "command_prompt"
aliases:
  - "95e19466-469e-4316-86d2-1dc401b5a959"
  - "Remote System Discovery - adidnsdump"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This tool enables enumeration and exporting of all DNS records in the zone for recon purposes of internal networks
Python 3 and adidnsdump must be installed, use the get_prereq_command's to meet the prerequisites for this test.
Successful execution of this test will list dns zones in the terminal.

## ATT&CK Mapping

- [[kb/attack/techniques/T1018-remote_system_discovery|T1018: Remote System Discovery]]

## Input Arguments

### acct_pass

- description: Account password.
- type: string
- default: password

### host_name

- description: hostname or ip address to connect to.
- type: string
- default: 192.168.1.1

### user_name

- description: username including domain.
- type: string
- default: domain\user

### venv_path

- description: Path to the folder for the tactics venv
- type: string
- default: PathToAtomicsFolder\..\ExternalPayloads\venv_t1018

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
if (Test-Path -Path "#{venv_path}" ) { exit 0 } else { exit 1 }
```

### Get Prerequisite

```powershell
py -m venv "#{venv_path}"
```

adidnsdump must be installed

### Prerequisite Check

```powershell
if (Get-Command "#{venv_path}\Scripts\adidnsdump" -errorAction SilentlyContinue) { exit 0 } else { exit 1 }
```

### Get Prerequisite

```powershell
& "#{venv_path}\Scripts\pip.exe" install --no-cache-dir adidnsdump 2>&1 | Out-Null
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
"#{venv_path}\Scripts\adidnsdump" -u #{user_name} -p #{acct_pass} --print-zones #{host_name}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1018/T1018.yaml)
