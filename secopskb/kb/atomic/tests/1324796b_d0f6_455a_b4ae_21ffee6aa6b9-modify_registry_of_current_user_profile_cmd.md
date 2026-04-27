---
atomic_guid: "1324796b-d0f6-455a-b4ae-21ffee6aa6b9"
title: "Modify Registry of Current User Profile - cmd"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "1324796b-d0f6-455a-b4ae-21ffee6aa6b9"
  - "Modify Registry of Current User Profile - cmd"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Modify Registry of Current User Profile - cmd

Modify the registry of the currently logged in user using reg.exe via cmd console. Upon execution, the message "The operation completed successfully."
will be displayed. Additionally, open Registry Editor to view the new entry in HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced.

## Metadata

- Atomic GUID: 1324796b-d0f6-455a-b4ae-21ffee6aa6b9
- Technique: T1112: Modify Registry
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1112/T1112.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Executor

- name: command_prompt

### Command

```cmd
reg add HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced /t REG_DWORD /v HideFileExt /d 1 /f
```

### Cleanup

```cmd
reg delete HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced /v HideFileExt /f >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
