---
atomic_guid: "09e3380a-fae5-4255-8b19-9950be0252cf"
title: "Reactivate a locked/expired account (FreeBSD)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1078.003"
attack_technique_name: "Valid Accounts: Local Accounts"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.003/T1078.003.yaml"
build_date: "2026-04-27 19:12:26"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

A system administrator may have locked and expired a user account rather than deleting it. "the user is coming back, at some stage" An adversary may reactivate a inactive account in an attempt to appear legitimate. 

In this test we create a "art" user with the password art, lock and expire the account, try to su to art and fail, unlock and renew the account, su successfully, then delete the account.

## ATT&CK Mapping

- [[kb/attack/techniques/T1078-valid_accounts#^t1078003-local-accounts|T1078.003: Local Accounts]]

## Executor

- elevation_required: True
- name: sh

### Command

```bash
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

```bash
rmuser -y art
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.003/T1078.003.yaml)
