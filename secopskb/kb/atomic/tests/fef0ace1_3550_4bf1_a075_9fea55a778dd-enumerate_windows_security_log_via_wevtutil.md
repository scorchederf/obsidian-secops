---
atomic_guid: "fef0ace1-3550-4bf1-a075-9fea55a778dd"
title: "Enumerate Windows Security Log via WevtUtil"
framework: "atomic"
generated: "true"
attack_technique_id: "T1654"
attack_technique_name: "Log Enumeration"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1654/T1654.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "fef0ace1-3550-4bf1-a075-9fea55a778dd"
  - "Enumerate Windows Security Log via WevtUtil"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Enumerate Windows Security Log via WevtUtil

WevtUtil is a command line tool that can be utilised by adversaries to gather intelligence on a targeted Windows system's logging infrastructure. 

By executing this command, malicious actors can enumerate all available event logs, including both default logs such as Application, Security, and System
as well as any custom logs created by administrators. 

This information provides valuable insight into the system's logging mechanisms, potentially allowing attackers to identify gaps or weaknesses in the logging configuration

## Metadata

- Atomic GUID: fef0ace1-3550-4bf1-a075-9fea55a778dd
- Technique: T1654: Log Enumeration
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1654/T1654.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1654-log_enumeration|T1654]]

## Executor

- name: command_prompt

### Command

```commandprompt
wevtutil enum-logs
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1654/T1654.yaml)
