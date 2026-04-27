---
atomic_guid: "02a91c34-8a5b-4bed-87af-501103eb5357"
title: "Create local account (Linux)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1078.003"
attack_technique_name: "Valid Accounts: Local Accounts"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.003/T1078.003.yaml"
build_date: "2026-04-27 19:12:26"
executor: "bash"
aliases:
  - "02a91c34-8a5b-4bed-87af-501103eb5357"
  - "Create local account (Linux)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

An adversary may wish to create an account with admin privileges to work with. In this test we create a "art" user with the password art, switch to art, execute whoami, exit and delete the art user.

## ATT&CK Mapping

- [[kb/attack/techniques/T1078-valid_accounts#^t1078003-local-accounts|T1078.003: Local Accounts]]

## Executor

- elevation_required: True
- name: bash

### Command

```bash
password=$(openssl passwd -1 art)
([ "$(uname)" = 'Linux' ] && useradd --shell /bin/bash --create-home --password $password art) || (pw useradd art -g wheel -s /bin/sh && (echo $password | pw mod user testuser1 -h 0))
su art -c "whoami; exit"
```

### Cleanup

```bash
[ "$(uname)" = 'Linux' ] && userdel art -rf || rmuser -y art
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.003/T1078.003.yaml)
