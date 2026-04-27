---
atomic_guid: "7c86c55c-70fa-4a05-83c9-3aa19b145d1a"
title: "Examine password expiration policy - All Linux"
framework: "atomic"
generated: "true"
attack_technique_id: "T1201"
attack_technique_name: "Password Policy Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1201/T1201.yaml"
build_date: "2026-04-26 17:02:12"
executor: "bash"
aliases:
  - "7c86c55c-70fa-4a05-83c9-3aa19b145d1a"
  - "Examine password expiration policy - All Linux"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Examine password expiration policy - All Linux

Lists the password expiration policy to console on CentOS/RHEL/Ubuntu.

## Metadata

- Atomic GUID: 7c86c55c-70fa-4a05-83c9-3aa19b145d1a
- Technique: T1201: Password Policy Discovery
- Platforms: linux
- Executor: bash
- Source Path: atomics/T1201/T1201.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1201-password_policy_discovery|T1201]]

## Executor

- name: bash

### Command

```bash
cat /etc/login.defs
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1201/T1201.yaml)
