---
atomic_guid: "fcec2963-9951-4173-9bfa-98d8b7834e62"
title: "Create a new Windows domain admin user"
framework: "atomic"
generated: "true"
attack_technique_id: "T1136.002"
attack_technique_name: "Create Account: Domain Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1136.002/T1136.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "fcec2963-9951-4173-9bfa-98d8b7834e62"
  - "Create a new Windows domain admin user"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Create a new Windows domain admin user

Creates a new domain admin user in a command prompt.

## Metadata

- Atomic GUID: fcec2963-9951-4173-9bfa-98d8b7834e62
- Technique: T1136.002: Create Account: Domain Account
- Platforms: windows
- Executor: command_prompt
- Elevation Required: False
- Source Path: atomics/T1136.002/T1136.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1136-create_account|T1136.002]]

## Input Arguments

### group

- description: Domain administrator group to which add the user to
- type: string
- default: Domain Admins

### password

- description: Password of the user to create
- type: string
- default: T1136_pass123!

### username

- description: Username of the user to create
- type: string
- default: T1136.002_Admin

## Executor

- elevation_required: False
- name: command_prompt

### Command

```cmd
net user "#{username}" "#{password}" /add /domain
net group "#{group}" "#{username}" /add /domain
```

### Cleanup

```cmd
net user "#{username}" >nul 2>&1 /del /domain
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1136.002/T1136.002.yaml)
