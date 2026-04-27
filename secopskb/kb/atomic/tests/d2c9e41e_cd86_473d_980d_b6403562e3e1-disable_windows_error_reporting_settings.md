---
atomic_guid: "d2c9e41e-cd86-473d-980d-b6403562e3e1"
title: "Disable Windows Error Reporting Settings"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "d2c9e41e-cd86-473d-980d-b6403562e3e1"
  - "Disable Windows Error Reporting Settings"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Modify the registry of the currently logged in user using reg.exe via cmd console to disable windows error reporting settings. This Windows feature allow the use to report bug, errors, failure or problems 
encounter in specific application or process.
See how azorult malware abuses this technique- https://app.any.run/tasks/a6f2ffe2-e6e2-4396-ae2e-04ea0143f2d8/

## ATT&CK Mapping

- [[kb/attack/techniques/T1112-modify_registry|T1112: Modify Registry]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
reg add HKLM64\SOFTWARE\Policies\Microsoft\Windows Defender\Reporting /v DisableEnhancedNotifications /t REG_DWORD /d 1 /f
reg add HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\Reporting /v DisableEnhancedNotifications /t REG_DWORD /d 1 /f
```

### Cleanup

```cmd
reg delete HKLM64\SOFTWARE\Policies\Microsoft\Windows Defender\Reporting /v DisableEnhancedNotifications /f >nul 2>&1
reg delete HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\Reporting /v DisableEnhancedNotifications /f >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
