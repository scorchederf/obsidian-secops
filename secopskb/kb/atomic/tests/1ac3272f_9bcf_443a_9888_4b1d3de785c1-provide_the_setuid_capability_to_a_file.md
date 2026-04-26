---
atomic_guid: "1ac3272f-9bcf-443a-9888-4b1d3de785c1"
title: "Provide the SetUID capability to a file"
framework: "atomic"
generated: "true"
attack_technique_id: "T1548.001"
attack_technique_name: "Abuse Elevation Control Mechanism: Setuid and Setgid"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.001/T1548.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "1ac3272f-9bcf-443a-9888-4b1d3de785c1"
  - "Provide the SetUID capability to a file"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Provide the SetUID capability to a file

This test gives a file the capability to set UID without using flags.

## Metadata

- Atomic GUID: 1ac3272f-9bcf-443a-9888-4b1d3de785c1
- Technique: T1548.001: Abuse Elevation Control Mechanism: Setuid and Setgid
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1548.001/T1548.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.001]]

## Input Arguments

### file_to_setcap

- description: Path of file to provide the SetUID capability
- type: path
- default: /tmp/evilBinary

## Executor

- elevation_required: True
- name: sh

### Command

```sh
touch #{file_to_setcap}
sudo setcap cap_setuid=ep #{file_to_setcap}
```

### Cleanup

```sh
rm #{file_to_setcap}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.001/T1548.001.yaml)
