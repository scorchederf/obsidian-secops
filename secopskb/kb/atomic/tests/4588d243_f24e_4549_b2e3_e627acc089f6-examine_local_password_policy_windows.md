---
atomic_guid: "4588d243-f24e-4549-b2e3-e627acc089f6"
title: "Examine local password policy - Windows"
framework: "atomic"
generated: "true"
attack_technique_id: "T1201"
attack_technique_name: "Password Policy Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1201/T1201.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "4588d243-f24e-4549-b2e3-e627acc089f6"
  - "Examine local password policy - Windows"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Lists the local password policy to console on Windows.

## ATT&CK Mapping

- [[kb/attack/techniques/T1201-password_policy_discovery|T1201: Password Policy Discovery]]

## Executor

- name: command_prompt

### Command

```cmd
net accounts
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1201/T1201.yaml)
