---
atomic_guid: "573d15da-c34e-4c59-a7d2-18f20d92dfa3"
title: "Adding custom paths for application execution"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "573d15da-c34e-4c59-a7d2-18f20d92dfa3"
  - "Adding custom paths for application execution"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Adding custom paths for application execution

As per Microsoft,the entries found under App Paths are used primarily to map an application’s executable file name to that file’s fully qualified path and to pre-pend information to the PATH environment variable on a per-application, per-process basis. 
The path can be modified to load a custom application of choice. 
Post the registry changes of this test, when someone tries to manually run msedge.exe via StartMenu/Run window , notepad will be launched.

## Metadata

- Atomic GUID: 573d15da-c34e-4c59-a7d2-18f20d92dfa3
- Technique: T1112: Modify Registry
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1112/T1112.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Input Arguments

### app_name

- description: path of application to be modified
- type: string
- default: msedge.exe

### new_path

- description: New App Path Added
- type: string
- default: C:\Windows\System32\notepad.exe

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\#{app_name}" /t REG_SZ /d #{new_path} /f
```

### Cleanup

```cmd
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\#{app_name}" /v (Default) /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\#{app_name}" /t REG_SZ /d "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
