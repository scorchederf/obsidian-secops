---
atomic_guid: "b51239b4-0129-474f-a2b4-70f855b9f2c2"
title: "Process Discovery - get-wmiObject"
framework: "atomic"
generated: "true"
attack_technique_id: "T1057"
attack_technique_name: "Process Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1057/T1057.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "b51239b4-0129-474f-a2b4-70f855b9f2c2"
  - "Process Discovery - get-wmiObject"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Process Discovery - get-wmiObject

Utilize get-wmiObject PowerShell cmdlet to identify processes.

Upon successful execution, powershell.exe will execute get-wmiObject to list processes. Output will be via stdout.

## Metadata

- Atomic GUID: b51239b4-0129-474f-a2b4-70f855b9f2c2
- Technique: T1057: Process Discovery
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1057/T1057.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1057-process_discovery|T1057]]

## Executor

- name: powershell

### Command

```powershell
get-wmiObject -class Win32_Process
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1057/T1057.yaml)
