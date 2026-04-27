---
atomic_guid: "f2f91612-d904-49d7-87c2-6c165d23bead"
title: "BIOS Information Discovery through Registry"
framework: "atomic"
generated: "true"
attack_technique_id: "T1082"
attack_technique_name: "System Information Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml"
build_date: "2026-04-27 19:12:26"
executor: "command_prompt"
aliases:
  - "f2f91612-d904-49d7-87c2-6c165d23bead"
  - "BIOS Information Discovery through Registry"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Looks up for BIOS information in the registry. BIOS information is often read in order to detect sandboxing environments.  Upon execution, BIOS information will be displayed.
- https://tria.ge/210111-eaz8mqhgh6/behavioral1
- https://evasions.checkpoint.com/techniques/registry.html

## ATT&CK Mapping

- [[kb/attack/techniques/T1082-system_information_discovery|T1082: System Information Discovery]]

## Executor

- name: command_prompt

### Command

```cmd
reg query HKEY_LOCAL_MACHINE\HARDWARE\DESCRIPTION\System /v SystemBiosVersion
reg query HKEY_LOCAL_MACHINE\HARDWARE\DESCRIPTION\System /v VideoBiosVersion
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml)
