---
atomic_guid: "795d3248-0394-4d4d-8e86-4e8df2a2693f"
title: "Windows Modify Show Compress Color And Info Tip Registry"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "795d3248-0394-4d4d-8e86-4e8df2a2693f"
  - "Windows Modify Show Compress Color And Info Tip Registry"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Modify the registry of the currently logged in user using reg.exe via cmd console to show compress color and show tips feature. 
See how hermeticwiper uses this technique - https://www.splunk.com/en_us/blog/security/detecting-hermeticwiper.html

## ATT&CK Mapping

- [[kb/attack/techniques/T1112-modify_registry|T1112: Modify Registry]]

## Executor

- name: command_prompt

### Command

```cmd
reg  add HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced /v ShowInfoTip /t REG_DWORD /d 0 /f
reg  add HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced /v ShowCompColor /t REG_DWORD /d 0 /f
```

### Cleanup

```cmd
reg delete HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced /v ShowInfoTip /f >nul 2>&1
reg delete HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced /v ShowCompColor /f >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
