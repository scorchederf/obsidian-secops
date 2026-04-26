---
atomic_guid: "a39ee1bc-b8c1-4331-8e5f-1859eb408518"
title: "Create a user account on a FreeBSD system"
framework: "atomic"
generated: "true"
attack_technique_id: "T1136.001"
attack_technique_name: "Create Account: Local Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1136.001/T1136.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "a39ee1bc-b8c1-4331-8e5f-1859eb408518"
  - "Create a user account on a FreeBSD system"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Create a user account on a FreeBSD system

Create a user via pw

## Metadata

- Atomic GUID: a39ee1bc-b8c1-4331-8e5f-1859eb408518
- Technique: T1136.001: Create Account: Local Account
- Platforms: linux
- Executor: sh
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
- name: sh

### Command

```sh
pw useradd #{username} -s /usr/sbin/nologin -d /nonexistent -c evil_account
```

### Cleanup

```sh
rmuser -y #{username}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1136.001/T1136.001.yaml)
