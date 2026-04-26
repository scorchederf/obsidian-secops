---
sigma_id: "f72aa3e8-49f9-4c7d-bd74-f8ab84ff9bbb"
title: "Suspicious RDP Redirect Using TSCON"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_tscon_rdp_redirect.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_tscon_rdp_redirect.yml"
build_date: "2026-04-26 17:03:23"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious RDP Redirect Using TSCON

Detects a suspicious RDP session redirect using tscon.exe

## Metadata

- Rule ID: f72aa3e8-49f9-4c7d-bd74-f8ab84ff9bbb
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2018-03-17
- Modified: 2023-05-16
- Source Path: rules/windows/process_creation/proc_creation_win_tscon_rdp_redirect.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1563-remote_service_session_hijacking|T1563.002]]
- [[kb/attack/techniques/T1021-remote_services|T1021.001]]

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
