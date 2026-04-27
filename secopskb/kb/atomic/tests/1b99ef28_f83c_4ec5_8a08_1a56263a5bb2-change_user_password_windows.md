---
atomic_guid: "1b99ef28-f83c-4ec5-8a08-1a56263a5bb2"
title: "Change User Password - Windows"
framework: "atomic"
generated: "true"
attack_technique_id: "T1531"
attack_technique_name: "Account Access Removal"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1531/T1531.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "1b99ef28-f83c-4ec5-8a08-1a56263a5bb2"
  - "Change User Password - Windows"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Changes the user password to hinder access attempts. Seen in use by LockerGoga. Upon execution, log into the user account "AtomicAdministrator" with
the password "HuHuHUHoHo283283".

## ATT&CK Mapping

- [[kb/attack/techniques/T1531-account_access_removal|T1531: Account Access Removal]]

## Input Arguments

### new_password

- description: New password for the specified account.
- type: string
- default: HuHuHUHoHo283283@dJD

### new_user_password

- description: Password to use if user account must be created first
- type: string
- default: User2ChangePW!

### user_account

- description: User account whose password will be changed.
- type: string
- default: AtomicAdministrator

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
net user #{user_account} #{new_user_password} /add
net.exe user #{user_account} #{new_password}
```

### Cleanup

```cmd
net.exe user #{user_account} /delete >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1531/T1531.yaml)
