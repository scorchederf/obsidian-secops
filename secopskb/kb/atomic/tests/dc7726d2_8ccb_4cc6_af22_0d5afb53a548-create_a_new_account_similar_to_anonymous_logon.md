---
atomic_guid: "dc7726d2-8ccb-4cc6-af22-0d5afb53a548"
title: "Create a new account similar to ANONYMOUS LOGON"
framework: "atomic"
generated: "true"
attack_technique_id: "T1136.002"
attack_technique_name: "Create Account: Domain Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1136.002/T1136.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "dc7726d2-8ccb-4cc6-af22-0d5afb53a548"
  - "Create a new account similar to ANONYMOUS LOGON"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Create a new account similar to ANONYMOUS LOGON

Create a new account similar to ANONYMOUS LOGON in a command prompt.

## Metadata

- Atomic GUID: dc7726d2-8ccb-4cc6-af22-0d5afb53a548
- Technique: T1136.002: Create Account: Domain Account
- Platforms: windows
- Executor: command_prompt
- Elevation Required: False
- Source Path: atomics/T1136.002/T1136.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1136-create_account|T1136.002]]

## Input Arguments

### password

- description: Password of the user to create
- type: string
- default: T1136_pass123!

### username

- description: Username of the user to create
- type: string
- default: ANONYMOUS  LOGON

## Executor

- elevation_required: False
- name: command_prompt

### Command

```cmd
net user "#{username}" "#{password}" /add /domain
```

### Cleanup

```cmd
net user "#{username}" >nul 2>&1 /del /domain
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1136.002/T1136.002.yaml)
