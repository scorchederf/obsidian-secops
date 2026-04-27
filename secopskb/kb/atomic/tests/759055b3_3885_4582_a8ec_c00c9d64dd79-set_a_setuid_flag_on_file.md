---
atomic_guid: "759055b3-3885-4582-a8ec-c00c9d64dd79"
title: "Set a SetUID flag on file"
framework: "atomic"
generated: "true"
attack_technique_id: "T1548.001"
attack_technique_name: "Abuse Elevation Control Mechanism: Setuid and Setgid"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.001/T1548.001.yaml"
build_date: "2026-04-27 19:12:27"
executor: "sh"
aliases:
  - "759055b3-3885-4582-a8ec-c00c9d64dd79"
  - "Set a SetUID flag on file"
platforms:
  - "macos"
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test sets the SetUID flag on a file in FreeBSD.

## ATT&CK Mapping

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism#^t1548001-setuid-and-setgid|T1548.001: Setuid and Setgid]]

## Input Arguments

### file_to_setuid

- description: Path of file to set SetUID flag
- type: path
- default: /tmp/evilBinary

## Executor

- elevation_required: True
- name: sh

### Command

```bash
sudo touch #{file_to_setuid}
sudo chown root #{file_to_setuid}
sudo chmod u+xs #{file_to_setuid}
```

### Cleanup

```bash
sudo rm #{file_to_setuid}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.001/T1548.001.yaml)
