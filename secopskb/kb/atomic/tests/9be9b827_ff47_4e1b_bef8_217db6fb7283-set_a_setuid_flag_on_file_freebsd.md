---
atomic_guid: "9be9b827-ff47-4e1b-bef8-217db6fb7283"
title: "Set a SetUID flag on file (freebsd)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1548.001"
attack_technique_name: "Abuse Elevation Control Mechanism: Setuid and Setgid"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.001/T1548.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "9be9b827-ff47-4e1b-bef8-217db6fb7283"
  - "Set a SetUID flag on file (freebsd)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Set a SetUID flag on file (freebsd)

This test sets the SetUID flag on a file in FreeBSD.

## Metadata

- Atomic GUID: 9be9b827-ff47-4e1b-bef8-217db6fb7283
- Technique: T1548.001: Abuse Elevation Control Mechanism: Setuid and Setgid
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1548.001/T1548.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.001]]

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
touch #{file_to_setuid}
chown root #{file_to_setuid}
chmod u+xs #{file_to_setuid}
```

### Cleanup

```bash
rm #{file_to_setuid}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.001/T1548.001.yaml)
