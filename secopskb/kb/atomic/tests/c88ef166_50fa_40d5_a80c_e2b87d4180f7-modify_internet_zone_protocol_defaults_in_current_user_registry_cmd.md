---
atomic_guid: "c88ef166-50fa-40d5-a80c-e2b87d4180f7"
title: "Modify Internet Zone Protocol Defaults in Current User Registry - cmd"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "c88ef166-50fa-40d5-a80c-e2b87d4180f7"
  - "Modify Internet Zone Protocol Defaults in Current User Registry - cmd"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test simulates an adversary modifying the Internet Zone Protocol Defaults in the registry of the currently logged-in user using the reg.exe utility via the command prompt. Such modifications can be indicative of an adversary trying to weaken browser security settings. Upon execution, if successful, the message "The operation completed successfully." will be displayed.
To verify the effects of the test:
1. Open the Registry Editor (regedit.exe).
2. Navigate to "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\ProtocolDefaults".
3. Check for the presence of the "http" and "https" DWORD values set to `0`.
Or run:
```batch
reg query "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\ProtocolDefaults"
```

## ATT&CK Mapping

- [[kb/attack/techniques/T1112-modify_registry|T1112: Modify Registry]]

## Executor

- name: command_prompt

### Command

```cmd
reg add "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\ProtocolDefaults" /v http /t REG_DWORD /d 0 /F
reg add "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\ProtocolDefaults" /v https /t REG_DWORD /d 0 /F
```

### Cleanup

```cmd
reg add "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\ProtocolDefaults" /v http /t REG_DWORD /d 3 /F
reg add "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\ProtocolDefaults" /v https /t REG_DWORD /d 3 /F
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
