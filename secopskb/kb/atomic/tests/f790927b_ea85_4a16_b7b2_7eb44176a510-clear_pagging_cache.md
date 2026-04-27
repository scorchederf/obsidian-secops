---
atomic_guid: "f790927b-ea85-4a16-b7b2-7eb44176a510"
title: "Clear Pagging Cache"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-27 19:12:28"
executor: "sh"
aliases:
  - "f790927b-ea85-4a16-b7b2-7eb44176a510"
  - "Clear Pagging Cache"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

clear pagging cache via system request. This is a temporary change in the system to clear paging cache. This technique seen in Awfulshred wiper as part
of its malicious payload on the compromised host. added reference link for this technique: https://www.tecmint.com/clear-ram-memory-cache-buffer-and-swap-space-on-linux/

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]

## Executor

- elevation_required: True
- name: sh

### Command

```bash
free && echo 3 > /proc/sys/vm/drop_caches && free
echo 3> /proc/sys/vm/drop_caches
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
