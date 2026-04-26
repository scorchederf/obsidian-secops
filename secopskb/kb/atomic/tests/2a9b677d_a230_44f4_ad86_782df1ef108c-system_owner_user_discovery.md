---
atomic_guid: "2a9b677d-a230-44f4-ad86-782df1ef108c"
title: "System Owner/User Discovery"
framework: "atomic"
generated: "true"
attack_technique_id: "T1033"
attack_technique_name: "System Owner/User Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1033/T1033.yaml"
build_date: "2026-04-26 14:38:39"
executor: "sh"
aliases:
  - "2a9b677d-a230-44f4-ad86-782df1ef108c"
  - "System Owner/User Discovery"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# System Owner/User Discovery

Identify System owner or users on an endpoint

Upon successful execution, sh will stdout list of usernames.

## Metadata

- Atomic GUID: 2a9b677d-a230-44f4-ad86-782df1ef108c
- Technique: T1033: System Owner/User Discovery
- Platforms: linux, macos
- Executor: sh
- Source Path: atomics/T1033/T1033.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1033-system_owner_user_discovery|T1033]]

## Executor

- name: sh

### Command

```sh
users
w
who
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1033/T1033.yaml)
