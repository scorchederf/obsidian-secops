---
atomic_guid: "70e13ef4-5a74-47e4-9d16-760b41b0e2db"
title: "operating system discovery "
framework: "atomic"
generated: "true"
attack_technique_id: "T1082"
attack_technique_name: "System Information Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "70e13ef4-5a74-47e4-9d16-760b41b0e2db"
  - "operating system discovery "
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# operating system discovery 

operating system discovery using get-ciminstance
https://petri.com/getting-operating-system-information-powershell/

## Metadata

- Atomic GUID: 70e13ef4-5a74-47e4-9d16-760b41b0e2db
- Technique: T1082: System Information Discovery
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1082/T1082.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
Get-CimInstance Win32_OperatingSystem | Select-Object Caption, Version, ServicePackMajorVersion, OSArchitecture, CSName, WindowsDirectory | Out-null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml)
