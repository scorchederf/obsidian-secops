---
sigma_id: "224f140f-3553-4cd1-af78-13d81bf9f7cc"
title: "Potential RDP Session Hijacking Activity"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_tscon_rdp_session_hijacking.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_tscon_rdp_session_hijacking.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "224f140f-3553-4cd1-af78-13d81bf9f7cc"
  - "Potential RDP Session Hijacking Activity"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential RDP Session Hijacking Activity

Detects potential RDP Session Hijacking activity on Windows systems

## Metadata

- Rule ID: 224f140f-3553-4cd1-af78-13d81bf9f7cc
- Status: test
- Level: medium
- Author: @juju4
- Date: 2022-12-27
- Modified: 2024-12-01
- Source Path: rules/windows/process_creation/proc_creation_win_tscon_rdp_session_hijacking.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_img:
- Image|endswith: \tscon.exe
- OriginalFileName: tscon.exe
selection_integrity:
  IntegrityLevel:
  - System
  - S-1-16-16384
condition: all of selection_*
```

## False Positives

- Administrative activity

## References

- https://twitter.com/Moti_B/status/909449115477659651

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_tscon_rdp_session_hijacking.yml)
