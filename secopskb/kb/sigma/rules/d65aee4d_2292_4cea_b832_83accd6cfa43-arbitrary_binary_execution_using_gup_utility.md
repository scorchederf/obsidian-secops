---
sigma_id: "d65aee4d-2292-4cea-b832-83accd6cfa43"
title: "Arbitrary Binary Execution Using GUP Utility"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_gup_arbitrary_binary_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_gup_arbitrary_binary_execution.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "d65aee4d-2292-4cea-b832-83accd6cfa43"
  - "Arbitrary Binary Execution Using GUP Utility"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Arbitrary Binary Execution Using GUP Utility

Detects execution of the Notepad++ updater (gup) to launch other commands or executables

## Metadata

- Rule ID: d65aee4d-2292-4cea-b832-83accd6cfa43
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-06-10
- Modified: 2023-03-02
- Source Path: rules/windows/process_creation/proc_creation_win_gup_arbitrary_binary_execution.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
  ParentImage|endswith: \gup.exe
  Image|endswith: \explorer.exe
filter:
  Image|endswith: \explorer.exe
  CommandLine|contains: \Notepad++\notepad++.exe
filter_parent:
  ParentImage|contains: \Notepad++\updater\
filter_null:
  CommandLine: null
condition: selection and not 1 of filter*
```

## False Positives

- Other parent binaries using GUP not currently identified

## References

- https://twitter.com/nas_bench/status/1535322445439180803

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_gup_arbitrary_binary_execution.yml)
