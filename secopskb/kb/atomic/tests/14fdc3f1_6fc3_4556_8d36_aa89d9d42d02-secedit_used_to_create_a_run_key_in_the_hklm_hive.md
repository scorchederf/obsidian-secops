---
atomic_guid: "14fdc3f1-6fc3-4556-8d36-aa89d9d42d02"
title: "secedit used to create a Run key in the HKLM Hive"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.001"
attack_technique_name: "Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.001/T1547.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "14fdc3f1-6fc3-4556-8d36-aa89d9d42d02"
  - "secedit used to create a Run key in the HKLM Hive"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# secedit used to create a Run key in the HKLM Hive

secedit allows to manipulate the HKLM hive of the Windows registry. This test creates a Run key with the keyname calc having calc.exe as the value in the HKLM hive.
[Reference](https://blueteamops.medium.com/secedit-and-i-know-it-595056dee53d)

## Metadata

- Atomic GUID: 14fdc3f1-6fc3-4556-8d36-aa89d9d42d02
- Technique: T1547.001: Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1547.001/T1547.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.001]]

## Input Arguments

### ini_file

- description: INI config template
- type: string
- default: $PathToAtomicsFolder\T1547.001\src\regtemplate.ini

### secedit_db

- description: Custom secedit db
- type: string
- default: mytemplate.db

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
secedit /import /db #{secedit_db} /cfg "#{ini_file}"
secedit /configure /db #{secedit_db}
```

### Cleanup

```cmd
REG DELETE "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "calc" /f >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.001/T1547.001.yaml)
