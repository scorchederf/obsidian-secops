---
atomic_guid: "de47f4a0-2acb-416d-9a6b-cee584a4c4d1"
title: "Add persistence via Windows Context Menu"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.001"
attack_technique_name: "Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.001/T1547.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "de47f4a0-2acb-416d-9a6b-cee584a4c4d1"
  - "Add persistence via Windows Context Menu"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Add persistence via Windows Context Menu

This atomic test add persistence taking advantage of the  Windows Context Menu [Hexacorn](https://www.hexacorn.com/blog/2018/07/29/beyond-good-ol-run-key-part-82/)
User have to right click on the main screen or in the white space of the opened folder (e.g. Size Modify).

## Metadata

- Atomic GUID: de47f4a0-2acb-416d-9a6b-cee584a4c4d1
- Technique: T1547.001: Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1547.001/T1547.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.001]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
reg add "HKEY_CLASSES_ROOT\Directory\Background\shell\Size Modify\command" /ve /t REG_SZ /d "C:\Windows\System32\calc.exe" /f
```

### Cleanup

```cmd
reg delete "HKEY_CLASSES_ROOT\Directory\Background\shell\Size Modify" /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.001/T1547.001.yaml)
