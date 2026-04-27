---
atomic_guid: "848e43b3-4c0a-4e4c-b4c9-d1e8cea9651c"
title: "Real-time system log clearance/deletion"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.002"
attack_technique_name: "Indicator Removal on Host: Clear FreeBSD, Linux or Mac System Logs"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.002/T1070.002.yaml"
build_date: "2026-04-27 19:12:26"
executor: "sh"
aliases:
  - "848e43b3-4c0a-4e4c-b4c9-d1e8cea9651c"
  - "Real-time system log clearance/deletion"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test reads real-time system log file and writes empty string to it, thus clearing the log file without tampering with the logging process

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal#^t1070002-clear-linux-or-mac-system-logs|T1070.002: Clear Linux or Mac System Logs]]

## Executor

- elevation_required: True
- name: sh

### Command

```bash
sudo log -f /var/log/system.log | : > /var/log/system.log
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.002/T1070.002.yaml)
