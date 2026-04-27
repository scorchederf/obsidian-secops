---
atomic_guid: "95b25212-91a7-42ff-9613-124aca6845a8"
title: "Windows Powershell Logging Disabled"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "95b25212-91a7-42ff-9613-124aca6845a8"
  - "Windows Powershell Logging Disabled"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Modify the registry of the currently logged in user using reg.exe via cmd console to disable Powershell Module Logging, Script Block Logging, Transcription and Script Execution
see https://admx.help/?Category=Windows_10_2016&Policy=Microsoft.Policies.PowerShell::EnableModuleLogging

## ATT&CK Mapping

- [[kb/attack/techniques/T1112-modify_registry|T1112: Modify Registry]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
reg  add HKCU\Software\Policies\Microsoft\Windows\PowerShell\ModuleLogging /v EnableModuleLogging /t REG_DWORD /d 0 /f
reg  add HKCU\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging /v EnableScriptBlockLogging /t REG_DWORD /d 0 /f
reg  add HKCU\Software\Policies\Microsoft\Windows\PowerShell\Transcription /v EnableTranscripting /t REG_DWORD /d 0 /f
reg  add HKCU\Software\Policies\Microsoft\Windows\PowerShell /v EnableScripts /t REG_DWORD /d 0 /f
reg delete HKCU\Software\Policies\Microsoft\Windows\PowerShell /v EnableScripts /f >nul 2>&1
```

### Cleanup

```cmd
reg delete HKCU\Software\Policies\Microsoft\Windows\PowerShell\ModuleLogging /v EnableModuleLogging /f >nul 2>&1
reg delete HKCU\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging /v EnableScriptBlockLogging /f >nul 2>&1
reg delete HKCU\Software\Policies\Microsoft\Windows\PowerShell\Transcription /v EnableTranscripting /f >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
