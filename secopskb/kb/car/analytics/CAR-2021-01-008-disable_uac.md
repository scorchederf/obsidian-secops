---
car_id: "CAR-2021-01-008"
title: "Disable UAC"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2021-01-008/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-01-008.yaml"
build_date: "2026-04-27 19:03:49"
aliases:
  - "CAR-2021-01-008"
  - "Disable UAC"
attack_technique_ids:
  - "T1548"
  - "T1548.002"
platforms:
  - "Windows"
implementation_types:
  - "Splunk"
  - "pseudocode"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Threat actors often, after compromising a machine, try to disable User Access Control (UAC) to escalate privileges. This is often done by changing the registry key for system policies using “reg.exe”, a legitimate tool provided by Microsoft for modifying the registry via command prompt or scripts. This action interferes with UAC and may enable a threat actor to escalate privileges on the compromised system, thereby allowing further exploitation of the system.

## ATT&CK Coverage

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548: Abuse Elevation Control Mechanism]] (coverage: Medium; tactics: TA0004)
  - [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism#^t1548002-bypass-user-account-control|T1548.002: Bypass User Account Control]]

## Implementations

### Splunk

This query looks for the specific use of reg.exe in correlation to commands aimed at disabling UAC.

- Data Model: Sysmon native

```splunk
sourcetype = __your_sysmon_index__ ParentImage = "C:\\Windows\\System32\\cmd.exe" | where like(CommandLine,"reg.exe%HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System%REG_DWORD /d 0%")
```

### pseudocode

This query looks for the specific use of reg.exe in correlation to commands aimed at disabling UAC.

- Data Model: Sysmon native

```pseudocode
processes = search Process:Create
cmd_processes = filter processes where (
                (parent_image = "C:\\Windows\\System32\\cmd.exe") AND (command_line = "reg.exe%HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System%REG_DWORD /d 0%")
                )
```

## Data Model References

- process/create/image_path
- process/create/command_line

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2021-01-008/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-01-008.yaml)
