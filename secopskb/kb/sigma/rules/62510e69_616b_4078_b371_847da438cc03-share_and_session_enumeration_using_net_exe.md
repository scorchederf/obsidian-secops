---
sigma_id: "62510e69-616b-4078-b371-847da438cc03"
title: "Share And Session Enumeration Using Net.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_net_view_share_and_sessions_enum.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_net_view_share_and_sessions_enum.yml"
build_date: "2026-04-26 14:14:35"
status: "stable"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "62510e69-616b-4078-b371-847da438cc03"
  - "Share And Session Enumeration Using Net.EXE"
attack_technique_ids:
  - "T1018"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Share And Session Enumeration Using Net.EXE

Detects attempts to enumerate file shares, printer shares and sessions using "net.exe" with the "view" flag.

## Metadata

- Rule ID: 62510e69-616b-4078-b371-847da438cc03
- Status: stable
- Level: low
- Author: Endgame, JHasenbusch (ported for oscd.community)
- Date: 2018-10-30
- Modified: 2023-02-21
- Source Path: rules/windows/process_creation/proc_creation_win_net_view_share_and_sessions_enum.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1018-remote_system_discovery|T1018]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \net.exe
  - \net1.exe
- OriginalFileName:
  - net.exe
  - net1.exe
selection_cli:
  CommandLine|contains: view
filter:
  CommandLine|contains: \\\\
condition: all of selection_* and not filter
```

## False Positives

- Legitimate use of net.exe utility by legitimate user

## References

- https://eqllib.readthedocs.io/en/latest/analytics/b8a94d2f-dc75-4630-9d73-1edc6bd26fff.html
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1018/T1018.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_net_view_share_and_sessions_enum.yml)
