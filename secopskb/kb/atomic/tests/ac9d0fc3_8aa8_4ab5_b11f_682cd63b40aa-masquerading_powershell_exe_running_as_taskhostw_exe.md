---
atomic_guid: "ac9d0fc3-8aa8-4ab5-b11f-682cd63b40aa"
title: "Masquerading - powershell.exe running as taskhostw.exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1036.003"
attack_technique_name: "Masquerading: Rename System Utilities"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036.003/T1036.003.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "ac9d0fc3-8aa8-4ab5-b11f-682cd63b40aa"
  - "Masquerading - powershell.exe running as taskhostw.exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Masquerading - powershell.exe running as taskhostw.exe

Copies powershell.exe, renames it, and launches it to masquerade as an instance of taskhostw.exe.

Upon successful execution, powershell.exe is renamed as taskhostw.exe and executed from non-standard path.

## Metadata

- Atomic GUID: ac9d0fc3-8aa8-4ab5-b11f-682cd63b40aa
- Technique: T1036.003: Masquerading: Rename System Utilities
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1036.003/T1036.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1036-masquerading|T1036.003]]

## Executor

- name: command_prompt

### Command

```cmd
copy %windir%\System32\windowspowershell\v1.0\powershell.exe %APPDATA%\taskhostw.exe /Y
cmd.exe /K %APPDATA%\taskhostw.exe
```

### Cleanup

```cmd
del /Q /F %APPDATA%\taskhostw.exe >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036.003/T1036.003.yaml)
