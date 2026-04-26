---
atomic_guid: "dea6c349-f1c6-44f3-87a1-1ed33a59a607"
title: "Dump LSASS.exe Memory using Windows Task Manager"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.001"
attack_technique_name: "OS Credential Dumping: LSASS Memory"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.001/T1003.001.yaml"
build_date: "2026-04-26 14:38:39"
executor: "manual"
aliases:
  - "dea6c349-f1c6-44f3-87a1-1ed33a59a607"
  - "Dump LSASS.exe Memory using Windows Task Manager"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Dump LSASS.exe Memory using Windows Task Manager

The memory of lsass.exe is often dumped for offline credential theft attacks. This can be achieved with the Windows Task
Manager and administrative permissions.

## Metadata

- Atomic GUID: dea6c349-f1c6-44f3-87a1-1ed33a59a607
- Technique: T1003.001: OS Credential Dumping: LSASS Memory
- Platforms: windows
- Executor: manual
- Source Path: atomics/T1003.001/T1003.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Executor

- name: manual
- steps: 1. Open Task Manager:
  On a Windows system this can be accomplished by pressing CTRL-ALT-DEL and selecting Task Manager or by right-clicking
  on the task bar and selecting "Task Manager".

2. Select lsass.exe:
  If lsass.exe is not visible, select "Show processes from all users". This will allow you to observe execution of lsass.exe
  and select it for manipulation.

3. Dump lsass.exe memory:
  Right-click on lsass.exe in Task Manager. Select "Create Dump File". The following dialog will show you the path to the saved file.


## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.001/T1003.001.yaml)
