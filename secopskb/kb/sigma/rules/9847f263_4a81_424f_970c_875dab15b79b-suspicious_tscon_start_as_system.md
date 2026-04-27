---
sigma_id: "9847f263-4a81-424f-970c-875dab15b79b"
title: "Suspicious TSCON Start as SYSTEM"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_tscon_localsystem.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_tscon_localsystem.yml"
build_date: "2026-04-27 19:13:57"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "9847f263-4a81-424f-970c-875dab15b79b"
  - "Suspicious TSCON Start as SYSTEM"
attack_technique_ids:
  - "T1219.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a tscon.exe start as LOCAL SYSTEM

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1219-remote_access_tools#^t1219002-remote-desktop-software|T1219.002: Remote Desktop Software]]

## Detection

```yaml
selection:
  User|contains:
  - AUTHORI
  - AUTORI
  Image|endswith: \tscon.exe
condition: selection
```

## False Positives

- Unknown

## References

- http://www.korznikov.com/2017/03/0-day-or-feature-privilege-escalation.html
- https://medium.com/@networksecurity/rdp-hijacking-how-to-hijack-rds-and-remoteapp-sessions-transparently-to-move-through-an-da2a1e73a5f6
- https://www.ired.team/offensive-security/lateral-movement/t1076-rdp-hijacking-for-lateral-movement

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_tscon_localsystem.yml)
