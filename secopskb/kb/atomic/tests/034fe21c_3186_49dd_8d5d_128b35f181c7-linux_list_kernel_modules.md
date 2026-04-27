---
atomic_guid: "034fe21c-3186-49dd-8d5d-128b35f181c7"
title: "Linux List Kernel Modules"
framework: "atomic"
generated: "true"
attack_technique_id: "T1082"
attack_technique_name: "System Information Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml"
build_date: "2026-04-27 19:12:26"
executor: "sh"
aliases:
  - "034fe21c-3186-49dd-8d5d-128b35f181c7"
  - "Linux List Kernel Modules"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Enumerate kernel modules installed 3 different ways. Upon successful execution stdout will display kernel modules installed on host 2 times, followed by list of modules matching 'vmw' if present.

## ATT&CK Mapping

- [[kb/attack/techniques/T1082-system_information_discovery|T1082: System Information Discovery]]

## Executor

- name: sh

### Command

```bash
lsmod
kmod list
grep vmw /proc/modules
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml)
