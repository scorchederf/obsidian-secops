---
atomic_guid: "4947897f-643a-4b75-b3f5-bed6885749f6"
title: "FreeBSD List Kernel Modules"
framework: "atomic"
generated: "true"
attack_technique_id: "T1082"
attack_technique_name: "System Information Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "4947897f-643a-4b75-b3f5-bed6885749f6"
  - "FreeBSD List Kernel Modules"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# FreeBSD List Kernel Modules

Enumerate kernel modules loaded. Upon successful execution stdout will display kernel modules loaded, followed by list of modules matching 'vmm' if present.

## Metadata

- Atomic GUID: 4947897f-643a-4b75-b3f5-bed6885749f6
- Technique: T1082: System Information Discovery
- Platforms: linux
- Executor: sh
- Source Path: atomics/T1082/T1082.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]

## Executor

- name: sh

### Command

```bash
kldstat
kldstat | grep vmm
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml)
