---
atomic_guid: "dade9447-791e-4c8f-b04b-3a35855dfa06"
title: "Suspicious jse file run from startup Folder"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.001"
attack_technique_name: "Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.001/T1547.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "dade9447-791e-4c8f-b04b-3a35855dfa06"
  - "Suspicious jse file run from startup Folder"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious jse file run from startup Folder

jse files can be placed in and ran from the startup folder to maintain persistance.
Upon execution, "T1547.001 Hello, World JSE!" will be displayed twice. 
Additionally, the new files can be viewed in the "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup"
folder and will also run when the computer is restarted and the user logs in.

## Metadata

- Atomic GUID: dade9447-791e-4c8f-b04b-3a35855dfa06
- Technique: T1547.001: Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1547.001/T1547.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.001]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Copy-Item "$PathToAtomicsFolder\T1547.001\src\jsestartup.jse" "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\jsestartup.jse"
Copy-Item "$PathToAtomicsFolder\T1547.001\src\jsestartup.jse" "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\jsestartup.jse"
cscript.exe /E:Jscript "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\jsestartup.jse"
cscript.exe /E:Jscript "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\jsestartup.jse"
```

### Cleanup

```powershell
Remove-Item "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\jsestartup.jse" -ErrorAction Ignore
Remove-Item "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\jsestartup.jse" -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.001/T1547.001.yaml)
