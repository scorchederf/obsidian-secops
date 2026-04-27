---
atomic_guid: "b7fc4c3f-fe6e-479a-ba27-ef91b88536e3"
title: "Persistence using automatic execution of custom DLL during RDP session"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546"
attack_technique_name: "Event Triggered Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546/T1546.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "b7fc4c3f-fe6e-479a-ba27-ef91b88536e3"
  - "Persistence using automatic execution of custom DLL during RDP session"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Persistence using automatic execution of custom DLL during RDP session

When remote desktop session is accepted, the system queries the key it queries the Registry key:HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server\AddIns\TestDVCPlugin. 
If such key exists, the OS will attempt to read the Path value underneath.Once the Path is read, the DLL that it points to will be loaded via LoadLibrary.

## Metadata

- Atomic GUID: b7fc4c3f-fe6e-479a-ba27-ef91b88536e3
- Technique: T1546: Event Triggered Execution
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1546/T1546.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server\AddIns\TestDVCPlugin" /v Path /t REG_SZ /d "C:\Windows\System32\amsi.dll" /f
```

### Cleanup

```cmd
reg delete "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server\AddIns\TestDVCPlugin" /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546/T1546.yaml)
