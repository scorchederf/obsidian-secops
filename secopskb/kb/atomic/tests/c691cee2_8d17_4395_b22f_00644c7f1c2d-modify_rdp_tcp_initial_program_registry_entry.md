---
atomic_guid: "c691cee2-8d17-4395-b22f-00644c7f1c2d"
title: "Modify RDP-Tcp Initial Program Registry Entry"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "c691cee2-8d17-4395-b22f-00644c7f1c2d"
  - "Modify RDP-Tcp Initial Program Registry Entry"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Modify RDP-Tcp Initial Program Registry Entry

If the fInheritInitialProgram value is set to 1, the exe indicated in the InitialProgram value is automatically started on RDP connection.
Once the test commands are run, notepad will execute automatically on new RDP connection

## Metadata

- Atomic GUID: c691cee2-8d17-4395-b22f-00644c7f1c2d
- Technique: T1112: Modify Registry
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1112/T1112.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v fInheritInitialProgram /t REG_DWORD /d 1 /f
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v InitialProgram /t REG_SZ /d "C:\Windows\System32\notepad.exe" /f
```

### Cleanup

```cmd
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v InitialProgram /t REG_SZ /d "" /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
