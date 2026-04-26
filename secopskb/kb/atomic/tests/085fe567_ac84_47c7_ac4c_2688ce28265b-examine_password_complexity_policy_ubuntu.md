---
atomic_guid: "085fe567-ac84-47c7-ac4c-2688ce28265b"
title: "Examine password complexity policy - Ubuntu"
framework: "atomic"
generated: "true"
attack_technique_id: "T1201"
attack_technique_name: "Password Policy Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1201/T1201.yaml"
build_date: "2026-04-26 17:02:12"
executor: "bash"
aliases:
  - "085fe567-ac84-47c7-ac4c-2688ce28265b"
  - "Examine password complexity policy - Ubuntu"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Examine password complexity policy - Ubuntu

Lists the password complexity policy to console on Ubuntu Linux.

## Metadata

- Atomic GUID: 085fe567-ac84-47c7-ac4c-2688ce28265b
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
cat /etc/pam.d/common-password
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1201/T1201.yaml)
