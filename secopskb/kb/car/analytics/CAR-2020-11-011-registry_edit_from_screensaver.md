---
car_id: "CAR-2020-11-011"
title: "Registry Edit from Screensaver"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2020-11-011/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2020-11-011.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2020-11-011"
  - "Registry Edit from Screensaver"
attack_technique_ids:
  - "T1546"
  - "T1546.002"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# CAR-2020-11-011: Registry Edit from Screensaver

## Metadata

- CAR ID: CAR-2020-11-011
- Submission Date: 2020/11/30
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: Olaf Hartong

## Description

Adversaries may use screensaver files to run malicious code. This analytic triggers on suspicious edits to the screensaver registry keys, which dictate which .scr file the screensaver runs.

## ATT&CK Coverage

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546]] (coverage: High; tactics: TA0003, TA0004)
  - [[kb/attack/techniques/T1546-event_triggered_execution|T1546.002]]

## Implementations

### Pseudocode

This is a pseudocode representation of the below splunk search.

- Data Model: CAR native

```pseudocode
reg_events = search Registry:add or Registry:edit
scr_reg_events = filter processes where (
  key="*\\Software\\Policies\\Microsoft\\Windows\\Control Panel\\Desktop\\SCRNSAVE.EXE" AND
output scr_reg_events
```

### Splunk

looks creations of edits of the SCRNSAVE.exe registry key

- Data Model: Sysmon native

```splunk
index=your_sysmon_index (EventCode=12 OR EventCode=13 OR EventCode=14) TargetObject="*\\Software\\Policies\\Microsoft\\Windows\\Control Panel\\Desktop\\SCRNSAVE.EXE"
```

### LogPoint

looks creations of edits of the SCRNSAVE.exe registry key

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon event_id IN [12, 13, 14] target_object="*\Software\Policies\Microsoft\Windows\Control Panel\Desktop\SCRNSAVE.EXE"
```

## Data Model References

- registry/edit/key
- registry/add/key

## D3FEND Mappings

- [[kb/defend/techniques/D3-USICA-user_session_init_config_analysis|D3-USICA: User Session Init Config Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2020-11-011/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2020-11-011.yaml)
