---
atomic_guid: "24fd9719-7419-42dd-bce6-ab3463110b3c"
title: "Mirror Blast Emulation"
framework: "atomic"
generated: "true"
attack_technique_id: "T1204.002"
attack_technique_name: "User Execution: Malicious File"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1204.002/T1204.002.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "24fd9719-7419-42dd-bce6-ab3463110b3c"
  - "Mirror Blast Emulation"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Mirror Blast Emulation

Emulates the JS -> MSI chain of the MirrorBlast T505 campaign by executing an xlsm file designed.
Requires the 32 bit version of Office to run. [MirrorBlast Campaign Analysis](https://blog.morphisec.com/explosive-new-mirrorblast-campaign-targets-financial-companies)

## Metadata

- Atomic GUID: 24fd9719-7419-42dd-bce6-ab3463110b3c
- Technique: T1204.002: User Execution: Malicious File
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1204.002/T1204.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1204-user_execution|T1204.002]]

## Executor

- name: powershell

### Command

```powershell
Cd "C:\ProgramData\Microsoft\Windows\Start Menu\Programs"
New-ItemProperty -Path Registry::HKEY_CURRENT_USER\SOFTWARE\Microsoft\Office\16.0\Excel\Security -Name "VBAWarnings" -Value "1" -PropertyType DWORD -Force | Out-Null
& '.\Excel 2016.lnk' "PathToAtomicsFolder\T1204.002\bin\mirrorblast_emulation.xlsm"
```

### Cleanup

```powershell
reg delete "HKCU\SOFTWARE\Microsoft\Office\16.0\Excel\Security" /v "VBAWarnings" /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1204.002/T1204.002.yaml)
