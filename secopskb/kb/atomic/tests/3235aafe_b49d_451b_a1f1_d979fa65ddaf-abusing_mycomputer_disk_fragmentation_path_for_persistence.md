---
atomic_guid: "3235aafe-b49d-451b-a1f1-d979fa65ddaf"
title: "Abusing MyComputer Disk Fragmentation Path for Persistence"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "3235aafe-b49d-451b-a1f1-d979fa65ddaf"
  - "Abusing MyComputer Disk Fragmentation Path for Persistence"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Abusing MyComputer Disk Fragmentation Path for Persistence

Replacing the registry settings with custom executable will end up with the replacement programs being executed at the time OS will decide to kick off the respective activity

## Metadata

- Atomic GUID: 3235aafe-b49d-451b-a1f1-d979fa65ddaf
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

```commandprompt
reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\DefragPath" /t REG_EXPAND_SZ /d "%systemroot%\system32\notepad.exe" /f
```

### Cleanup

```commandprompt
reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\DefragPath" /t REG_EXPAND_SZ /d "%systemroot%\system32\dfrgui.exe" /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
