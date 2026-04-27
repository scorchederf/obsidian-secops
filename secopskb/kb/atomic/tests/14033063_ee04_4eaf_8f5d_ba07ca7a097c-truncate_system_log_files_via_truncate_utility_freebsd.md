---
atomic_guid: "14033063-ee04-4eaf-8f5d-ba07ca7a097c"
title: "Truncate system log files via truncate utility (freebsd)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.002"
attack_technique_name: "Indicator Removal on Host: Clear FreeBSD, Linux or Mac System Logs"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.002/T1070.002.yaml"
build_date: "2026-04-26 17:02:12"
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

# Truncate system log files via truncate utility (freebsd)

This test truncates the system log files using the truncate utility with (-s 0 or --size=0) parameter which sets file size to zero, thus emptying the file content

## Metadata

- Atomic GUID: 14033063-ee04-4eaf-8f5d-ba07ca7a097c
- Technique: T1070.002: Indicator Removal on Host: Clear FreeBSD, Linux or Mac System Logs
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1070.002/T1070.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.002]]

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
