---
atomic_guid: "3c717bf3-2ecc-4d79-8ac8-0bfbf08fbce6"
title: "Change User Password via passwd"
framework: "atomic"
generated: "true"
attack_technique_id: "T1531"
attack_technique_name: "Account Access Removal"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1531/T1531.yaml"
build_date: "2026-04-27 19:12:27"
executor: "sh"
aliases:
  - "3c717bf3-2ecc-4d79-8ac8-0bfbf08fbce6"
  - "Change User Password via passwd"
platforms:
  - "macos"
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test changes the user password to hinder access to the account using passwd utility.

## ATT&CK Mapping

- [[kb/attack/techniques/T1531-account_access_removal|T1531: Account Access Removal]]

## Input Arguments

### user_account

- description: User account whose password will be changed.
- type: string
- default: ARTUser

## Executor

- elevation_required: True
- name: sh

### Command

```bash
passwd #{user_account} #enter admin password > enter new password > confirm new password
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1531/T1531.yaml)
