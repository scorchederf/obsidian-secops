---
atomic_guid: "96257079-cdc1-4aba-8705-3146e94b6dce"
title: "Inspect SystemStartOptions Value in Registry"
framework: "atomic"
generated: "true"
attack_technique_id: "T1012"
attack_technique_name: "Query Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1012/T1012.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "96257079-cdc1-4aba-8705-3146e94b6dce"
  - "Inspect SystemStartOptions Value in Registry"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Inspect SystemStartOptions Value in Registry

The objective of this test is to query the SystemStartOptions key under HKLM\SYSTEM\CurrentControlSet\Control in the Windows registry. This action could be used to uncover specific details about how the system is configured to start, potentially aiding in understanding boot parameters or identifying security-related settings. key is.

## Metadata

- Atomic GUID: 96257079-cdc1-4aba-8705-3146e94b6dce
- Technique: T1012: Query Registry
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1012/T1012.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1012-query_registry|T1012]]

## Executor

- name: command_prompt

### Command

```cmd
reg.exe query HKLM\SYSTEM\CurrentControlSet\Control /v SystemStartOptions
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1012/T1012.yaml)
