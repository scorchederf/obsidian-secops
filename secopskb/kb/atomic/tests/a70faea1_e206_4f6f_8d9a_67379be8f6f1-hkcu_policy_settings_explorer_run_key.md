---
atomic_guid: "a70faea1-e206-4f6f-8d9a-67379be8f6f1"
title: "HKCU - Policy Settings Explorer Run Key"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.001"
attack_technique_name: "Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.001/T1547.001.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "a70faea1-e206-4f6f-8d9a-67379be8f6f1"
  - "HKCU - Policy Settings Explorer Run Key"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test will create a new value under HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run to launch calc.exe on boot. 
*Requires reboot

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution#^t1547001-registry-run-keys---startup-folder|T1547.001: Registry Run Keys / Startup Folder]]

## Input Arguments

### payload

- description: payload to execute
- type: string
- default: C:\Windows\System32\calc.exe

### target_key_value_name

- description: registry value to crate on target key
- type: string
- default: atomictest

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
if (!(Test-Path -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer")){
  New-Item -ItemType Key -Path  "HKCU:\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer"
}
if (!(Test-Path -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run")){
  New-Item -ItemType Key -Path  "HKCU:\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run"
}
Set-ItemProperty -Path  "HKCU:\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run" -Name "#{target_key_value_name}" -Value "#{payload}"
```

### Cleanup

```powershell
Remove-ItemProperty -Path  "HKCU:\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run" -Name "#{target_key_value_name}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.001/T1547.001.yaml)
