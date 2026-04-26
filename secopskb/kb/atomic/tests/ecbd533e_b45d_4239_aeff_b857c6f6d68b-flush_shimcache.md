---
atomic_guid: "ecbd533e-b45d-4239-aeff-b857c6f6d68b"
title: "Flush Shimcache"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "ecbd533e-b45d-4239-aeff-b857c6f6d68b"
  - "Flush Shimcache"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Flush Shimcache

The ShimCache is a component in Windows operating systems that stores information about recently executed applications. It is used by the operating system to speed up the launching process of applications. The ShimCache is also used by IR teams and Forensic teams. Forensic investigators can use the ShimCache to determine which programs have been executed on a system, even if they have been deleted or their logs have been cleared.Reference : https://blueteamops.medium.com/shimcache-flush-89daff28d15e

## Metadata

- Atomic GUID: ecbd533e-b45d-4239-aeff-b857c6f6d68b
- Technique: T1112: Modify Registry
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1112/T1112.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
Rundll32.exe apphelp.dll,ShimFlushCache
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
