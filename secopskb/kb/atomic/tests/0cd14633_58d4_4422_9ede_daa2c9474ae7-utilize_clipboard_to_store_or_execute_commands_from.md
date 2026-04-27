---
atomic_guid: "0cd14633-58d4-4422-9ede-daa2c9474ae7"
title: "Utilize Clipboard to store or execute commands from"
framework: "atomic"
generated: "true"
attack_technique_id: "T1115"
attack_technique_name: "Clipboard Data"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1115/T1115.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "0cd14633-58d4-4422-9ede-daa2c9474ae7"
  - "Utilize Clipboard to store or execute commands from"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Add data to clipboard to copy off or execute commands from.

## ATT&CK Mapping

- [[kb/attack/techniques/T1115-clipboard_data|T1115: Clipboard Data]]

## Executor

- name: command_prompt

### Command

```cmd
dir | clip
echo "T1115" > %temp%\T1115.txt
clip < %temp%\T1115.txt
```

### Cleanup

```cmd
del %temp%\T1115.txt >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1115/T1115.yaml)
