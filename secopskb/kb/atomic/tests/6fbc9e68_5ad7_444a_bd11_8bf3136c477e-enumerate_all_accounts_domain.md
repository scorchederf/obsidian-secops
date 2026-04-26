---
atomic_guid: "6fbc9e68-5ad7-444a-bd11-8bf3136c477e"
title: "Enumerate all accounts (Domain)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1087.002"
attack_technique_name: "Account Discovery: Domain Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.002/T1087.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "6fbc9e68-5ad7-444a-bd11-8bf3136c477e"
  - "Enumerate all accounts (Domain)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Enumerate all accounts (Domain)

Enumerate all accounts
Upon exection, multiple enumeration commands will be run and their output displayed in the PowerShell session

## Metadata

- Atomic GUID: 6fbc9e68-5ad7-444a-bd11-8bf3136c477e
- Technique: T1087.002: Account Discovery: Domain Account
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1087.002/T1087.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1087-account_discovery|T1087.002]]

## Executor

- name: command_prompt

### Command

```cmd
net user /domain
net group /domain
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.002/T1087.002.yaml)
