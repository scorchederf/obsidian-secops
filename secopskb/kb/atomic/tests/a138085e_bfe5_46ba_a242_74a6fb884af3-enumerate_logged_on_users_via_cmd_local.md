---
atomic_guid: "a138085e-bfe5-46ba-a242-74a6fb884af3"
title: "Enumerate logged on users via CMD (Local)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1087.001"
attack_technique_name: "Account Discovery: Local Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.001/T1087.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "a138085e-bfe5-46ba-a242-74a6fb884af3"
  - "Enumerate logged on users via CMD (Local)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Enumerate logged on users via CMD (Local)

Enumerate logged on users. Upon execution, logged on users will be displayed.

## Metadata

- Atomic GUID: a138085e-bfe5-46ba-a242-74a6fb884af3
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
query user
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.001/T1087.001.yaml)
