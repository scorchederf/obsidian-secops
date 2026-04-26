---
atomic_guid: "01993ba5-1da3-4e15-a719-b690d4f0f0b2"
title: "Create a user account on a MacOS system"
framework: "atomic"
generated: "true"
attack_technique_id: "T1136.001"
attack_technique_name: "Create Account: Local Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1136.001/T1136.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "bash"
aliases:
  - "01993ba5-1da3-4e15-a719-b690d4f0f0b2"
  - "Create a user account on a MacOS system"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Create a user account on a MacOS system

Creates a user on a MacOS system with dscl

## Metadata

- Atomic GUID: 01993ba5-1da3-4e15-a719-b690d4f0f0b2
- Technique: T1136.001: Create Account: Local Account
- Platforms: macos
- Executor: bash
- Elevation Required: True
- Source Path: atomics/T1136.001/T1136.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1136-create_account|T1136.001]]

## Input Arguments

### realname

- description: 'realname' to record when creating the user
- type: string
- default: Evil Account

### username

- description: Username of the user to create
- type: string
- default: evil_user

## Executor

- elevation_required: True
- name: bash

### Command

```bash
dscl . -create /Users/#{username}
dscl . -create /Users/#{username} UserShell /bin/zsh
dscl . -create /Users/#{username} RealName "#{realname}"
dscl . -create /Users/#{username} UniqueID "1010"
dscl . -create /Users/#{username} PrimaryGroupID 80
dscl . -create /Users/#{username} NFSHomeDirectory /Users/#{username}
```

### Cleanup

```bash
dscl . -delete /Users/#{username}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1136.001/T1136.001.yaml)
