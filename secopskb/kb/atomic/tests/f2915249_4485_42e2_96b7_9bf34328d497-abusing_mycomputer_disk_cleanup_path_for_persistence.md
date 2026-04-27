---
atomic_guid: "f2915249-4485-42e2-96b7-9bf34328d497"
title: "Abusing MyComputer Disk Cleanup Path for Persistence"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "f2915249-4485-42e2-96b7-9bf34328d497"
  - "Abusing MyComputer Disk Cleanup Path for Persistence"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Replacing the registry settings with custom executable will end up with the replacement programs being executed at the time OS will decide to kick off the respective activity

## ATT&CK Mapping

- [[kb/attack/techniques/T1112-modify_registry|T1112: Modify Registry]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\cleanuppath" /t REG_EXPAND_SZ /d "%systemroot%\system32\notepad.exe" /f
```

### Cleanup

```cmd
reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\cleanuppath" /t REG_EXPAND_SZ /d "%SystemRoot%\System32\cleanmgr.exe /D %c" /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
