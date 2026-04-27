---
atomic_guid: "ac333fe1-ce2b-400b-a117-538634427439"
title: "Disable ASLR Via sysctl parameters - Linux"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-27 19:12:28"
executor: "bash"
aliases:
  - "ac333fe1-ce2b-400b-a117-538634427439"
  - "Disable ASLR Via sysctl parameters - Linux"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects Execution of the `sysctl` command to set `kernel.randomize_va_space=0` which disables Address Space Layout Randomization (ASLR) in Linux.

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]

## Executor

- elevation_required: True
- name: bash

### Command

```bash
sysctl -w kernel.randomize_va_space=0
```

### Cleanup

```bash
sysctl -w kernel.randomize_va_space=2
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
