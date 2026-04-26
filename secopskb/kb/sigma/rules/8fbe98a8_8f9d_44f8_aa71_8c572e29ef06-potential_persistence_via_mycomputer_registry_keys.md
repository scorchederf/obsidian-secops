---
sigma_id: "8fbe98a8-8f9d-44f8-aa71-8c572e29ef06"
title: "Potential Persistence Via MyComputer Registry Keys"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_persistence_mycomputer.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_mycomputer.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "8fbe98a8-8f9d-44f8-aa71-8c572e29ef06"
  - "Potential Persistence Via MyComputer Registry Keys"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Persistence Via MyComputer Registry Keys

Detects modification to the "Default" value of the "MyComputer" key and subkeys to point to a custom binary that will be launched whenever the associated action is executed (see reference section for example)

## Metadata

- Rule ID: 8fbe98a8-8f9d-44f8-aa71-8c572e29ef06
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-09
- Modified: 2024-01-11
- Source Path: rules/windows/registry/registry_set/registry_set_persistence_mycomputer.yml

## Logsource

- category: registry_set
- product: windows

## Detection

```yaml
selection:
  TargetObject|contains: \Microsoft\Windows\CurrentVersion\Explorer\MyComputer
  TargetObject|endswith: (Default)
condition: selection
```

## False Positives

- Unlikely but if you experience FPs add specific processes and locations you would like to monitor for

## References

- https://www.hexacorn.com/blog/2017/01/18/beyond-good-ol-run-key-part-55/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_mycomputer.yml)
