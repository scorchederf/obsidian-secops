---
atomic_guid: "896dfe97-ae43-4101-8e96-9a7996555d80"
title: "Make and modify binary from C source"
framework: "atomic"
generated: "true"
attack_technique_id: "T1548.001"
attack_technique_name: "Abuse Elevation Control Mechanism: Setuid and Setgid"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.001/T1548.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "896dfe97-ae43-4101-8e96-9a7996555d80"
  - "Make and modify binary from C source"
platforms:
  - "macos"
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Make and modify binary from C source

Make, change owner, and change file attributes on a C source code file

## Metadata

- Atomic GUID: 896dfe97-ae43-4101-8e96-9a7996555d80
- Technique: T1548.001: Abuse Elevation Control Mechanism: Setuid and Setgid
- Platforms: macos, linux
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1548.001/T1548.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.001]]

## Input Arguments

### payload

- description: hello.c payload
- type: path
- default: PathToAtomicsFolder/T1548.001/src/hello.c

## Executor

- elevation_required: True
- name: sh

### Command

```sh
cp #{payload} /tmp/hello.c
sudo chown root /tmp/hello.c
sudo make /tmp/hello
sudo chown root /tmp/hello
sudo chmod u+s /tmp/hello
/tmp/hello
```

### Cleanup

```sh
sudo rm /tmp/hello
sudo rm /tmp/hello.c
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.001/T1548.001.yaml)
