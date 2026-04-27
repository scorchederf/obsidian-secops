---
car_id: "CAR-2020-09-005"
title: "AppInit DLLs"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2020-09-005/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2020-09-005.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2020-09-005"
  - "AppInit DLLs"
attack_technique_ids:
  - "T1546"
  - "T1546.010"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# CAR-2020-09-005: AppInit DLLs

## Metadata

- CAR ID: CAR-2020-09-005
- Submission Date: 2020/09/10
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Registry
- Contributors: Olaf Hartong

## Description

Adversaries may establish persistence and/or elevate privileges by executing malicious content triggered by AppInit DLLs loaded into processes. Dynamic-link libraries (DLLs) that are specified in the AppInit_DLLs value in the Registry keys `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Windows` or `HKEY_LOCAL_MACHINE\Software\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Windows` are loaded by user32.dll into every process that loads user32.dll. These values can be abused to obtain elevated privileges by causing a malicious DLL to be loaded and run in the context of separate processes. Accordingly, this analytic looks for modifications to these registry keys that may be indicative of this type of abuse.

## ATT&CK Coverage

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546]] (coverage: Moderate; tactics: TA0003, TA0004)
  - [[kb/attack/techniques/T1546-event_triggered_execution|T1546.010]]

## Implementations

### Pseudocode

This is a pseudocode representation of the below splunk search.

- Data Model: CAR native

```pseudocode
registry_keys = search (Registry:Create AND Registry:Remove AND Registry:Edit)
appinit_keys = filter registry_keys where (
  key = "*\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows\Appinit_Dlls\*" OR
  key = "*\SOFTWARE\\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Windows\Appinit_Dlls\*""
  )
output clsid_keys
```

### Splunk

This Splunk search looks for any registry keys that were created, deleted, or renamed, as well as any registry values that were set or renamed under the Windows AppInit DLL registry keys.

- Data Model: Sysmon native

```splunk
index=__your_sysmon_index__ (EventCode=12 OR EventCode=13 OR EventCode=14) (TargetObject="*\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Windows\\Appinit_Dlls\\*" OR TargetObject="*\\SOFTWARE\\Wow6432Node\\Microsoft\\Windows NT\\CurrentVersion\\Windows\\Appinit_Dlls\\*")
```

### LogPoint

This LogPoint search looks for any registry keys that were created, deleted, or renamed, as well as any registry values that were set or renamed under the Windows AppInit DLL registry keys.

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon event_id IN [12, 13, 14] target_object IN ["*\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows\Appinit_Dlls\*", "*\SOFTWARE\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Windows\Appinit_Dlls\*"]
```

## Data Model References

- registry/add/key
- registry/remove/key
- registry/edit/key

## D3FEND Mappings

- [[kb/defend/techniques/D3-SICA-system_init_config_analysis|D3-SICA: System Init Config Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2020-09-005/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2020-09-005.yaml)
