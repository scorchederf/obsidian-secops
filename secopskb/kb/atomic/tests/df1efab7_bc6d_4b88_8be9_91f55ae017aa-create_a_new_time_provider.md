---
atomic_guid: "df1efab7-bc6d-4b88-8be9-91f55ae017aa"
title: "Create a new time provider"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.003"
attack_technique_name: "Time Providers"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.003/T1547.003.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "df1efab7-bc6d-4b88-8be9-91f55ae017aa"
  - "Create a new time provider"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Create a new time provider

Establishes persistence by creating a new time provider registry key under HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\TimeProvider.
The new time provider will point to a DLL which will be loaded after the w32time service is started. The DLL will then create the file AtomicTest.txt
in C:\Users\Public\ as validation that the test is successful.

Payload source code: https://github.com/tr4cefl0w/payloads/tree/master/T1547.003/

## Metadata

- Atomic GUID: df1efab7-bc6d-4b88-8be9-91f55ae017aa
- Technique: T1547.003: Time Providers
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1547.003/T1547.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.003]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
net stop w32time
Copy-Item "$PathToAtomicsFolder\T1547.003\bin\AtomicTest.dll" C:\Users\Public\AtomicTest.dll
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\TimeProviders\AtomicTest" /t REG_SZ /v "DllName" /d "C:\Users\Public\AtomicTest.dll" /f
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\TimeProviders\AtomicTest" /t REG_DWORD /v "Enabled" /d "1" /f
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\TimeProviders\AtomicTest" /t REG_DWORD /v "InputProvider" /d "1" /f
net start w32time
```

### Cleanup

```powershell
net stop w32time
reg delete "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\TimeProviders\AtomicTest" /f
rm -force C:\Users\Public\AtomicTest.dll
net start w32time
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.003/T1547.003.yaml)
