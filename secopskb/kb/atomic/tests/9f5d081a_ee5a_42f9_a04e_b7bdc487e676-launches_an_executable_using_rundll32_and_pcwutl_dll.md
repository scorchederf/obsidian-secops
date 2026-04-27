---
atomic_guid: "9f5d081a-ee5a-42f9-a04e-b7bdc487e676"
title: "Launches an executable using Rundll32 and pcwutl.dll"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.011"
attack_technique_name: "Signed Binary Proxy Execution: Rundll32"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.011/T1218.011.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "9f5d081a-ee5a-42f9-a04e-b7bdc487e676"
  - "Launches an executable using Rundll32 and pcwutl.dll"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Launches an executable using Rundll32 and pcwutl.dll

Executes the LaunchApplication function in pcwutl.dll to proxy execution of an executable.

## Metadata

- Atomic GUID: 9f5d081a-ee5a-42f9-a04e-b7bdc487e676
- Technique: T1218.011: Signed Binary Proxy Execution: Rundll32
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1218.011/T1218.011.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

## Input Arguments

### exe_to_launch

- description: Path of the executable to launch
- type: path
- default: %windir%\System32\notepad.exe

## Executor

- name: command_prompt

### Command

```cmd
rundll32.exe pcwutl.dll,LaunchApplication #{exe_to_launch}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.011/T1218.011.yaml)
