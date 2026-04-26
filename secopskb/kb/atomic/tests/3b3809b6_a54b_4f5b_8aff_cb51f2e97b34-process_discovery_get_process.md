---
atomic_guid: "3b3809b6-a54b-4f5b-8aff-cb51f2e97b34"
title: "Process Discovery - Get-Process"
framework: "atomic"
generated: "true"
attack_technique_id: "T1057"
attack_technique_name: "Process Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1057/T1057.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "3b3809b6-a54b-4f5b-8aff-cb51f2e97b34"
  - "Process Discovery - Get-Process"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Process Discovery - Get-Process

Utilize Get-Process PowerShell cmdlet to identify processes.

Upon successful execution, powershell.exe will execute Get-Process to list processes. Output will be via stdout.

## Metadata

- Atomic GUID: 3b3809b6-a54b-4f5b-8aff-cb51f2e97b34
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
Get-Process
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1057/T1057.yaml)
