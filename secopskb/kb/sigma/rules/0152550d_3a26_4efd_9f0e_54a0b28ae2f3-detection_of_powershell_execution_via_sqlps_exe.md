---
sigma_id: "0152550d-3a26-4efd-9f0e-54a0b28ae2f3"
title: "Detection of PowerShell Execution via Sqlps.exe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_mssql_sqlps_susp_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mssql_sqlps_susp_execution.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "0152550d-3a26-4efd-9f0e-54a0b28ae2f3"
  - "Detection of PowerShell Execution via Sqlps.exe"
attack_technique_ids:
  - "T1059.001"
  - "T1127"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Detection of PowerShell Execution via Sqlps.exe

This rule detects execution of a PowerShell code through the sqlps.exe utility, which is included in the standard set of utilities supplied with the MSSQL Server.
Script blocks are not logged in this case, so this utility helps to bypass protection mechanisms based on the analysis of these logs.

## Metadata

- Rule ID: 0152550d-3a26-4efd-9f0e-54a0b28ae2f3
- Status: test
- Level: medium
- Author: Agro (@agro_sev) oscd.community
- Date: 2020-10-10
- Modified: 2022-12-09
- Source Path: rules/windows/process_creation/proc_creation_win_mssql_sqlps_susp_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]
- [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127]]

## Detection

```yaml
selection_parent:
  ParentImage|endswith: \sqlps.exe
selection_image:
- Image|endswith: \sqlps.exe
- OriginalFileName: sqlps.exe
filter_image:
  ParentImage|endswith: \sqlagent.exe
condition: selection_parent or (selection_image and not filter_image)
```

## False Positives

- Direct PS command execution through SQLPS.exe is uncommon, childprocess sqlps.exe spawned by sqlagent.exe is a legitimate action.

## References

- https://learn.microsoft.com/en-us/sql/tools/sqlps-utility?view=sql-server-ver15
- https://lolbas-project.github.io/lolbas/OtherMSBinaries/Sqlps/
- https://twitter.com/bryon_/status/975835709587075072

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mssql_sqlps_susp_execution.yml)
