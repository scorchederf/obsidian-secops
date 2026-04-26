---
sigma_id: "e6fe26ee-d063-4f5b-b007-39e90aaf50e3"
title: "Potential Persistence Via AutodialDLL"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_persistence_autodial_dll.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_autodial_dll.yml"
build_date: "2026-04-26 15:01:48"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "e6fe26ee-d063-4f5b-b007-39e90aaf50e3"
  - "Potential Persistence Via AutodialDLL"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential Persistence Via AutodialDLL

Detects change the the "AutodialDLL" key which could be used as a persistence method to load custom DLL via the "ws2_32" library

## Metadata

- Rule ID: e6fe26ee-d063-4f5b-b007-39e90aaf50e3
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-10
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_persistence_autodial_dll.yml

## Logsource

- category: registry_set
- product: windows

## Detection

```yaml
selection:
  TargetObject|contains: \Services\WinSock2\Parameters\AutodialDLL
condition: selection
```

## False Positives

- Unlikely

## References

- https://www.hexacorn.com/blog/2015/01/13/beyond-good-ol-run-key-part-24/
- https://persistence-info.github.io/Data/autodialdll.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_autodial_dll.yml)
