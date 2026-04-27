---
car_id: "CAR-2016-04-003"
title: "User Activity from Stopping Windows Defensive Services"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2016-04-003/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2016-04-003.yaml"
build_date: "2026-04-27 19:03:49"
aliases:
  - "CAR-2016-04-003"
  - "User Activity from Stopping Windows Defensive Services"
attack_technique_ids:
  - "T1562"
  - "T1562.001"
platforms:
  - "Windows"
implementation_types:
  - "pseudocode"
  - "LogPoint"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Spyware and malware remain a serious problem and Microsoft developed security services, Windows Defender and Windows Firewall, to combat this threat. In the event Windows Defender or Windows Firewall is turned off, administrators should correct the issue immediately to prevent the possibility of infection or further infection and investigate to determine if caused by crash or user manipulation.

Stopping services events are Windows Event Code 7036.

## ATT&CK Coverage

- [[kb/attack/techniques/T1562-impair_defenses|T1562: Impair Defenses]] (coverage: Low; tactics: TA0005)
  - [[kb/attack/techniques/T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]

## Implementations

### pseudocode

Windows Event code 7036 from the System log identifies if a service has stopped or started. This analytic looks for "Windows Defender" or "Windows Firewall" that has stopped.

```pseudocode
log_name == "System" AND
event_code == "7036"
param1 in ["Windows Defender", "Windows Firewall"] AND
param2 == "stopped"
```

### LogPoint

LogPoint version of the above pseudocode.

- Data Model: LogPoint native

```logpoint
norm_id=WinServer channel="System" event_id=7036 param1 in ["Windows Defender", "Windows Firewall"] param2="stopped"
```

## Unit Tests

From an administrative user powershell console, run the Stop-Service command.

- Configurations: Windows 7

```text
Stop-Service -displayname "Windows Firewall"
Stop-Service -displayname "Windows Defender"
```

## D3FEND Mappings

- [[kb/defend/techniques/D3-SDM-system_daemon_monitoring|D3-SDM: System Daemon Monitoring]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2016-04-003/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2016-04-003.yaml)
