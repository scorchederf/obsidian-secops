---
atomic_guid: "9b6a06f9-ab5e-4e8d-8289-1df4289db02f"
title: "Registry key creation and/or modification events for SDB"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.011"
attack_technique_name: "Event Triggered Execution: Application Shimming"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.011/T1546.011.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "9b6a06f9-ab5e-4e8d-8289-1df4289db02f"
  - "Registry key creation and/or modification events for SDB"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Registry key creation and/or modification events for SDB

Create registry keys in locations where fin7 typically places SDB patches. Upon execution, output will be displayed describing
the registry keys that were created. These keys can also be viewed using the Registry Editor.

https://www.fireeye.com/blog/threat-research/2017/05/fin7-shim-databases-persistence.html

## Metadata

- Atomic GUID: 9b6a06f9-ab5e-4e8d-8289-1df4289db02f
- Technique: T1546.011: Event Triggered Execution: Application Shimming
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1546.011/T1546.011.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.011]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
New-ItemProperty -Path HKLM:"\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Custom" -Name "AtomicRedTeamT1546.011" -Value "AtomicRedTeamT1546.011"
New-ItemProperty -Path HKLM:"\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\InstalledSDB" -Name "AtomicRedTeamT1546.011" -Value "AtomicRedTeamT1546.011"
```

### Cleanup

```powershell
Remove-ItemProperty -Path HKLM:"\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Custom" -Name "AtomicRedTeamT1546.011" -ErrorAction Ignore
Remove-ItemProperty -Path HKLM:"\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\InstalledSDB" -Name "AtomicRedTeamT1546.011" -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.011/T1546.011.yaml)
