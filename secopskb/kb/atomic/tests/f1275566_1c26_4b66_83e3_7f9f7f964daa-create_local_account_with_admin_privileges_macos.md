---
atomic_guid: "f1275566-1c26-4b66-83e3-7f9f7f964daa"
title: "Create local account with admin privileges - MacOS"
framework: "atomic"
generated: "true"
attack_technique_id: "T1078.003"
attack_technique_name: "Valid Accounts: Local Accounts"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.003/T1078.003.yaml"
build_date: "2026-04-27 19:12:26"
executor: "bash"
aliases:
  - "f1275566-1c26-4b66-83e3-7f9f7f964daa"
  - "Create local account with admin privileges - MacOS"
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
dscl . -create /Users/AtomicUser
dscl . -create /Users/AtomicUser UserShell /bin/bash
dscl . -create /Users/AtomicUser RealName "Atomic User"
dscl . -create /Users/AtomicUser UniqueID 503
dscl . -create /Users/AtomicUser PrimaryGroupID 503
dscl . -create /Users/AtomicUser NFSHomeDirectory /Local/Users/AtomicUser
dscl . -passwd /Users/AtomicUser mySecretPassword
dscl . -append /Groups/admin GroupMembership AtomicUser
```

### Cleanup

```bash
sudo dscl . -delete /Users/AtomicUser
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.003/T1078.003.yaml)
