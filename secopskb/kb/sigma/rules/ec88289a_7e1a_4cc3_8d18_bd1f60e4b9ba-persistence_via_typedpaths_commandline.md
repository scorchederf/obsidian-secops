---
sigma_id: "ec88289a-7e1a-4cc3-8d18-bd1f60e4b9ba"
title: "Persistence Via TypedPaths - CommandLine"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_registry_typed_paths_persistence.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_registry_typed_paths_persistence.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "ec88289a-7e1a-4cc3-8d18-bd1f60e4b9ba"
  - "Persistence Via TypedPaths - CommandLine"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Persistence Via TypedPaths - CommandLine

Detects modification addition to the 'TypedPaths' key in the user or admin registry via the commandline. Which might indicate persistence attempt

## Metadata

- Rule ID: ec88289a-7e1a-4cc3-8d18-bd1f60e4b9ba
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-22
- Source Path: rules/windows/process_creation/proc_creation_win_registry_typed_paths_persistence.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
  CommandLine|contains: \Software\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/dez_/status/1560101453150257154
- https://forensafe.com/blogs/typedpaths.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_registry_typed_paths_persistence.yml)
