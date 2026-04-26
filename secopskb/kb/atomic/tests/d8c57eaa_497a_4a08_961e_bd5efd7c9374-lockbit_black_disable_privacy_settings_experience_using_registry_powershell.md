---
atomic_guid: "d8c57eaa-497a-4a08-961e-bd5efd7c9374"
title: "LockBit Black - Disable Privacy Settings Experience Using Registry -Powershell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "d8c57eaa-497a-4a08-961e-bd5efd7c9374"
  - "LockBit Black - Disable Privacy Settings Experience Using Registry -Powershell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# LockBit Black - Disable Privacy Settings Experience Using Registry -Powershell

LockBit Black - Disable Privacy Settings Experience Using Registry

## Metadata

- Atomic GUID: d8c57eaa-497a-4a08-961e-bd5efd7c9374
- Technique: T1562.001: Impair Defenses: Disable or Modify Tools
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1562.001/T1562.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
New-ItemProperty "HKCU:\Software\Policies\Microsoft\Windows\OOBE" -Name DisablePrivacyExperience -PropertyType DWord -Value 1 -Force
```

### Cleanup

```powershell
Remove-ItemProperty "HKCU:\Software\Policies\Microsoft\Windows\OOBE" -Name DisablePrivacyExperience -Force -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
