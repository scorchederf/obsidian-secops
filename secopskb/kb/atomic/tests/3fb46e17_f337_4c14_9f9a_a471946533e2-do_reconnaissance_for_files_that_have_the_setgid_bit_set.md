---
atomic_guid: "3fb46e17-f337-4c14-9f9a-a471946533e2"
title: "Do reconnaissance for files that have the setgid bit set"
framework: "atomic"
generated: "true"
attack_technique_id: "T1548.001"
attack_technique_name: "Abuse Elevation Control Mechanism: Setuid and Setgid"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.001/T1548.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "3fb46e17-f337-4c14-9f9a-a471946533e2"
  - "Do reconnaissance for files that have the setgid bit set"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Do reconnaissance for files that have the setgid bit set

This test simulates a command that can be run to enumerate files that have the setgid bit set

## Metadata

- Atomic GUID: 3fb46e17-f337-4c14-9f9a-a471946533e2
- Technique: T1548.001: Abuse Elevation Control Mechanism: Setuid and Setgid
- Platforms: linux
- Executor: sh
- Source Path: atomics/T1548.001/T1548.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.001]]

## Executor

- name: sh

### Command

```bash
find /usr/bin -perm -2000
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.001/T1548.001.yaml)
