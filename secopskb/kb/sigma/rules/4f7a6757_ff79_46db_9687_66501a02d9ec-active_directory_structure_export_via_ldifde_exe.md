---
sigma_id: "4f7a6757-ff79-46db-9687-66501a02d9ec"
title: "Active Directory Structure Export Via Ldifde.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_ldifde_export.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_ldifde_export.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "4f7a6757-ff79-46db-9687-66501a02d9ec"
  - "Active Directory Structure Export Via Ldifde.EXE"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Active Directory Structure Export Via Ldifde.EXE

Detects the execution of "ldifde.exe" in order to export organizational Active Directory structure.

## Metadata

- Rule ID: 4f7a6757-ff79-46db-9687-66501a02d9ec
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-03-14
- Source Path: rules/windows/process_creation/proc_creation_win_ldifde_export.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_ldif:
- Image|endswith: \ldifde.exe
- OriginalFileName: ldifde.exe
selection_cmd:
  CommandLine|contains: -f
filter_import:
  CommandLine|contains: ' -i'
condition: all of selection_* and not 1 of filter_*
```

## False Positives

- Unknown

## References

- https://businessinsights.bitdefender.com/deep-dive-into-a-backdoordiplomacy-attack-a-study-of-an-attackers-toolkit
- https://www.documentcloud.org/documents/5743766-Global-Threat-Report-2019.html
- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc731033(v=ws.11)

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_ldifde_export.yml)
