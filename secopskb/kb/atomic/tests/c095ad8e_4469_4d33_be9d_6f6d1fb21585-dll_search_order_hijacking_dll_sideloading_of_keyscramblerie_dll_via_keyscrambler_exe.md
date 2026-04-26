---
atomic_guid: "c095ad8e-4469-4d33-be9d-6f6d1fb21585"
title: "DLL Search Order Hijacking,DLL Sideloading Of KeyScramblerIE.DLL Via KeyScrambler.EXE"
framework: "atomic"
generated: "true"
attack_technique_id: "T1574.001"
attack_technique_name: "Hijack Execution Flow: DLL"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1574.001/T1574.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "c095ad8e-4469-4d33-be9d-6f6d1fb21585"
  - "DLL Search Order Hijacking,DLL Sideloading Of KeyScramblerIE.DLL Via KeyScrambler.EXE"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# DLL Search Order Hijacking,DLL Sideloading Of KeyScramblerIE.DLL Via KeyScrambler.EXE

Various threat actors and malware have been found side loading a masqueraded "KeyScramblerIE.dll" through "KeyScrambler.exe", which can load further executables embedded in modified KeyScramblerIE.dll file.

## Metadata

- Atomic GUID: c095ad8e-4469-4d33-be9d-6f6d1fb21585
- Technique: T1574.001: Hijack Execution Flow: DLL
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1574.001/T1574.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Write-Host 1.Downloading KeyScrambler from official website to temp directory
Invoke-WebRequest -Uri "https://download.qfxsoftware.com/download/latest/KeyScrambler_Setup.exe" -OutFile $env:Temp\KeyScrambler_Setup.exe
Write-Host 2.Installing KeyScrambler with KeyScrambler_Setup.exe from temp directory
Start-Process -FilePath $env:Temp\KeyScrambler_Setup.exe -ArgumentList /S -Wait
Write-Host 3.Copying KeyScrambler.exe to temp folder,to avoid permission issues, which calls KeyScramblerIE.dll in CWD i.e. temp
Copy-Item "C:\Program Files (x86)\KeyScrambler\KeyScrambler.exe" -Destination $env:TEMP\KeyScrambler.exe
Write-Host 4.Executing KeyScrambler.exe, you should see a popup of missing KeyScramblerIE.dll, you can close this popup
Start-Process -FilePath $env:Temp\KeyScrambler.exe
Write-Host 5.A modified KeyScramblerIE.dll can be copied to temp, which can be misused by Attacker
```

### Cleanup

```powershell
Write-Host 1.Kindly close the popup window asking for KeyScramblerIE.dll ,so that it gets deleted.

Remove-Item -Path $env:Temp\KeyScrambler_Setup.exe
Start-Process -FilePath "C:\Program Files (x86)\KeyScrambler\Uninstall.exe" -ArgumentList /S -Wait
Remove-Item -Path $env:Temp\KeyScrambler.exe
Write-Host 2.KeyScrambler cleanup completed successfully.
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1574.001/T1574.001.yaml)
