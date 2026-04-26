---
car_id: "CAR-2020-11-009"
title: "Compiled HTML Access"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2020-11-009/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2020-11-009.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2020-11-009"
  - "Compiled HTML Access"
attack_technique_ids:
  - "T1218"
  - "T1218.001"
platforms:
  - "Windows"
implementation_types:
  - "Pseudocode"
  - "Splunk"
  - "LogPoint"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

# CAR-2020-11-009: Compiled HTML Access

## Metadata

- CAR ID: CAR-2020-11-009
- Submission Date: 2020/11/30
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: Olaf Hartong

## Description

Adversaries may hide malicious code in .chm compiled HTML files. When these files are read, Windows uses the HTML help executable named hh.exe, which is the signature for this analytic.

## ATT&CK Coverage

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]] (coverage: High; tactics: TA0005)
  - [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.001]]

## Implementations

### Pseudocode

This is a pseudocode representation of the below splunk search.

- Data Model: CAR native

```pseudocode
processes = search Process:Create
target_processes = filter processes where (exe="C:\Windows\syswow64\hh.exe" OR exe="C:\Windows\system32\hh.exe")
output target_processes
```

### Splunk

looks all instances of hh.exe

- Data Model: Sysmon native

```splunk
(index=__your_sysmon_index__ EventCode=1) (Image="C:\\Windows\\syswow64\\hh.exe" OR Image="C:\\Windows\\system32\\hh.exe")
```

### LogPoint

looks all instances of hh.exe

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon event_id=1 (image="C:\Windows\syswow64\hh.exe" OR image="C:\Windows\system32\hh.exe")
```

## Data Model References

- process/create/exe

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2020-11-009/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2020-11-009.yaml)
