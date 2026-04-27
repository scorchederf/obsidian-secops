---
atomic_guid: "191db57d-091a-47d5-99f3-97fde53de505"
title: "Create local account with admin privileges using sysadminctl utility - MacOS"
framework: "atomic"
generated: "true"
attack_technique_id: "T1078.003"
attack_technique_name: "Valid Accounts: Local Accounts"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.003/T1078.003.yaml"
build_date: "2026-04-27 19:12:26"
executor: "bash"
aliases:
  - "191db57d-091a-47d5-99f3-97fde53de505"
  - "Create local account with admin privileges using sysadminctl utility - MacOS"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

After execution the new account will be active and added to the Administrators group

## ATT&CK Mapping

- [[kb/attack/techniques/T1078-valid_accounts#^t1078003-local-accounts|T1078.003: Local Accounts]]

## Executor

- elevation_required: True
- name: bash

### Command

```bash
sysadminctl interactive -addUser art-tester -fullName ARTUser -password !pass123! -admin
```

### Cleanup

```bash
sysadminctl interactive -deleteUser art-tester
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.003/T1078.003.yaml)
