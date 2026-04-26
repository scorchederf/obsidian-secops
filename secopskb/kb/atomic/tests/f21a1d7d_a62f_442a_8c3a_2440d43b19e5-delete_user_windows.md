---
atomic_guid: "f21a1d7d-a62f-442a-8c3a-2440d43b19e5"
title: "Delete User - Windows"
framework: "atomic"
generated: "true"
attack_technique_id: "T1531"
attack_technique_name: "Account Access Removal"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1531/T1531.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "f21a1d7d-a62f-442a-8c3a-2440d43b19e5"
  - "Delete User - Windows"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Delete User - Windows

Deletes a user account to prevent access. Upon execution, run the command "net user" to verify that the new "AtomicUser" account was deleted.

## Metadata

- Atomic GUID: f21a1d7d-a62f-442a-8c3a-2440d43b19e5
- Technique: T1531: Account Access Removal
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1531/T1531.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1531-account_access_removal|T1531]]

## Input Arguments

### new_user_password

- description: Password to use if user account must be created first
- type: string
- default: User2DeletePW!

### user_account

- description: User account to be deleted.
- type: string
- default: AtomicUser

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
net user #{user_account} #{new_user_password} /add
net.exe user #{user_account} /delete
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1531/T1531.yaml)
