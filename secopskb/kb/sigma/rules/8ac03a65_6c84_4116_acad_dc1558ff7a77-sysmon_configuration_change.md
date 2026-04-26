---
sigma_id: "8ac03a65-6c84-4116-acad-dc1558ff7a77"
title: "Sysmon Configuration Change"
framework: "sigma"
generated: "true"
source_path: "rules/windows/sysmon/sysmon_config_modification.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/sysmon/sysmon_config_modification.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / sysmon"
aliases:
  - "8ac03a65-6c84-4116-acad-dc1558ff7a77"
  - "Sysmon Configuration Change"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Sysmon Configuration Change

Detects a Sysmon configuration change, which could be the result of a legitimate reconfiguration or someone trying manipulate the configuration

## Metadata

- Rule ID: 8ac03a65-6c84-4116-acad-dc1558ff7a77
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-01-12
- Source Path: rules/windows/sysmon/sysmon_config_modification.yml

## Logsource

- product: windows
- service: sysmon

## Detection

```yaml
selection:
  EventID: 16
condition: selection
```

## False Positives

- Legitimate administrative action

## References

- https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/sysmon/sysmon_config_modification.yml)
