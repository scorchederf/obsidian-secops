---
atomic_guid: "433842ba-e796-4fd5-a14f-95d3a1970875"
title: "Add a new/existing user to the admin group using dseditgroup utility - macOS"
framework: "atomic"
generated: "true"
attack_technique_id: "T1078.003"
attack_technique_name: "Valid Accounts: Local Accounts"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.003/T1078.003.yaml"
build_date: "2026-04-27 19:12:26"
executor: "bash"
aliases:
  - "433842ba-e796-4fd5-a14f-95d3a1970875"
  - "Add a new/existing user to the admin group using dseditgroup utility - macOS"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

After execution the current/new user will be added to the Admin group

## ATT&CK Mapping

- [[kb/attack/techniques/T1078-valid_accounts#^t1078003-local-accounts|T1078.003: Local Accounts]]

## Executor

- elevation_required: True
- name: bash

### Command

```bash
dseditgroup -o edit -a art-user -t user admin
```

### Cleanup

```bash
dseditgroup -o edit -d art-user -t user admin
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.003/T1078.003.yaml)
