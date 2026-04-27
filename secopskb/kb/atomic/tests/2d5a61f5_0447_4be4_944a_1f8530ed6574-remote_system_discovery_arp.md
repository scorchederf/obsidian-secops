---
atomic_guid: "2d5a61f5-0447-4be4-944a-1f8530ed6574"
title: "Remote System Discovery - arp"
framework: "atomic"
generated: "true"
attack_technique_id: "T1018"
attack_technique_name: "Remote System Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1018/T1018.yaml"
build_date: "2026-04-27 19:12:25"
executor: "command_prompt"
aliases:
  - "2d5a61f5-0447-4be4-944a-1f8530ed6574"
  - "Remote System Discovery - arp"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Identify remote systems via arp. 

Upon successful execution, cmd.exe will execute arp to list out the arp cache. Output will be via stdout.

## ATT&CK Mapping

- [[kb/attack/techniques/T1018-remote_system_discovery|T1018: Remote System Discovery]]

## Executor

- name: command_prompt

### Command

```cmd
arp -a
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1018/T1018.yaml)
