---
atomic_guid: "486e88ea-4f56-470f-9b57-3f4d73f39133"
title: "Hostname Discovery"
framework: "atomic"
generated: "true"
attack_technique_id: "T1082"
attack_technique_name: "System Information Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml"
build_date: "2026-04-27 19:12:26"
executor: "sh"
aliases:
  - "486e88ea-4f56-470f-9b57-3f4d73f39133"
  - "Hostname Discovery"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Identify system hostname for FreeBSD, Linux and macOS systems.

## ATT&CK Mapping

- [[kb/attack/techniques/T1082-system_information_discovery|T1082: System Information Discovery]]

## Executor

- name: sh

### Command

```bash
hostname
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml)
