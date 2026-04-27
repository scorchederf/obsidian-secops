---
atomic_guid: "127b4afe-2346-4192-815c-69042bec570e"
title: "Writes text to a file and displays it."
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.003"
attack_technique_name: "Command and Scripting Interpreter: Windows Command Shell"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.003/T1059.003.yaml"
build_date: "2026-04-27 19:12:26"
executor: "command_prompt"
aliases:
  - "127b4afe-2346-4192-815c-69042bec570e"
  - "Writes text to a file and displays it."
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Writes text to a file and display the results. This test is intended to emulate the dropping of a malicious file to disk.

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059003-windows-command-shell|T1059.003: Windows Command Shell]]

## Input Arguments

### file_contents_path

- description: Path to the file that the command prompt will drop.
- type: path
- default: %TEMP%\test.bin

### message

- description: Message that will be written to disk and then displayed.
- type: string
- default: Hello from the Windows Command Prompt!

## Executor

- name: command_prompt

### Command

```cmd
echo "#{message}" > "#{file_contents_path}" & type "#{file_contents_path}"
```

### Cleanup

```cmd
del "#{file_contents_path}" >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.003/T1059.003.yaml)
