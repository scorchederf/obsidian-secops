---
atomic_guid: "14033063-ee04-4eaf-8f5d-ba07ca7a097c"
title: "Truncate system log files via truncate utility (freebsd)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.002"
attack_technique_name: "Indicator Removal on Host: Clear FreeBSD, Linux or Mac System Logs"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.002/T1070.002.yaml"
build_date: "2026-04-27 19:12:26"
executor: "sh"
aliases:
  - "14033063-ee04-4eaf-8f5d-ba07ca7a097c"
  - "Truncate system log files via truncate utility (freebsd)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test truncates the system log files using the truncate utility with (-s 0 or --size=0) parameter which sets file size to zero, thus emptying the file content

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal#^t1070002-clear-linux-or-mac-system-logs|T1070.002: Clear Linux or Mac System Logs]]

## Executor

- elevation_required: True
- name: sh

### Command

```bash
truncate -s 0 /var/log/messages #size parameter shorthand
truncate --size=0 /var/log/security #size parameter
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.002/T1070.002.yaml)
