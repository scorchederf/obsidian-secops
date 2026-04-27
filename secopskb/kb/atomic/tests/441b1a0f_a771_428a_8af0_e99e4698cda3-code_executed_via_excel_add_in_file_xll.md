---
atomic_guid: "441b1a0f-a771-428a-8af0-e99e4698cda3"
title: "Code Executed Via Excel Add-in File (XLL)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1137.006"
attack_technique_name: "Office Application Startup: Add-ins"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1137.006/T1137.006.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "441b1a0f-a771-428a-8af0-e99e4698cda3"
  - "Code Executed Via Excel Add-in File (XLL)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Code Executed Via Excel Add-in File (XLL)

Loads an XLL file using the excel add-ins library.
This causes excel to launch Notepad.exe as a child process. This atomic test does not include persistent code execution as you would typically see when this is implemented in malware.

## Metadata

- Atomic GUID: 441b1a0f-a771-428a-8af0-e99e4698cda3
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
    $excelApp.RegisterXLL("PathToAtomicsFolder\T1137.006\bin\Addins\excelxll_x64.xll")
}
else{
  Write-Host "32-bit Office"
  $excelApp.RegisterXLL("PathToAtomicsFolder\T1137.006\bin\Addins\excelxll_x86.xll")
}
```

### Cleanup

```powershell
Stop-Process -Name "notepad","Excel" -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1137.006/T1137.006.yaml)
