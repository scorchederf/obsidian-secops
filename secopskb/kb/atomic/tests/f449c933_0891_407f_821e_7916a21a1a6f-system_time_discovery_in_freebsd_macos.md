---
atomic_guid: "f449c933-0891-407f-821e-7916a21a1a6f"
title: "System Time Discovery in FreeBSD/macOS"
framework: "atomic"
generated: "true"
attack_technique_id: "T1124"
attack_technique_name: "System Time Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1124/T1124.yaml"
build_date: "2026-04-27 19:12:27"
executor: "sh"
aliases:
  - "f449c933-0891-407f-821e-7916a21a1a6f"
  - "System Time Discovery in FreeBSD/macOS"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Identify system time. Upon execution, the local computer system time and timezone will be displayed.

## ATT&CK Mapping

- [[kb/attack/techniques/T1124-system_time_discovery|T1124: System Time Discovery]]

## Executor

- name: sh

### Command

```bash
date
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1124/T1124.yaml)
