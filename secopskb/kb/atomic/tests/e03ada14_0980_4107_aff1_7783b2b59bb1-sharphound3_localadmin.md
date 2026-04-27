---
atomic_guid: "e03ada14-0980-4107-aff1-7783b2b59bb1"
title: "SharpHound3 - LocalAdmin"
framework: "atomic"
generated: "true"
attack_technique_id: "T1069.001"
attack_technique_name: "Permission Groups Discovery: Local Groups"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.001/T1069.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "e03ada14-0980-4107-aff1-7783b2b59bb1"
  - "SharpHound3 - LocalAdmin"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# SharpHound3 - LocalAdmin

This module runs the Windows executable of SharpHound in order to remotely list members of the local Administrators group (SAMR)

## Metadata

- Atomic GUID: e03ada14-0980-4107-aff1-7783b2b59bb1
- Technique: T1069.001: Permission Groups Discovery: Local Groups
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1069.001/T1069.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1069-permission_groups_discovery|T1069.001]]

## Input Arguments

### domain

- description: FQDN of the targeted domain
- type: string
- default: $env:UserDnsDomain

### output_path

- description: Output for SharpHound
- type: path
- default: $env:TEMP\SharpHound\

### sharphound_path

- description: SharpHound Windows executable
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\SharpHound.exe

## Dependencies

SharpHound binary must exist on disk and at specified location (#{sharphound_path}).
And the computer must be domain joined (implicit authentication).

### Prerequisite Check

```powershell
if (Test-Path "#{sharphound_path}") { exit 0 } else { exit 1 }
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://github.com/BloodHoundAD/BloodHound/blob/e062fe73d73c015dccb37fae5089342d009b84b8/Collectors/SharpHound.exe?raw=true" -OutFile "#{sharphound_path}"
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
New-Item -Path "#{output_path}" -ItemType Directory > $null
& "#{sharphound_path}" -d "#{domain}" --CollectionMethod LocalAdmin --NoSaveCache --OutputDirectory "#{output_path}"
```

### Cleanup

```powershell
Remove-Item -Recurse #{output_path} -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.001/T1069.001.yaml)
