---
atomic_guid: "3386975b-367a-4fbb-9d77-4dcf3639ffd3"
title: "Map admin share"
framework: "atomic"
generated: "true"
attack_technique_id: "T1021.002"
attack_technique_name: "Remote Services: SMB/Windows Admin Shares"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1021.002/T1021.002.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "3386975b-367a-4fbb-9d77-4dcf3639ffd3"
  - "Map admin share"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Map admin share

Connecting To Remote Shares

## Metadata

- Atomic GUID: 3386975b-367a-4fbb-9d77-4dcf3639ffd3
- Technique: T1021.002: Remote Services: SMB/Windows Admin Shares
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1021.002/T1021.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1021-remote_services|T1021.002]]

## Input Arguments

### computer_name

- description: Target Computer Name
- type: string
- default: Target

### password

- description: Password
- type: string
- default: P@ssw0rd1

### share_name

- description: Examples C$, IPC$, Admin$
- type: string
- default: C$

### user_name

- description: Username
- type: string
- default: DOMAIN\Administrator

## Executor

- name: command_prompt

### Command

```commandprompt
cmd.exe /c "net use \\#{computer_name}\#{share_name} #{password} /u:#{user_name}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1021.002/T1021.002.yaml)
