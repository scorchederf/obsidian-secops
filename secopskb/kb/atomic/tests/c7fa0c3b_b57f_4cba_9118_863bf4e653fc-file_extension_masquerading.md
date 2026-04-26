---
atomic_guid: "c7fa0c3b-b57f-4cba-9118-863bf4e653fc"
title: "File Extension Masquerading"
framework: "atomic"
generated: "true"
attack_technique_id: "T1036.007"
attack_technique_name: "Masquerading: Double File Extension"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036.007/T1036.007.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "c7fa0c3b-b57f-4cba-9118-863bf4e653fc"
  - "File Extension Masquerading"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# File Extension Masquerading

download and execute a file masquerading as images or Office files. Upon execution 3 calc instances and 3 vbs windows will be launched.

e.g SOME_LEGIT_NAME.[doc,docx,xls,xlsx,pdf,rtf,png,jpg,etc.].[exe,vbs,js,ps1,etc] (Quartelyreport.docx.exe)

## Metadata

- Atomic GUID: c7fa0c3b-b57f-4cba-9118-863bf4e653fc
- Technique: T1036.007: Masquerading: Double File Extension
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1036.007/T1036.007.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1036-masquerading|T1036.007]]

## Input Arguments

### exe_path

- description: path to exe to use when creating masquerading files
- type: path
- default: C:\Windows\System32\calc.exe

### ps1_path

- description: path of powershell script to use when creating masquerading files
- type: path
- default: PathToAtomicsFolder\T1036.007\src\T1036.007_masquerading.ps1

### vbs_path

- description: path of vbs to use when creating masquerading files
- type: path
- default: PathToAtomicsFolder\T1036.007\src\T1036.007_masquerading.vbs

## Dependencies

File to copy must exist on disk at specified location (#{vbs_path})

### Prerequisite Check

```powershell
if (Test-Path "#{vbs_path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{vbs_path}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1036.007/src/T1036.007_masquerading.vbs" -OutFile "#{vbs_path}"
```

File to copy must exist on disk at specified location (#{ps1_path})

### Prerequisite Check

```powershell
if (Test-Path "#{ps1_path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{ps1_path}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1036.007/src/T1036.007_masquerading.ps1" -OutFile "#{ps1_path}"
```

## Executor

- name: command_prompt

### Command

```cmd
copy "#{exe_path}" %temp%\T1036.007_masquerading.docx.exe /Y
copy "#{exe_path}" %temp%\T1036.007_masquerading.pdf.exe /Y
copy "#{exe_path}" %temp%\T1036.007_masquerading.ps1.exe /Y
copy "#{vbs_path}" %temp%\T1036.007_masquerading.xls.vbs /Y
copy "#{vbs_path}" %temp%\T1036.007_masquerading.xlsx.vbs /Y
copy "#{vbs_path}" %temp%\T1036.007_masquerading.png.vbs /Y
copy "#{ps1_path}" %temp%\T1036.007_masquerading.doc.ps1 /Y
copy "#{ps1_path}" %temp%\T1036.007_masquerading.pdf.ps1 /Y
copy "#{ps1_path}" %temp%\T1036.007_masquerading.rtf.ps1 /Y
%temp%\T1036.007_masquerading.docx.exe
%temp%\T1036.007_masquerading.pdf.exe
%temp%\T1036.007_masquerading.ps1.exe
%temp%\T1036.007_masquerading.xls.vbs
%temp%\T1036.007_masquerading.xlsx.vbs
%temp%\T1036.007_masquerading.png.vbs
C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -File %temp%\T1036.007_masquerading.doc.ps1
C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -File %temp%\T1036.007_masquerading.pdf.ps1
C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -File %temp%\T1036.007_masquerading.rtf.ps1
```

### Cleanup

```cmd
del /f %temp%\T1036.007_masquerading.docx.exe > nul 2>&1
del /f %temp%\T1036.007_masquerading.pdf.exe > nul 2>&1
del /f %temp%\T1036.007_masquerading.ps1.exe > nul 2>&1
del /f %temp%\T1036.007_masquerading.xls.vbs > nul 2>&1
del /f %temp%\T1036.007_masquerading.xlsx.vbs > nul 2>&1
del /f %temp%\T1036.007_masquerading.png.vbs > nul 2>&1
del /f %temp%\T1036.007_masquerading.doc.ps1 > nul 2>&1
del /f %temp%\T1036.007_masquerading.pdf.ps1 > nul 2>&1
del /f %temp%\T1036.007_masquerading.rtf.ps1 > nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036.007/T1036.007.yaml)
