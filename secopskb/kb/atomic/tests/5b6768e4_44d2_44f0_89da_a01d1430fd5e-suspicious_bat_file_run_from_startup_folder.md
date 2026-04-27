---
atomic_guid: "5b6768e4-44d2-44f0-89da-a01d1430fd5e"
title: "Suspicious bat file run from startup Folder"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.001"
attack_technique_name: "Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.001/T1547.001.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "5b6768e4-44d2-44f0-89da-a01d1430fd5e"
  - "Suspicious bat file run from startup Folder"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

bat files can be placed in and executed from the startup folder to maintain persistance

Upon execution, cmd will be run and immediately closed. Additionally, the new files can be viewed in the "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup"
folder and will also run when the computer is restarted and the user logs in.

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution#^t1547001-registry-run-keys---startup-folder|T1547.001: Registry Run Keys / Startup Folder]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Copy-Item "$PathToAtomicsFolder\T1547.001\src\batstartup.bat" "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\batstartup.bat"
Copy-Item "$PathToAtomicsFolder\T1547.001\src\batstartup.bat" "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\batstartup.bat"
Start-Process "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\batstartup.bat"
Start-Process "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\batstartup.bat"
```

### Cleanup

```powershell
Remove-Item "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\batstartup.bat" -ErrorAction Ignore
Remove-Item "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\batstartup.bat" -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.001/T1547.001.yaml)
