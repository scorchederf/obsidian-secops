---
atomic_guid: "86677d0e-0b5e-4a2b-b302-454175f9aa9e"
title: "Allow RDP Remote Assistance Feature"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "86677d0e-0b5e-4a2b-b302-454175f9aa9e"
  - "Allow RDP Remote Assistance Feature"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Allow RDP Remote Assistance Feature

Modify the registry of the currently logged in user using reg.exe via cmd console to allow rdp remote assistance feature. This feature allow specific
user to rdp connect on the targeted machine.
See how azorult malware abuses this technique- https://app.any.run/tasks/a6f2ffe2-e6e2-4396-ae2e-04ea0143f2d8/

## Metadata

- Atomic GUID: 86677d0e-0b5e-4a2b-b302-454175f9aa9e
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

```cmd
reg add "HKLM\System\CurrentControlSet\Control\Terminal Server" /v fAllowToGetHelp /t REG_DWORD /d 1 /f
```

### Cleanup

```cmd
reg delete "HKLM\System\CurrentControlSet\Control\Terminal Server" /v fAllowToGetHelp /f >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
