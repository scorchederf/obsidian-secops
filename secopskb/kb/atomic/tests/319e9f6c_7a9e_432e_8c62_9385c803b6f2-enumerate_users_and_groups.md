---
atomic_guid: "319e9f6c-7a9e-432e-8c62-9385c803b6f2"
title: "Enumerate users and groups"
framework: "atomic"
generated: "true"
attack_technique_id: "T1087.001"
attack_technique_name: "Account Discovery: Local Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.001/T1087.001.yaml"
build_date: "2026-04-26 14:38:39"
executor: "sh"
aliases:
  - "319e9f6c-7a9e-432e-8c62-9385c803b6f2"
  - "Enumerate users and groups"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Enumerate users and groups

Utilize local utilities to enumerate users and groups

## Metadata

- Atomic GUID: 319e9f6c-7a9e-432e-8c62-9385c803b6f2
- Technique: T1087.001: Account Discovery: Local Account
- Platforms: macos
- Executor: sh
- Source Path: atomics/T1087.001/T1087.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1087-account_discovery|T1087.001]]

## Executor

- name: sh

### Command

```sh
dscl . list /Groups
dscl . list /Users
dscl . list /Users | grep -v '_'
dscacheutil -q group
dscacheutil -q user
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.001/T1087.001.yaml)
