---
atomic_guid: "40d8eabd-e394-46f6-8785-b9bfa1d011d2"
title: "Create a user account on a Linux system"
framework: "atomic"
generated: "true"
attack_technique_id: "T1136.001"
attack_technique_name: "Create Account: Local Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1136.001/T1136.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "bash"
aliases:
  - "40d8eabd-e394-46f6-8785-b9bfa1d011d2"
  - "Create a user account on a Linux system"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Create a user account on a Linux system

Create a user via useradd

## Metadata

- Atomic GUID: 40d8eabd-e394-46f6-8785-b9bfa1d011d2
- Technique: T1136.001: Create Account: Local Account
- Platforms: linux
- Executor: bash
- Elevation Required: True
- Source Path: atomics/T1136.001/T1136.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1136-create_account|T1136.001]]

## Input Arguments

### username

- description: Username of the user to create
- type: string
- default: evil_user

## Executor

- elevation_required: True
- name: bash

### Command

```bash
useradd -M -N -r -s /bin/bash -c evil_account #{username}
```

### Cleanup

```bash
userdel #{username}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1136.001/T1136.001.yaml)
