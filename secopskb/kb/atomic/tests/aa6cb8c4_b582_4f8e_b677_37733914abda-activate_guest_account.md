---
atomic_guid: "aa6cb8c4-b582-4f8e-b677-37733914abda"
title: "Activate Guest Account"
framework: "atomic"
generated: "true"
attack_technique_id: "T1078.001"
attack_technique_name: "Valid Accounts: Default Accounts"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.001/T1078.001.yaml"
build_date: "2026-04-27 19:12:26"
executor: "command_prompt"
aliases:
  - "aa6cb8c4-b582-4f8e-b677-37733914abda"
  - "Activate Guest Account"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

The Adversaries can activate the default Guest user. The guest account is inactivated by default

## ATT&CK Mapping

- [[kb/attack/techniques/T1078-valid_accounts#^t1078001-default-accounts|T1078.001: Default Accounts]]

## Input Arguments

### guest_user

- description: Specify the guest account
- type: string
- default: guest

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
net user #{guest_user} /active:yes
```

### Cleanup

```cmd
net user #{guest_user} /active:no
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.001/T1078.001.yaml)
