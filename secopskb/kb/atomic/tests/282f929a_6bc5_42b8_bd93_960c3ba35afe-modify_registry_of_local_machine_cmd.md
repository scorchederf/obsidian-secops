---
atomic_guid: "282f929a-6bc5-42b8-bd93-960c3ba35afe"
title: "Modify Registry of Local Machine - cmd"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "282f929a-6bc5-42b8-bd93-960c3ba35afe"
  - "Modify Registry of Local Machine - cmd"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Modify Registry of Local Machine - cmd

Modify the Local Machine registry RUN key to change Windows Defender executable that should be ran on startup.  This should only be possible when
CMD is ran as Administrative rights. Upon execution, the message "The operation completed successfully."
will be displayed. Additionally, open Registry Editor to view the modified entry in HKLM\Software\Microsoft\Windows\CurrentVersion\Run.

## Metadata

- Atomic GUID: 282f929a-6bc5-42b8-bd93-960c3ba35afe
- Technique: T1112: Modify Registry
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1112/T1112.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Input Arguments

### new_executable

- description: New executable to run on startup instead of Windows Defender
- type: string
- default: calc.exe

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
reg add HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run /t REG_EXPAND_SZ /v SecurityHealth /d #{new_executable} /f
```

### Cleanup

```commandprompt
reg delete HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run /v SecurityHealth /f >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
