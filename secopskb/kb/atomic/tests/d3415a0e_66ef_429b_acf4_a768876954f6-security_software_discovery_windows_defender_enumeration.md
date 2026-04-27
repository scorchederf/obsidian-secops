---
atomic_guid: "d3415a0e-66ef-429b-acf4-a768876954f6"
title: "Security Software Discovery - Windows Defender Enumeration"
framework: "atomic"
generated: "true"
attack_technique_id: "T1518.001"
attack_technique_name: "Software Discovery: Security Software Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1518.001/T1518.001.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "d3415a0e-66ef-429b-acf4-a768876954f6"
  - "Security Software Discovery - Windows Defender Enumeration"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Windows Defender Enumeration via different built-in windows native tools.
when sucessfully executed, information about windows defender is displayed.

## ATT&CK Mapping

- [[kb/attack/techniques/T1518-software_discovery#^t1518001-security-software-discovery|T1518.001: Security Software Discovery]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Get-Service WinDefend #check the service state of Windows Defender
Get-MpComputerStatus #provides the current status of security solution elements, including Anti-Spyware, Antivirus, LoavProtection, Real-time protection, etc
Get-MpThreat #threats details that have been detected using MS Defender
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1518.001/T1518.001.yaml)
