---
atomic_guid: "befc2b40-d487-4a5a-8813-c11085fb5672"
title: "Modify BootExecute Value"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.001"
attack_technique_name: "Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.001/T1547.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "befc2b40-d487-4a5a-8813-c11085fb5672"
  - "Modify BootExecute Value"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Modify BootExecute Value

This test modifies the BootExecute registry value to "autocheck autoche *", which can be used to simulate an adversary's attempt to tamper with the system's boot process. 
Reference - https://www.welivesecurity.com/wp-content/uploads/2018/09/ESET-LoJax.pdf
NOTE that by not saving the correct value, you may inhibit your system from booting properly. Only run on a test system. There is a reg export before running the Atomic.

## Metadata

- Atomic GUID: befc2b40-d487-4a5a-8813-c11085fb5672
- Technique: T1547.001: Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1547.001/T1547.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.001]]

## Input Arguments

### registry_value

- description: Registry value to set
- type: string
- default: autocheck autoche *

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
if (!(Test-Path "$PathToAtomicsFolder\T1547.001\src\SessionManagerBackup.reg")) { reg.exe export "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager" "$PathToAtomicsFolder\T1547.001\src\SessionManagerBackup.reg" /y }
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager" -Name "BootExecute" -Value "#{registry_value}" -Type MultiString
```

### Cleanup

```powershell
reg.exe import "$PathToAtomicsFolder\T1547.001\src\SessionManagerBackup.reg"
Remove-Item -Path "$PathToAtomicsFolder\T1547.001\src\SessionManagerBackup.reg" -Force
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.001/T1547.001.yaml)
