---
atomic_guid: "eefe6a49-d88b-41d8-8fc2-b46822da90d3"
title: "FreeBSD VM Check via Kernel Modules"
framework: "atomic"
generated: "true"
attack_technique_id: "T1082"
attack_technique_name: "System Information Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "eefe6a49-d88b-41d8-8fc2-b46822da90d3"
  - "FreeBSD VM Check via Kernel Modules"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# FreeBSD VM Check via Kernel Modules

Identify virtual machine host kernel modules.

## Metadata

- Atomic GUID: eefe6a49-d88b-41d8-8fc2-b46822da90d3
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
kldstat | grep -i "vmm"
kldstat | grep -i "vbox"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml)
