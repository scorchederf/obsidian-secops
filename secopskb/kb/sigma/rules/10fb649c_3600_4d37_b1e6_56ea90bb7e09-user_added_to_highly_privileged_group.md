---
sigma_id: "10fb649c-3600-4d37-b1e6-56ea90bb7e09"
title: "User Added To Highly Privileged Group"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_add_user_privileged_group.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_add_user_privileged_group.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "10fb649c-3600-4d37-b1e6-56ea90bb7e09"
  - "User Added To Highly Privileged Group"
attack_technique_ids:
  - "T1098"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# User Added To Highly Privileged Group

Detects addition of users to highly privileged groups via "Net" or "Add-LocalGroupMember".

## Metadata

- Rule ID: 10fb649c-3600-4d37-b1e6-56ea90bb7e09
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2024-02-23
- Source Path: rules/windows/process_creation/proc_creation_win_susp_add_user_privileged_group.yml

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
  - Group Policy Creator Owners
  - Schema Admins
condition: all of selection_*
```

## False Positives

- Administrative activity that must be investigated

## References

- https://www.huntress.com/blog/slashandgrab-screen-connect-post-exploitation-in-the-wild-cve-2024-1709-cve-2024-1708

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_add_user_privileged_group.yml)
