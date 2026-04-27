---
atomic_guid: "a524ce99-86de-4db6-b4f9-e08f35a47a15"
title: "Create local account with admin privileges"
framework: "atomic"
generated: "true"
attack_technique_id: "T1078.003"
attack_technique_name: "Valid Accounts: Local Accounts"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.003/T1078.003.yaml"
build_date: "2026-04-27 19:12:26"
executor: "command_prompt"
aliases:
  - "a524ce99-86de-4db6-b4f9-e08f35a47a15"
  - "Create local account with admin privileges"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

After execution the new account will be active and added to the Administrators group

## ATT&CK Mapping

- [[kb/attack/techniques/T1078-valid_accounts#^t1078003-local-accounts|T1078.003: Local Accounts]]

## Input Arguments

### password

- description: Password for art-test user
- type: string
- default: -4RTisCool!-321

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
net user art-test /add
net user art-test #{password}
net localgroup administrators art-test /add
```

### Cleanup

```cmd
net localgroup administrators art-test /delete >nul 2>&1
net user art-test /delete >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.003/T1078.003.yaml)
