---
atomic_guid: "2a8f2d3c-3dec-4262-99dd-150cb2a4d63a"
title: "manage-bde.wsf Signed Script Command Execution"
framework: "atomic"
generated: "true"
attack_technique_id: "T1216"
attack_technique_name: "Signed Script Proxy Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1216/T1216.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "2a8f2d3c-3dec-4262-99dd-150cb2a4d63a"
  - "manage-bde.wsf Signed Script Command Execution"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Executes the signed manage-bde.wsf script with options to execute an arbitrary command.

## ATT&CK Mapping

- [[kb/attack/techniques/T1216-system_script_proxy_execution|T1216: System Script Proxy Execution]]

## Input Arguments

### command_to_execute

- description: A command to execute.
- type: path
- default: %windir%\System32\calc.exe

## Executor

- name: command_prompt

### Command

```cmd
set comspec=#{command_to_execute}
cscript %windir%\System32\manage-bde.wsf
```

### Cleanup

```cmd
set comspec=%windir%\System32\cmd.exe
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1216/T1216.yaml)
