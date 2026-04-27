---
atomic_guid: "cb379146-53f1-43e0-b884-7ce2c635ff5b"
title: "Automated Collection Command Prompt"
framework: "atomic"
generated: "true"
attack_technique_id: "T1119"
attack_technique_name: "Automated Collection"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1119/T1119.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "cb379146-53f1-43e0-b884-7ce2c635ff5b"
  - "Automated Collection Command Prompt"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Automated Collection. Upon execution, check the users temp directory (%temp%) for the folder T1119_command_prompt_collection
to see what was collected.

## ATT&CK Mapping

- [[kb/attack/techniques/T1119-automated_collection|T1119: Automated Collection]]

## Executor

- name: command_prompt

### Command

```cmd
mkdir %temp%\T1119_command_prompt_collection >nul 2>&1
dir c: /b /s .docx | findstr /e .docx
for /R c:\ %f in (*.docx) do copy /Y %f %temp%\T1119_command_prompt_collection
```

### Cleanup

```cmd
del %temp%\T1119_command_prompt_collection /F /Q >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1119/T1119.yaml)
