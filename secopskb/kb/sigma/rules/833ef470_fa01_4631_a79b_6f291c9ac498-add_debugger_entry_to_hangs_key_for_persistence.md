---
sigma_id: "833ef470-fa01-4631-a79b-6f291c9ac498"
title: "Add Debugger Entry To Hangs Key For Persistence"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_hangs_debugger_persistence.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_hangs_debugger_persistence.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "833ef470-fa01-4631-a79b-6f291c9ac498"
  - "Add Debugger Entry To Hangs Key For Persistence"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Add Debugger Entry To Hangs Key For Persistence

Detects when an attacker adds a new "Debugger" value to the "Hangs" key in order to achieve persistence which will get invoked when an application crashes

## Metadata

- Rule ID: 833ef470-fa01-4631-a79b-6f291c9ac498
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-21
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_hangs_debugger_persistence.yml

## Logsource

- category: registry_set
- product: windows

## Detection

```yaml
selection:
  TargetObject|contains: \SOFTWARE\Microsoft\Windows\Windows Error Reporting\Hangs\Debugger
condition: selection
```

## False Positives

- This value is not set by default but could be rarly used by administrators

## References

- https://persistence-info.github.io/Data/wer_debugger.html
- https://www.hexacorn.com/blog/2019/09/20/beyond-good-ol-run-key-part-116/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_hangs_debugger_persistence.yml)
