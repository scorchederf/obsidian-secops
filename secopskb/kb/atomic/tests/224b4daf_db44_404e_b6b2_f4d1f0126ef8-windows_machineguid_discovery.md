---
atomic_guid: "224b4daf-db44-404e-b6b2-f4d1f0126ef8"
title: "Windows MachineGUID Discovery"
framework: "atomic"
generated: "true"
attack_technique_id: "T1082"
attack_technique_name: "System Information Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml"
build_date: "2026-04-27 19:12:26"
executor: "command_prompt"
aliases:
  - "224b4daf-db44-404e-b6b2-f4d1f0126ef8"
  - "Windows MachineGUID Discovery"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Identify the Windows MachineGUID value for a system. Upon execution, the machine GUID will be displayed from registry.

## ATT&CK Mapping

- [[kb/attack/techniques/T1082-system_information_discovery|T1082: System Information Discovery]]

## Executor

- name: command_prompt

### Command

```cmd
REG QUERY HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography /v MachineGuid
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml)
