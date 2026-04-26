---
atomic_guid: "83810c46-f45e-4485-9ab6-8ed0e9e6ed7f"
title: "Malicious process Masquerading as LSM.exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1036.003"
attack_technique_name: "Masquerading: Rename System Utilities"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036.003/T1036.003.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "83810c46-f45e-4485-9ab6-8ed0e9e6ed7f"
  - "Malicious process Masquerading as LSM.exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Malicious process Masquerading as LSM.exe

Detect LSM running from an incorrect directory and an incorrect service account
This works by copying cmd.exe to a file, naming it lsm.exe, then copying a file to the C:\ folder.

Upon successful execution, cmd.exe will be renamed as lsm.exe and executed from non-standard path.

## Metadata

- Atomic GUID: 83810c46-f45e-4485-9ab6-8ed0e9e6ed7f
- Technique: T1036.003: Masquerading: Rename System Utilities
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1036.003/T1036.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1036-masquerading|T1036.003]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
copy C:\Windows\System32\cmd.exe C:\lsm.exe
C:\lsm.exe /c echo T1036.003 > C:\T1036.003.txt
```

### Cleanup

```commandprompt
del C:\T1036.003.txt >nul 2>&1
del C:\lsm.exe >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036.003/T1036.003.yaml)
