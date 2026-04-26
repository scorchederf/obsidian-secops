---
sigma_id: "88f46b67-14d4-4f45-ac2c-d66984f22191"
title: "Renamed Microsoft Teams Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_renamed_msteams.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_msteams.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "88f46b67-14d4-4f45-ac2c-d66984f22191"
  - "Renamed Microsoft Teams Execution"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Renamed Microsoft Teams Execution

Detects the execution of a renamed Microsoft Teams binary.

## Metadata

- Rule ID: 88f46b67-14d4-4f45-ac2c-d66984f22191
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2024-07-12
- Source Path: rules/windows/process_creation/proc_creation_win_renamed_msteams.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
  OriginalFileName:
  - msteams.exe
  - teams.exe
filter_main_legit_names:
  Image|endswith:
  - \msteams.exe
  - \teams.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_msteams.yml)
