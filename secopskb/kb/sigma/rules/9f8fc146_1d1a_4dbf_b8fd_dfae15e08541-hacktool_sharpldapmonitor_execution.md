---
sigma_id: "9f8fc146-1d1a-4dbf-b8fd-dfae15e08541"
title: "HackTool - SharpLDAPmonitor Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_sharp_ldap_monitor.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_sharp_ldap_monitor.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "9f8fc146-1d1a-4dbf-b8fd-dfae15e08541"
  - "HackTool - SharpLDAPmonitor Execution"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# HackTool - SharpLDAPmonitor Execution

Detects execution of the SharpLDAPmonitor. Which can monitor the creation, deletion and changes to LDAP objects.

## Metadata

- Rule ID: 9f8fc146-1d1a-4dbf-b8fd-dfae15e08541
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-12-30
- Modified: 2023-02-14
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_sharp_ldap_monitor.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_img:
- Image|endswith: \SharpLDAPmonitor.exe
- OriginalFileName: SharpLDAPmonitor.exe
selection_cli:
  CommandLine|contains|all:
  - '/user:'
  - '/pass:'
  - '/dcip:'
condition: 1 of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/p0dalirius/LDAPmonitor

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_sharp_ldap_monitor.yml)
