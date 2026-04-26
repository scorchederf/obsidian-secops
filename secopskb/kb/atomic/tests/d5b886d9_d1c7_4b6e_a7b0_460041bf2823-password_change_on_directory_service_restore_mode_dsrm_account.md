---
atomic_guid: "d5b886d9-d1c7-4b6e-a7b0-460041bf2823"
title: "Password Change on Directory Service Restore Mode (DSRM) Account"
framework: "atomic"
generated: "true"
attack_technique_id: "T1098"
attack_technique_name: "Account Manipulation"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1098/T1098.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "d5b886d9-d1c7-4b6e-a7b0-460041bf2823"
  - "Password Change on Directory Service Restore Mode (DSRM) Account"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Password Change on Directory Service Restore Mode (DSRM) Account

Change the password on the Directory Service Restore Mode (DSRM) account using ntdsutil by syncing to existing account

## Metadata

- Atomic GUID: d5b886d9-d1c7-4b6e-a7b0-460041bf2823
- Technique: T1098: Account Manipulation
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1098/T1098.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1098-account_manipulation|T1098]]

## Input Arguments

### sync_account

- description: Account to sync password from
- type: string
- default: %username%

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
ntdsutil "set dsrm password" "sync from domain account #{sync_account}" "q" "q"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1098/T1098.yaml)
