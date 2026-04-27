---
car_id: "CAR-2014-11-006"
title: "Windows Remote Management (WinRM)"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2014-11-006/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2014-11-006.yaml"
build_date: "2026-04-27 19:03:49"
aliases:
  - "CAR-2014-11-006"
  - "Windows Remote Management (WinRM)"
attack_technique_ids:
  - "T1021"
  - "T1021.006"
platforms:
  - "Windows"
implementation_types:
  - "pseudocode"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

When a [Windows Remote Management](https://attack.mitre.org/techniques/T1021/006) connection is opened, the client sends HTTP requests to port 5985 for HTTP or 5986 for HTTPS on the target host. Each HTTP(S) request to the URI "/wsman" is called, and other information is set in the headers. Depending on the operation, the HTTP method may vary (i.e., GET, POST, etc.). This analytic would detect Remote PowerShell, as well as other communications that rely on WinRM. Additionally, it outputs the executable on the client host, the connection information, and the hostname of the target host.

## ATT&CK Coverage

- [[kb/attack/techniques/T1021-remote_services|T1021: Remote Services]] (coverage: Moderate; tactics: TA0008)
  - [[kb/attack/techniques/T1021-remote_services#^t1021006-windows-remote-management|T1021.006: Windows Remote Management]]

## Implementations

### pseudocode

Look for network connections to port 5985 and 5986. To really decipher what is going on, these outputs should be fed into something that can do packet analysis.

```pseudocode
flow = search Flow:Start
winrm = filter flow where (dest_port == 5985)
winrm_s = filter flow where (dest_port == 5986)
output winrm, winrm_s
```

## Data Model References

- flow/start/dest_port

## D3FEND Mappings

- [[kb/defend/techniques/D3-ANAA-administrative_network_activity_analysis|D3-ANAA: Administrative Network Activity Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2014-11-006/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2014-11-006.yaml)
