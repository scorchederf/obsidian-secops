---
sigma_id: "6ba5a05f-b095-4f0a-8654-b825f4f16334"
title: "Potential MSTSC Shadowing Activity"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_mstsc_rdp_hijack_shadowing.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mstsc_rdp_hijack_shadowing.yml"
build_date: "2026-04-27 19:13:54"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "6ba5a05f-b095-4f0a-8654-b825f4f16334"
  - "Potential MSTSC Shadowing Activity"
attack_technique_ids:
  - "T1563.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects RDP session hijacking by using MSTSC shadowing

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1563-remote_service_session_hijacking#^t1563002-rdp-hijacking|T1563.002: RDP Hijacking]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - noconsentprompt
  - 'shadow:'
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/kmkz_security/status/1220694202301976576
- https://github.com/kmkz/Pentesting/blob/47592e5e160d3b86c2024f09ef04ceb87d204995/Post-Exploitation-Cheat-Sheet

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mstsc_rdp_hijack_shadowing.yml)
