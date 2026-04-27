---
atomic_guid: "d5d5a6b0-0f92-42d8-985d-47aafa2dd4db"
title: "System Time Discovery W32tm as a Delay"
framework: "atomic"
generated: "true"
attack_technique_id: "T1124"
attack_technique_name: "System Time Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1124/T1124.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "d5d5a6b0-0f92-42d8-985d-47aafa2dd4db"
  - "System Time Discovery W32tm as a Delay"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

identifies DCRat delay time tactics using w32tm.
https://research.splunk.com/endpoint/b2cc69e7-11ba-42dc-a269-59c069a48870/
https://blogs.blackberry.com/en/2022/05/dirty-deeds-done-dirt-cheap-russian-rat-offers-backdoor-bargains

## ATT&CK Mapping

- [[kb/attack/techniques/T1124-system_time_discovery|T1124: System Time Discovery]]

## Executor

- name: command_prompt

### Command

```cmd
W32tm /stripchart /computer:localhost /period:5 /dataonly /samples:2
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1124/T1124.yaml)
