---
atomic_guid: "161dcd85-d014-4f5e-900c-d3eaae82a0f7"
title: "Enumerate logged on users via CMD (Domain)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1087.002"
attack_technique_name: "Account Discovery: Domain Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.002/T1087.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "161dcd85-d014-4f5e-900c-d3eaae82a0f7"
  - "Enumerate logged on users via CMD (Domain)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Enumerate logged on users via CMD (Domain)

Enumerate logged on users. Upon exeuction, logged on users will be displayed.

## Metadata

- Atomic GUID: 161dcd85-d014-4f5e-900c-d3eaae82a0f7
- Technique: T1087.002: Account Discovery: Domain Account
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1087.002/T1087.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1087-account_discovery|T1087.002]]

## Input Arguments

### computer_name

- description: Name of remote system to query
- type: string
- default: %COMPUTERNAME%

## Executor

- name: command_prompt

### Command

```cmd
query user /SERVER:#{computer_name}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.002/T1087.002.yaml)
