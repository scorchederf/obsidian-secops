---
atomic_guid: "81483501-b8a5-4225-8b32-52128e2f69db"
title: "Event Viewer Registry Modification - Redirection Program"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "81483501-b8a5-4225-8b32-52128e2f69db"
  - "Event Viewer Registry Modification - Redirection Program"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Event Viewer Registry Modification - Redirection Program

Modify event viewer registry values to alter the behavior of the online help redirection. Upon opening an event in event viewer and attempting to view the help page for the event, it will execute the program defined in the redirection program registry entry.

## Metadata

- Atomic GUID: 81483501-b8a5-4225-8b32-52128e2f69db
- Technique: T1112: Modify Registry
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1112/T1112.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Input Arguments

### redirection_program

- description: Path of the program to execute upon opening the event help
- type: path
- default: C:\windows\system32\notepad.exe

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Event Viewer" /v MicrosoftRedirectionProgram /t REG_EXPAND_SZ /d "#{redirection_program}" /f
```

### Cleanup

```cmd
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Event Viewer" /v MicrosoftRedirectionProgram /t REG_EXPAND_SZ /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
