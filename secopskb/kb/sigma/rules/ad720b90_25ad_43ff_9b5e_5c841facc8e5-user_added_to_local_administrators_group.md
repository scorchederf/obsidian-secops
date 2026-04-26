---
sigma_id: "ad720b90-25ad-43ff-9b5e-5c841facc8e5"
title: "User Added to Local Administrators Group"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_add_user_local_admin_group.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_add_user_local_admin_group.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "ad720b90-25ad-43ff-9b5e-5c841facc8e5"
  - "User Added to Local Administrators Group"
attack_technique_ids:
  - "T1098"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# User Added to Local Administrators Group

Detects addition of users to the local administrator group via "Net" or "Add-LocalGroupMember".

## Metadata

- Rule ID: ad720b90-25ad-43ff-9b5e-5c841facc8e5
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-12
- Modified: 2023-03-02
- Source Path: rules/windows/process_creation/proc_creation_win_susp_add_user_local_admin_group.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1098-account_manipulation|T1098]]

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
  - ' administrators '
  - ' administrateur'
condition: all of selection_*
```

## False Positives

- Administrative activity

## References

- https://blog.talosintelligence.com/2022/08/recent-cyber-attack.html?m=1

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_add_user_local_admin_group.yml)
