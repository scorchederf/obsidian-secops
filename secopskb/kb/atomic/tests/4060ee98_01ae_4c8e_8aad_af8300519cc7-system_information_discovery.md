---
atomic_guid: "4060ee98-01ae-4c8e-8aad-af8300519cc7"
title: "System Information Discovery"
framework: "atomic"
generated: "true"
attack_technique_id: "T1082"
attack_technique_name: "System Information Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "4060ee98-01ae-4c8e-8aad-af8300519cc7"
  - "System Information Discovery"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# System Information Discovery

The script gathernetworkinfo.vbs is employed to collect system information such as the operating system, DNS details, firewall configuration, etc. Outputs are stored in c:\Windows\System32\config or c:\Windows\System32\reg. https://www.verboon.info/2011/06/the-gathernetworkinfo-vbs-script/

## Metadata

- Atomic GUID: 4060ee98-01ae-4c8e-8aad-af8300519cc7
- Technique: T1082: System Information Discovery
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1082/T1082.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
wscript.exe C:\Windows\System32\gatherNetworkInfo.vbs
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml)
