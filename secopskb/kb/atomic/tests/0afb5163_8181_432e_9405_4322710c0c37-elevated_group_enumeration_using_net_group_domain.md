---
atomic_guid: "0afb5163-8181-432e-9405-4322710c0c37"
title: "Elevated group enumeration using net group (Domain)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1069.002"
attack_technique_name: "Permission Groups Discovery: Domain Groups"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.002/T1069.002.yaml"
build_date: "2026-04-27 19:12:26"
executor: "command_prompt"
aliases:
  - "0afb5163-8181-432e-9405-4322710c0c37"
  - "Elevated group enumeration using net group (Domain)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Runs "net group" command including command aliases and loose typing to simulate enumeration/discovery of high value domain groups. This
test will display some errors if run on a computer not connected to a domain. Upon execution, domain information will be displayed.

## ATT&CK Mapping

- [[kb/attack/techniques/T1069-permission_groups_discovery#^t1069002-domain-groups|T1069.002: Domain Groups]]

## Executor

- name: command_prompt

### Command

```cmd
net groups "Account Operators" /domain
net groups "Exchange Organization Management" /domain
net group "BUILTIN\Backup Operators" /domain
net group "Domain Admins" /domain
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.002/T1069.002.yaml)
