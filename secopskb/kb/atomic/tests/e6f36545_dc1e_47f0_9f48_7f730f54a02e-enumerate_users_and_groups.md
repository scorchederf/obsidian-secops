---
atomic_guid: "e6f36545-dc1e-47f0-9f48-7f730f54a02e"
title: "Enumerate users and groups"
framework: "atomic"
generated: "true"
attack_technique_id: "T1087.001"
attack_technique_name: "Account Discovery: Local Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.001/T1087.001.yaml"
build_date: "2026-04-27 19:12:26"
executor: "sh"
aliases:
  - "e6f36545-dc1e-47f0-9f48-7f730f54a02e"
  - "Enumerate users and groups"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Utilize groups and id to enumerate users and groups

## ATT&CK Mapping

- [[kb/attack/techniques/T1087-account_discovery#^t1087001-local-account|T1087.001: Local Account]]

## Executor

- name: sh

### Command

```bash
groups
id
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.001/T1087.001.yaml)
