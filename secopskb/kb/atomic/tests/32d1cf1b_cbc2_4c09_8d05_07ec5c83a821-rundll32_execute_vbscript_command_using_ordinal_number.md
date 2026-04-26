---
atomic_guid: "32d1cf1b-cbc2-4c09-8d05-07ec5c83a821"
title: "Rundll32 execute VBscript command using Ordinal number"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.011"
attack_technique_name: "Signed Binary Proxy Execution: Rundll32"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.011/T1218.011.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "32d1cf1b-cbc2-4c09-8d05-07ec5c83a821"
  - "Rundll32 execute VBscript command using Ordinal number"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Rundll32 execute VBscript command using Ordinal number

Test execution of a command using rundll32.exe and VBscript in a similar manner to the JavaScript test.
Technique documented by Hexacorn- http://www.hexacorn.com/blog/2019/10/29/rundll32-with-a-vbscript-protocol/
Upon execution calc.exe will be launched

## Metadata

- Atomic GUID: 32d1cf1b-cbc2-4c09-8d05-07ec5c83a821
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

```commandprompt
rundll32 vbscript:"\..\mshtml,#135 "+String(CreateObject("WScript.Shell").Run("#{command_to_execute}"),0)
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.011/T1218.011.yaml)
