---
atomic_guid: "3a2a578b-0a01-46e4-92e3-62e2859b42f0"
title: "Masquerading - cscript.exe running as notepad.exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1036.003"
attack_technique_name: "Masquerading: Rename System Utilities"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036.003/T1036.003.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "3a2a578b-0a01-46e4-92e3-62e2859b42f0"
  - "Masquerading - cscript.exe running as notepad.exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Masquerading - cscript.exe running as notepad.exe

Copies cscript.exe, renames it, and launches it to masquerade as an instance of notepad.exe.

Upon successful execution, cscript.exe is renamed as notepad.exe and executed from non-standard path.

## Metadata

- Atomic GUID: 3a2a578b-0a01-46e4-92e3-62e2859b42f0
- Technique: T1036.003: Masquerading: Rename System Utilities
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1036.003/T1036.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1036-masquerading|T1036.003]]

## Executor

- name: command_prompt

### Command

```commandprompt
copy %SystemRoot%\System32\cscript.exe %APPDATA%\notepad.exe /Y
cmd.exe /c %APPDATA%\notepad.exe /B
```

### Cleanup

```commandprompt
del /Q /F %APPDATA%\notepad.exe >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036.003/T1036.003.yaml)
