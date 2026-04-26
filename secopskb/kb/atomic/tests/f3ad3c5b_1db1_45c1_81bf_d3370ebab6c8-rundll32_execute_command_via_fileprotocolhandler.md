---
atomic_guid: "f3ad3c5b-1db1-45c1-81bf-d3370ebab6c8"
title: "Rundll32 execute command via FileProtocolHandler"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.011"
attack_technique_name: "Signed Binary Proxy Execution: Rundll32"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.011/T1218.011.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "f3ad3c5b-1db1-45c1-81bf-d3370ebab6c8"
  - "Rundll32 execute command via FileProtocolHandler"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Rundll32 execute command via FileProtocolHandler

Test execution of a command using rundll32.exe and the FileProtocolHandler technique.
Upon execution, calc.exe will be launched.
This technique is documented by Levan Abesadze - https://medium.com/@Wolverineisstillalive/system-binary-proxy-execution-rundll32-bypass-method-790871e1f2b7

## Metadata

- Atomic GUID: f3ad3c5b-1db1-45c1-81bf-d3370ebab6c8
- Technique: T1218.011: Signed Binary Proxy Execution: Rundll32
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1218.011/T1218.011.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

## Input Arguments

### command_to_execute

- description: Command for rundll32.exe to execute
- type: string
- default: calc.exe

## Executor

- name: command_prompt

### Command

```cmd
rundll32.exe url.dll,FileProtocolHandler #{command_to_execute}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.011/T1218.011.yaml)
