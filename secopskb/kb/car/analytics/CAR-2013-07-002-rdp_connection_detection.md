---
car_id: "CAR-2013-07-002"
title: "RDP Connection Detection"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2013-07-002/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-07-002.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2013-07-002"
  - "RDP Connection Detection"
attack_technique_ids:
  - "T1021"
  - "T1021.001"
implementation_types:
  - "pseudocode"
  - "Sigma"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# CAR-2013-07-002: RDP Connection Detection

## Metadata

- CAR ID: CAR-2013-07-002
- Submission Date: 2013/07/24
- Information Domain: Analytic, Network
- Analytic Type: Situational Awareness, TTP
- Platforms: 
- Data Subtypes: Map building, Anomaly, Hostflow
- Contributors: MITRE

## Description

The [Remote Desktop Protocol](https://attack.mitre.org/techniques/T1021/001) (RDP), built in to Microsoft operating systems, allows a user to remotely log in to the desktop of another host. It allows for interactive access of the running windows, and forwards key presses, mouse clicks, etc. Network administrators, power users, and end-users may use RDP for day-to-day operations. From an adversary's perspective, RDP provides a means to [laterally move](https://attack.mitre.org/tactics/TA0008) to a new host. Determining which RDP connections correspond to adversary activity can be a difficult problem in highly dynamic environments, but will be useful in identifying the scope of a compromise.

Remote Desktop can be detected in several ways

-   Network connections to port 3389/tcp (assuming use of the default port)
-   Packet capture analysis
-   Windows security logs (Event ID 4624, 4634, 4647, 4778)
-   Detecting network connections from `mstsc.exe`
-   Execution of the process `rdpclip.exe`
-   Runs as the clipboard manager on the RDP target if clipboard sharing is enabled

### Output Description

The time of the Connection, the source, the destination, and the user name used

## ATT&CK Coverage

- [[kb/attack/techniques/T1021-remote_services|T1021]] (coverage: Medium; tactics: TA0008)
  - [[kb/attack/techniques/T1021-remote_services|T1021.001]]

## Implementations

### pseudocode

```pseudocode
flow_start = search Flow:Start
flow_end = search Flow:End
rdp_start = filter flow_start where (port == "3389")
rdp_end = filter flow_start where (port == "3389")
rdp = group flow_start, flow_end by src_ip, src_port, dest_ip, dest_port
output rdp
```

### Sigma

[Sigma](https://github.com/Neo23x0/sigma/blob/master/rules/windows/builtin/win_rdp_localhost_login.yml) rule, focusing on RDP localhost login.

## Data Model References

- flow/end/dest_port
- flow/start/dest_ip
- flow/start/dest_port
- flow/start/src_ip

## D3FEND Mappings

- [[kb/defend/techniques/D3-RTSD-remote_terminal_session_detection|D3-RTSD: Remote Terminal Session Detection]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2013-07-002/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-07-002.yaml)
