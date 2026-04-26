---
atomic_guid: "21fe622f-8e53-4b31-ba83-6d333c2583f4"
title: "Testing usage of uncommonly used port with PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1571"
attack_technique_name: "Non-Standard Port"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1571/T1571.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "21fe622f-8e53-4b31-ba83-6d333c2583f4"
  - "Testing usage of uncommonly used port with PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Testing usage of uncommonly used port with PowerShell

Testing uncommonly used port utilizing PowerShell. APT33 has been known to attempt telnet over port 8081. Upon execution, details about the successful
port check will be displayed.

## Metadata

- Atomic GUID: 21fe622f-8e53-4b31-ba83-6d333c2583f4
- Technique: T1571: Non-Standard Port
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1571/T1571.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1571-non-standard_port|T1571]]

## Input Arguments

### domain

- description: Specify target hostname
- type: string
- default: google.com

### port

- description: Specify uncommon port number
- type: string
- default: 8081

## Executor

- name: powershell

### Command

```powershell
Test-NetConnection -ComputerName #{domain} -port #{port}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1571/T1571.yaml)
