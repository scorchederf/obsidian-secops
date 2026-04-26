---
atomic_guid: "db53959c-207d-4000-9e7a-cd8eb417e072"
title: "Make and modify capabilities of a binary"
framework: "atomic"
generated: "true"
attack_technique_id: "T1548.001"
attack_technique_name: "Abuse Elevation Control Mechanism: Setuid and Setgid"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.001/T1548.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "db53959c-207d-4000-9e7a-cd8eb417e072"
  - "Make and modify capabilities of a binary"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Make and modify capabilities of a binary

Make and modify [capabilities](https://man7.org/linux/man-pages/man7/capabilities.7.html) of a C source code file.
The binary doesn't have to modify the UID, but the binary is given the capability to arbitrarily modify it at any time with `setuid(0)`.
Without being owned by root, the binary can set the UID to 0.

## Metadata

- Atomic GUID: db53959c-207d-4000-9e7a-cd8eb417e072
- Technique: T1548.001: Abuse Elevation Control Mechanism: Setuid and Setgid
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1548.001/T1548.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.001]]

## Input Arguments

### payload

- description: cap.c payload
- type: path
- default: PathToAtomicsFolder/T1548.001/src/cap.c

## Executor

- elevation_required: True
- name: sh

### Command

```sh
cp #{payload} /tmp/cap.c
make /tmp/cap
sudo setcap cap_setuid=ep /tmp/cap
/tmp/cap
```

### Cleanup

```sh
rm /tmp/cap
rm /tmp/cap.c
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.001/T1548.001.yaml)
