---
atomic_guid: "09e3380a-fae5-4255-8b19-9950be0252cf"
title: "Reactivate a locked/expired account (FreeBSD)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1078.003"
attack_technique_name: "Valid Accounts: Local Accounts"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.003/T1078.003.yaml"
build_date: "2026-04-26 14:38:39"
executor: "sh"
aliases:
  - "09e3380a-fae5-4255-8b19-9950be0252cf"
  - "Reactivate a locked/expired account (FreeBSD)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Reactivate a locked/expired account (FreeBSD)

A system administrator may have locked and expired a user account rather than deleting it. "the user is coming back, at some stage" An adversary may reactivate a inactive account in an attempt to appear legitimate. 

In this test we create a "art" user with the password art, lock and expire the account, try to su to art and fail, unlock and renew the account, su successfully, then delete the account.

## Metadata

- Atomic GUID: 09e3380a-fae5-4255-8b19-9950be0252cf
- Technique: T1078.003: Valid Accounts: Local Accounts
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1078.003/T1078.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1078-valid_accounts|T1078.003]]

## Executor

- elevation_required: True
- name: sh

### Command

```sh
pw useradd art -g wheel -s /bin/sh
echo $(openssl passwd -1 art) | pw mod user testuser1 -h 0
pw lock art
pw usermod art -e +1d
pw unlock art
pw user mod art -e +99d
su art
whoami
exit
```

### Cleanup

```sh
rmuser -y art
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.003/T1078.003.yaml)
