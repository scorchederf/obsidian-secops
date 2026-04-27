---
atomic_guid: "631d4cf1-42c9-4209-8fe9-6bd4de9421be"
title: "Discover System Language by Registry Query"
framework: "atomic"
generated: "true"
attack_technique_id: "T1614.001"
attack_technique_name: "System Location Discovery: System Language Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1614.001/T1614.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "631d4cf1-42c9-4209-8fe9-6bd4de9421be"
  - "Discover System Language by Registry Query"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Discover System Language by Registry Query

Identify System language by querying the registry on an endpoint. 

Upon successful execution, result in number format can be looked up to correlate the language.

## Metadata

- Atomic GUID: 631d4cf1-42c9-4209-8fe9-6bd4de9421be
- Technique: T1614.001: System Location Discovery: System Language Discovery
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1614.001/T1614.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1614-system_location_discovery|T1614.001]]

## Executor

- name: command_prompt

### Command

```cmd
reg query HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Nls\Language
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1614.001/T1614.001.yaml)
