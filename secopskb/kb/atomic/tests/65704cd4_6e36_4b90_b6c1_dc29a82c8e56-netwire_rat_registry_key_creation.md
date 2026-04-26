---
atomic_guid: "65704cd4-6e36-4b90-b6c1-dc29a82c8e56"
title: "NetWire RAT Registry Key Creation"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "65704cd4-6e36-4b90-b6c1-dc29a82c8e56"
  - "NetWire RAT Registry Key Creation"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# NetWire RAT Registry Key Creation

NetWire continues to create its home key (HKCU\SOFTWARE\NetWire) as well as adding it into the auto-run group in the victim’s registry.
See how NetWire malware - https://app.any.run/tasks/41ecdbde-4997-4301-a350-0270448b4c8f/

## Metadata

- Atomic GUID: 65704cd4-6e36-4b90-b6c1-dc29a82c8e56
- Technique: T1112: Modify Registry
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1112/T1112.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Executor

- name: command_prompt

### Command

```commandprompt
reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v NetWire /t REG_SZ  /d "C:\Users\admin\AppData\Roaming\Install\Host.exe" /f
reg add HKCU\SOFTWARE\NetWire /v HostId /t REG_SZ /d HostId-kai6Ci /f
reg add HKCU\SOFTWARE\NetWire /v "Install Date" /t REG_SZ /d "2021-08-30 07:17:27" /f
```

### Cleanup

```commandprompt
reg delete HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v NetWire /f >nul 2>&1
reg delete HKCU\SOFTWARE\NetWire /va /f >nul 2>&1
reg delete HKCU\SOFTWARE\NetWire /f >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
