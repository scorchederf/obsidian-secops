---
atomic_guid: "80887bec-5a9b-4efc-a81d-f83eb2eb32ab"
title: "Enumerate all accounts on Windows (Local)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1087.001"
attack_technique_name: "Account Discovery: Local Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.001/T1087.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "80887bec-5a9b-4efc-a81d-f83eb2eb32ab"
  - "Enumerate all accounts on Windows (Local)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Enumerate all accounts on Windows (Local)

Enumerate all accounts
Upon execution, multiple enumeration commands will be run and their output displayed in the PowerShell session

## Metadata

- Atomic GUID: 80887bec-5a9b-4efc-a81d-f83eb2eb32ab
- Technique: T1087.001: Account Discovery: Local Account
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1087.001/T1087.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1087-account_discovery|T1087.001]]

## Executor

- name: command_prompt

### Command

```cmd
net user
dir c:\Users\
cmdkey.exe /list
net localgroup "Users"
net localgroup
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.001/T1087.001.yaml)
