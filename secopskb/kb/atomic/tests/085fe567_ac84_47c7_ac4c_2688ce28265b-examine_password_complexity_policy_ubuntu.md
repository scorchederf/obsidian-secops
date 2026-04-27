---
atomic_guid: "085fe567-ac84-47c7-ac4c-2688ce28265b"
title: "Examine password complexity policy - Ubuntu"
framework: "atomic"
generated: "true"
attack_technique_id: "T1201"
attack_technique_name: "Password Policy Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1201/T1201.yaml"
build_date: "2026-04-27 19:12:27"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Lists the password complexity policy to console on Ubuntu Linux.

## ATT&CK Mapping

- [[kb/attack/techniques/T1201-password_policy_discovery|T1201: Password Policy Discovery]]

## Executor

- name: bash

### Command

```bash
cat /etc/pam.d/common-password
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1201/T1201.yaml)
