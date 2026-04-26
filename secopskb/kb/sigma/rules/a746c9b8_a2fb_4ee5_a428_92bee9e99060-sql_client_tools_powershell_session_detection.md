---
sigma_id: "a746c9b8-a2fb-4ee5-a428-92bee9e99060"
title: "SQL Client Tools PowerShell Session Detection"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_mssql_sqltoolsps_susp_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mssql_sqltoolsps_susp_execution.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "a746c9b8-a2fb-4ee5-a428-92bee9e99060"
  - "SQL Client Tools PowerShell Session Detection"
attack_technique_ids:
  - "T1059.001"
  - "T1127"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# SQL Client Tools PowerShell Session Detection

This rule detects execution of a PowerShell code through the sqltoolsps.exe utility, which is included in the standard set of utilities supplied with the Microsoft SQL Server Management studio.
Script blocks are not logged in this case, so this utility helps to bypass protection mechanisms based on the analysis of these logs.

## Metadata

- Rule ID: a746c9b8-a2fb-4ee5-a428-92bee9e99060
- Status: test
- Level: medium
- Author: Agro (@agro_sev) oscd.communitly
- Date: 2020-10-13
- Modified: 2022-02-25
- Source Path: rules/windows/process_creation/proc_creation_win_mssql_sqltoolsps_susp_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]
- [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127]]

## Detection

```yaml
selection:
- Image|endswith: \sqltoolsps.exe
- ParentImage|endswith: \sqltoolsps.exe
- OriginalFileName: \sqltoolsps.exe
filter:
  ParentImage|endswith: \smss.exe
condition: selection and not filter
```

## False Positives

- Direct PS command execution through SQLToolsPS.exe is uncommon, childprocess sqltoolsps.exe spawned by smss.exe is a legitimate action.

## References

- https://github.com/LOLBAS-Project/LOLBAS/blob/8283d8d91552213ded165fd36deb6cb9534cb443/yml/OtherMSBinaries/Sqltoolsps.yml
- https://twitter.com/pabraeken/status/993298228840992768

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mssql_sqltoolsps_susp_execution.yml)
