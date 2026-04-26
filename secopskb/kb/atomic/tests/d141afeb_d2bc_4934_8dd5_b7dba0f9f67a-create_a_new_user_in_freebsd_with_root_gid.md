---
atomic_guid: "d141afeb-d2bc-4934-8dd5-b7dba0f9f67a"
title: "Create a new user in FreeBSD with `root` GID."
framework: "atomic"
generated: "true"
attack_technique_id: "T1136.001"
attack_technique_name: "Create Account: Local Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1136.001/T1136.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "d141afeb-d2bc-4934-8dd5-b7dba0f9f67a"
  - "Create a new user in FreeBSD with `root` GID."
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Create a new user in FreeBSD with `root` GID.

Creates a new user in FreeBSD and adds the user to the `root` group. This technique was used by adversaries during the Butter attack campaign.

## Metadata

- Atomic GUID: d141afeb-d2bc-4934-8dd5-b7dba0f9f67a
- Technique: T1136.001: Create Account: Local Account
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1136.001/T1136.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1136-create_account|T1136.001]]

## Input Arguments

### password

- description: Password of the user to create
- type: string
- default: BetterWithButter

### username

- description: Username of the user to create
- type: string
- default: butter

## Executor

- elevation_required: True
- name: sh

### Command

```bash
pw useradd #{username} -g 0 -d /root -s /bin/sh
echo "#{password}" | pw usermod #{username} -h 0
```

### Cleanup

```bash
pw userdel #{username}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1136.001/T1136.001.yaml)
