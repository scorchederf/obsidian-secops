---
atomic_guid: "5c784969-1d43-4ac7-8c3d-ed6d025ed10d"
title: "Check Software Inventory Logging (SIL) status via Registry"
framework: "atomic"
generated: "true"
attack_technique_id: "T1012"
attack_technique_name: "Query Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1012/T1012.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "5c784969-1d43-4ac7-8c3d-ed6d025ed10d"
  - "Check Software Inventory Logging (SIL) status via Registry"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Check Software Inventory Logging (SIL) status via Registry

Microsoft's Software Inventory Logging (SIL) collects information about software installed per host basis. Adversary can use such logs to passively 
check for existence of software of interest to them. Status of SIL can be checked via registry.
[Reference](https://blog.talosintelligence.com/chinese-hacking-group-apt41-compromised-taiwanese-government-affiliated-research-institute-with-shadowpad-and-cobaltstrike-2/)

## Metadata

- Atomic GUID: 5c784969-1d43-4ac7-8c3d-ed6d025ed10d
- Technique: T1012: Query Registry
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1012/T1012.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1012-query_registry|T1012]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
reg.exe query hklm\software\microsoft\windows\softwareinventorylogging /v collectionstate /reg:64
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1012/T1012.yaml)
