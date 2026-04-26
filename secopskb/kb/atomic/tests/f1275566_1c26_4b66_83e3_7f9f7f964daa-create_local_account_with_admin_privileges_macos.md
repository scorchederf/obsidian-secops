---
atomic_guid: "f1275566-1c26-4b66-83e3-7f9f7f964daa"
title: "Create local account with admin privileges - MacOS"
framework: "atomic"
generated: "true"
attack_technique_id: "T1078.003"
attack_technique_name: "Valid Accounts: Local Accounts"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.003/T1078.003.yaml"
build_date: "2026-04-26 14:38:39"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Create local account with admin privileges - MacOS

After execution the new account will be active and added to the Administrators group

## Metadata

- Atomic GUID: f1275566-1c26-4b66-83e3-7f9f7f964daa
- Technique: T1078.003: Valid Accounts: Local Accounts
- Platforms: macos
- Executor: bash
- Elevation Required: True
- Source Path: atomics/T1078.003/T1078.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1078-valid_accounts|T1078.003]]

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
