---
sigma_id: "ffa28e60-bdb1-46e0-9f82-05f7a61cc06e"
title: "User Added to Remote Desktop Users Group"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_add_user_remote_desktop_group.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_add_user_remote_desktop_group.yml"
build_date: "2026-04-27 19:13:58"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "ffa28e60-bdb1-46e0-9f82-05f7a61cc06e"
  - "User Added to Remote Desktop Users Group"
attack_technique_ids:
  - "T1133"
  - "T1136.001"
  - "T1021.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects addition of users to the local Remote Desktop Users group via "Net" or "Add-LocalGroupMember".

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1133-external_remote_services|T1133: External Remote Services]]
- [[kb/attack/techniques/T1136-create_account#^t1136001-local-account|T1136.001: Local Account]]
- [[kb/attack/techniques/T1021-remote_services#^t1021001-remote-desktop-protocol|T1021.001: Remote Desktop Protocol]]

## Detection

```yaml
selection_main:
- CommandLine|contains|all:
  - 'localgroup '
  - ' /add'
- CommandLine|contains|all:
  - 'Add-LocalGroupMember '
  - ' -Group '
selection_group:
  CommandLine|contains:
  - Remote Desktop Users
  - Utilisateurs du Bureau à distance
  - Usuarios de escritorio remoto
condition: all of selection_*
```

## False Positives

- Administrative activity

## References

- https://www.microsoft.com/security/blog/2021/11/16/evolving-trends-in-iranian-threat-actor-activity-mstic-presentation-at-cyberwarcon-2021/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_add_user_remote_desktop_group.yml)
