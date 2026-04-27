---
atomic_guid: "db55f666-7cba-46c6-9fe6-205a05c3242c"
title: "Set a SetGID flag on file"
framework: "atomic"
generated: "true"
attack_technique_id: "T1548.001"
attack_technique_name: "Abuse Elevation Control Mechanism: Setuid and Setgid"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.001/T1548.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "db55f666-7cba-46c6-9fe6-205a05c3242c"
  - "Set a SetGID flag on file"
platforms:
  - "macos"
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Set a SetGID flag on file

This test sets the SetGID flag on a file in Linux and macOS.

## Metadata

- Atomic GUID: db55f666-7cba-46c6-9fe6-205a05c3242c
- Technique: T1548.001: Abuse Elevation Control Mechanism: Setuid and Setgid
- Platforms: macos, linux
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1548.001/T1548.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.001]]

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
sudo touch #{file_to_setuid}
sudo chown root #{file_to_setuid}
sudo chmod g+xs #{file_to_setuid}
```

### Cleanup

```bash
sudo rm #{file_to_setuid}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.001/T1548.001.yaml)
