---
atomic_guid: "7f566051-f033-49fb-89de-b6bacab730f0"
title: "Security Software Discovery - powershell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1518.001"
attack_technique_name: "Software Discovery: Security Software Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1518.001/T1518.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "7f566051-f033-49fb-89de-b6bacab730f0"
  - "Security Software Discovery - powershell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Security Software Discovery - powershell

Methods to identify Security Software on an endpoint

when sucessfully executed, powershell is going to processes related AV products if they are running.
Note that, depending on the privilege of current user, get-process | ?{$_.Description -like "*"} may not return the processes related to AV products of the check.
For instance, only with Administrator right, you can see the process description of McAffee processes. Hence, it is better to use get-process | ?{$_.ProcessName -like "*"},
if you know the name of those processes.

## Metadata

- Atomic GUID: 7f566051-f033-49fb-89de-b6bacab730f0
- Technique: T1518.001: Software Discovery: Security Software Discovery
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1518.001/T1518.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1518-software_discovery|T1518.001]]

## Executor

- name: powershell

### Command

```powershell
get-process | ?{$_.Description -like "*virus*"}
get-process | ?{$_.Description -like "*carbonblack*"}
get-process | ?{$_.Description -like "*defender*"}
get-process | ?{$_.Description -like "*cylance*"}
get-process | ?{$_.Description -like "*mc*"}
get-process | ?{$_.ProcessName -like "*mc*"}
get-process | Where-Object { $_.ProcessName -eq "Sysmon" }
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1518.001/T1518.001.yaml)
