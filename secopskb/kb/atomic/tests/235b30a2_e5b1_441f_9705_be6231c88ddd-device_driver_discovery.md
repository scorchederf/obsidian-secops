---
atomic_guid: "235b30a2-e5b1-441f-9705-be6231c88ddd"
title: "Device Driver Discovery"
framework: "atomic"
generated: "true"
attack_technique_id: "T1652"
attack_technique_name: "Device Driver Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1652/T1652.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "235b30a2-e5b1-441f-9705-be6231c88ddd"
  - "Device Driver Discovery"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Device Driver Discovery

Displays a list of installed device drivers on the local computer and their properties. Threat actors use this command to enumerate the existing drivers on the computer. 
Parameters: 
/v /fo list - Displays verbose output in a list format - the /v parameter is not valid for signed drivers
/si /fo list - Provides information about signed drivers and outputs it in a list format

## Metadata

- Atomic GUID: 235b30a2-e5b1-441f-9705-be6231c88ddd
- Technique: T1652: Device Driver Discovery
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1652/T1652.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1652-device_driver_discovery|T1652]]

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
driverquery /v /fo list
driverquery /si /fo list
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1652/T1652.yaml)
