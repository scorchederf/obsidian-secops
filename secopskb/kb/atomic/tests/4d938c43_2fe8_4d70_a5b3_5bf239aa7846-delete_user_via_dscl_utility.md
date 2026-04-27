---
atomic_guid: "4d938c43-2fe8-4d70-a5b3-5bf239aa7846"
title: "Delete User via dscl utility"
framework: "atomic"
generated: "true"
attack_technique_id: "T1531"
attack_technique_name: "Account Access Removal"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1531/T1531.yaml"
build_date: "2026-04-27 19:12:27"
executor: "sh"
aliases:
  - "4d938c43-2fe8-4d70-a5b3-5bf239aa7846"
  - "Delete User via dscl utility"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test deletes the user account using the dscl utility.

## ATT&CK Mapping

- [[kb/attack/techniques/T1531-account_access_removal|T1531: Account Access Removal]]

## Input Arguments

### user_account

- description: User account which will be deleted.
- type: string
- default: ARTUser

### user_password

- description: User password.
- type: string
- default: ARTPassword

## Executor

- elevation_required: True
- name: sh

### Command

```bash
dscl . -delete /Users/#{user_account} #enter admin password
```

### Cleanup

```bash
dscl . -create /Users/#{user_account} #enter admin password
dscl . -create /Users/#{user_account} UserShell /bin/bash
dscl . -create /Users/#{user_account} UniqueID 503
dscl . -create /Users/#{user_account} NFSHomeDirectory /Users/#{user_account}
dscl . -passwd /Users/#{user_account} #{user_password} #enter password for new user
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1531/T1531.yaml)
