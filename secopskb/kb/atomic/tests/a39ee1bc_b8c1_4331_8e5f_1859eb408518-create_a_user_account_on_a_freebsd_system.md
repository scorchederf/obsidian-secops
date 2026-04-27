---
atomic_guid: "a39ee1bc-b8c1-4331-8e5f-1859eb408518"
title: "Create a user account on a FreeBSD system"
framework: "atomic"
generated: "true"
attack_technique_id: "T1136.001"
attack_technique_name: "Create Account: Local Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1136.001/T1136.001.yaml"
build_date: "2026-04-27 19:12:27"
executor: "sh"
aliases:
  - "a39ee1bc-b8c1-4331-8e5f-1859eb408518"
  - "Create a user account on a FreeBSD system"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Create a user via pw

## ATT&CK Mapping

- [[kb/attack/techniques/T1136-create_account#^t1136001-local-account|T1136.001: Local Account]]

## Input Arguments

### username

- description: Username of the user to create
- type: string
- default: evil_user

## Executor

- elevation_required: True
- name: sh

### Command

```bash
pw useradd #{username} -s /usr/sbin/nologin -d /nonexistent -c evil_account
```

### Cleanup

```bash
rmuser -y #{username}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1136.001/T1136.001.yaml)
