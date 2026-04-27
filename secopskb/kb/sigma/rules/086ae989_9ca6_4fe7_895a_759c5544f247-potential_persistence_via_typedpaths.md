---
sigma_id: "086ae989-9ca6-4fe7-895a-759c5544f247"
title: "Potential Persistence Via TypedPaths"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_persistence_typed_paths.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_typed_paths.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "086ae989-9ca6-4fe7-895a-759c5544f247"
  - "Potential Persistence Via TypedPaths"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Potential Persistence Via TypedPaths

Detects modification addition to the 'TypedPaths' key in the user or admin registry from a non standard application. Which might indicate persistence attempt

## Metadata

- Rule ID: 086ae989-9ca6-4fe7-895a-759c5544f247
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-22
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_persistence_typed_paths.yml

## Logsource

- category: registry_set
- product: windows

## Detection

```yaml
selection:
  TargetObject|contains: \Software\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths\
filter:
  Image:
  - C:\Windows\explorer.exe
  - C:\Windows\SysWOW64\explorer.exe
condition: selection and not filter
```

## False Positives

- Unlikely

## References

- https://twitter.com/dez_/status/1560101453150257154
- https://forensafe.com/blogs/typedpaths.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_typed_paths.yml)
