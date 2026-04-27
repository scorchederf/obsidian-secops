---
car_id: "CAR-2016-04-005"
title: "Remote Desktop Logon"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2016-04-005/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2016-04-005.yaml"
build_date: "2026-04-27 19:03:49"
aliases:
  - "CAR-2016-04-005"
  - "Remote Desktop Logon"
attack_technique_ids:
  - "T1021"
  - "T1021.001"
platforms:
  - "Windows"
implementation_types:
  - "pseudocode"
  - "Sigma"
  - "LogPoint"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

A remote desktop logon, through [RDP](https://attack.mitre.org/techniques/T1021/001), may be typical of a system administrator or IT support, but only from select workstations. Monitoring remote desktop logons and comparing to known/approved originating systems can detect lateral movement of an adversary.

## ATT&CK Coverage

- [[kb/attack/techniques/T1021-remote_services|T1021: Remote Services]] (coverage: Moderate; tactics: TA0008)
  - [[kb/attack/techniques/T1021-remote_services#^t1021001-remote-desktop-protocol|T1021.001: Remote Desktop Protocol]]

## Implementations

### pseudocode

Look in the system logs for remote logons using RDP.

```pseudocode
[EventCode] == 4624 and
[AuthenticationPackageName] == 'Negotiate' and
[Severity] == "Information" and
[LogonType] == 10
```

### Sigma

[Sigma version](https://github.com/Neo23x0/sigma/blob/master/rules/windows/builtin/win_admin_rdp_login.yml) of the above pseudocode, with some modifications.

### LogPoint

LogPoint version of the above pseudocode.

- Data Model: LogPoint native

```logpoint
norm_id=WinServer event_id=4624 package="Negotiate" log_level="INFO" logon_type=10
```

## D3FEND Mappings

- [[kb/defend/techniques/D3-RTSD-remote_terminal_session_detection|D3-RTSD: Remote Terminal Session Detection]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2016-04-005/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2016-04-005.yaml)
