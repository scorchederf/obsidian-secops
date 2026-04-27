---
car_id: "CAR-2014-11-004"
title: "Remote PowerShell Sessions"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2014-11-004/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2014-11-004.yaml"
build_date: "2026-04-27 19:03:49"
aliases:
  - "CAR-2014-11-004"
  - "Remote PowerShell Sessions"
attack_technique_ids:
  - "T1059"
  - "T1059.001"
  - "T1021"
  - "T1021.006"
platforms:
  - "Windows"
implementation_types:
  - "pseudocode"
  - "EQL"
  - "LogPoint"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

According to [ATT&CK](https://attack.mitre.org/), [PowerShell](https://attack.mitre.org/techniques/T1059/001) can be used over WinRM to remotely run commands on a host. When a remote PowerShell session starts, svchost.exe executes wsmprovhost.exe

For this to work, certain registry keys must be set, and the WinRM service must be enabled. The PowerShell command `Enter-PSSession -ComputerName \<RemoteHost\>` creates a remote PowerShell session.

## ATT&CK Coverage

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]] (coverage: Moderate; tactics: TA0002)
  - [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]
- [[kb/attack/techniques/T1021-remote_services|T1021: Remote Services]] (coverage: Moderate; tactics: TA0008)
  - [[kb/attack/techniques/T1021-remote_services#^t1021006-windows-remote-management|T1021.006: Windows Remote Management]]

## Implementations

### pseudocode

```pseudocode
process = search Process:Create
wsmprovhost = filter process where (exe == "wsmprovhost.exe" and parent_exe == "svchost.exe")
```

### EQL

EQL version of the above pseudocode.

- Data Model: EQL native

```eql
process where subtype.create and
  (process_name == "wsmprovhost.exe" and parent_process_name == "svchost.exe")
```

### LogPoint

LogPoint version of the above pseudocode.

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon event_id=1 image="*\wsmprovhost.exe" parent_image="*\svchost.exe"
```

## Data Model References

- process/create/exe
- process/create/parent_exe

## D3FEND Mappings

- [[kb/defend/techniques/D3-PLA-process_lineage_analysis|D3-PLA: Process Lineage Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2014-11-004/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2014-11-004.yaml)
