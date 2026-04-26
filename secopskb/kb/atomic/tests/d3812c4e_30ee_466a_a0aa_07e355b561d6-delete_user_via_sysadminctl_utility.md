---
atomic_guid: "d3812c4e-30ee-466a-a0aa-07e355b561d6"
title: "Delete User via sysadminctl utility"
framework: "atomic"
generated: "true"
attack_technique_id: "T1531"
attack_technique_name: "Account Access Removal"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1531/T1531.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "d3812c4e-30ee-466a-a0aa-07e355b561d6"
  - "Delete User via sysadminctl utility"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Delete User via sysadminctl utility

This test deletes the user account using the sysadminctl utility.

## Metadata

- Atomic GUID: d3812c4e-30ee-466a-a0aa-07e355b561d6
- Technique: T1531: Account Access Removal
- Platforms: macos
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1531/T1531.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1531-account_access_removal|T1531]]

## Input Arguments

### user_account

- description: User account which will be deleted.
- type: string
- default: ARTUserAccount

### user_name

- description: New user name.
- type: string
- default: ARTUser

### user_password

- description: New user password.
- type: string
- default: ARTPassword

## Executor

- elevation_required: True
- name: sh

### Command

```bash
sysadminctl -deleteUser #{user_account} #enter admin password
```

### Cleanup

```bash
sysadminctl -addUser #{user_account} -fullName "#{user_name}" -password #{user_password}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1531/T1531.yaml)
