---
atomic_guid: "d91473ca-944e-477a-b484-0e80217cd789"
title: "Discover System Language with chcp"
framework: "atomic"
generated: "true"
attack_technique_id: "T1614.001"
attack_technique_name: "System Location Discovery: System Language Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1614.001/T1614.001.yaml"
build_date: "2026-04-27 19:12:28"
executor: "command_prompt"
aliases:
  - "d91473ca-944e-477a-b484-0e80217cd789"
  - "Discover System Language with chcp"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Identify System language with the chcp command.

Upon successful execution, result in number format can be looked up to correlate the language.

## ATT&CK Mapping

- [[kb/attack/techniques/T1614-system_location_discovery#^t1614001-system-language-discovery|T1614.001: System Language Discovery]]

## Executor

- name: command_prompt

### Command

```cmd
chcp
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1614.001/T1614.001.yaml)
