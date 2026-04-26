---
atomic_guid: "d2b95631-62d7-45a3-aaef-0972cea97931"
title: "Reactivate a locked/expired account (Linux)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1078.003"
attack_technique_name: "Valid Accounts: Local Accounts"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.003/T1078.003.yaml"
build_date: "2026-04-26 17:02:12"
executor: "bash"
aliases:
  - "d2b95631-62d7-45a3-aaef-0972cea97931"
  - "Reactivate a locked/expired account (Linux)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Reactivate a locked/expired account (Linux)

A system administrator may have locked and expired a user account rather than deleting it. "the user is coming back, at some stage" An adversary may reactivate a inactive account in an attempt to appear legitimate. 

In this test we create a "art" user with the password art, lock and expire the account, try to su to art and fail, unlock and renew the account, su successfully, then delete the account.

## Metadata

- Atomic GUID: d2b95631-62d7-45a3-aaef-0972cea97931
- Technique: T1078.003: Valid Accounts: Local Accounts
- Platforms: linux
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
useradd --shell /bin/bash --create-home --password $(openssl passwd -1 art) art
usermod --lock art
usermod --expiredate "1" art
usermod --unlock art
usermod --expiredate "99999" art
su -c whoami art
```

### Cleanup

```bash
userdel -r art
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.003/T1078.003.yaml)
