---
atomic_guid: "1f73af33-62a8-4bf1-bd10-3bea931f2c0d"
title: "Set a SetGID flag on file (freebsd)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1548.001"
attack_technique_name: "Abuse Elevation Control Mechanism: Setuid and Setgid"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.001/T1548.001.yaml"
build_date: "2026-04-27 19:12:27"
executor: "sh"
aliases:
  - "1f73af33-62a8-4bf1-bd10-3bea931f2c0d"
  - "Set a SetGID flag on file (freebsd)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test sets the SetGID flag on a file in FreeBSD.

## ATT&CK Mapping

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism#^t1548001-setuid-and-setgid|T1548.001: Setuid and Setgid]]

## Input Arguments

### file_to_setuid

- description: Path of file to set SetGID flag
- type: path
- default: /tmp/evilBinary

## Executor

- elevation_required: True
- name: sh

### Command

```bash
touch #{file_to_setuid}
chown root #{file_to_setuid}
chmod g+xs #{file_to_setuid}
```

### Cleanup

```bash
rm #{file_to_setuid}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.001/T1548.001.yaml)
