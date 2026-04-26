---
atomic_guid: "69fc085b-5444-4879-8002-b24c8e1a3e02"
title: "LockBit Black - Disable the ETW Provider of Windows Defender -Powershell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.006"
attack_technique_name: "Impair Defenses: Indicator Blocking"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.006/T1562.006.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "69fc085b-5444-4879-8002-b24c8e1a3e02"
  - "LockBit Black - Disable the ETW Provider of Windows Defender -Powershell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# LockBit Black - Disable the ETW Provider of Windows Defender -Powershell

An adversary can disable the ETW Provider of Windows Defender,
so nothing would be logged to Microsoft-Windows-Windows-Defender/Operational anymore.
https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-075a

## Metadata

- Atomic GUID: 69fc085b-5444-4879-8002-b24c8e1a3e02
- Technique: T1562.006: Impair Defenses: Indicator Blocking
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1562.006/T1562.006.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.006]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
New-ItemProperty "HKLM:\Software\Microsoft\Windows\CurrentVersion\WINEVT\Channels\Microsoft-Windows-Windows Defender/Operational" -Name Enabled  -PropertyType DWord -Value 0 -Force
```

### Cleanup

```powershell
Remove-ItemProperty "HKLM:\Software\Microsoft\Windows\CurrentVersion\WINEVT\Channels\Microsoft-Windows-Windows Defender/Operational" -Name Enabled -Force -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.006/T1562.006.yaml)
