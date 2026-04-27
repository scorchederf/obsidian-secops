---
sigma_id: "f72aa3e8-49f9-4c7d-bd74-f8ab84ff9bbb"
title: "Suspicious RDP Redirect Using TSCON"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_tscon_rdp_redirect.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_tscon_rdp_redirect.yml"
build_date: "2026-04-27 19:13:57"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "f72aa3e8-49f9-4c7d-bd74-f8ab84ff9bbb"
  - "Suspicious RDP Redirect Using TSCON"
attack_technique_ids:
  - "T1563.002"
  - "T1021.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a suspicious RDP session redirect using tscon.exe

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1563-remote_service_session_hijacking#^t1563002-rdp-hijacking|T1563.002: RDP Hijacking]]
- [[kb/attack/techniques/T1021-remote_services#^t1021001-remote-desktop-protocol|T1021.001: Remote Desktop Protocol]]

## Detection

```yaml
selection:
  CommandLine|contains: ' /dest:rdp-tcp#'
condition: selection
```

## False Positives

- Unknown

## References

- http://www.korznikov.com/2017/03/0-day-or-feature-privilege-escalation.html
- https://medium.com/@networksecurity/rdp-hijacking-how-to-hijack-rds-and-remoteapp-sessions-transparently-to-move-through-an-da2a1e73a5f6
- https://www.hackingarticles.in/rdp-session-hijacking-with-tscon/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_tscon_rdp_redirect.yml)
