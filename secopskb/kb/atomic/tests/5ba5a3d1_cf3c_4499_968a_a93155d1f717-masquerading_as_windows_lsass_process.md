---
atomic_guid: "5ba5a3d1-cf3c-4499-968a-a93155d1f717"
title: "Masquerading as Windows LSASS process"
framework: "atomic"
generated: "true"
attack_technique_id: "T1036.003"
attack_technique_name: "Masquerading: Rename System Utilities"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036.003/T1036.003.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "5ba5a3d1-cf3c-4499-968a-a93155d1f717"
  - "Masquerading as Windows LSASS process"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Masquerading as Windows LSASS process

Copies cmd.exe, renames it, and launches it to masquerade as an instance of lsass.exe.

Upon execution, cmd will be launched by powershell. If using Invoke-AtomicTest, The test will hang until the 120 second timeout cancels the session

## Metadata

- Atomic GUID: 5ba5a3d1-cf3c-4499-968a-a93155d1f717
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
copy %SystemRoot%\System32\cmd.exe %SystemRoot%\Temp\lsass.exe
%SystemRoot%\Temp\lsass.exe /B
```

### Cleanup

```commandprompt
del /Q /F %SystemRoot%\Temp\lsass.exe >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036.003/T1036.003.yaml)
