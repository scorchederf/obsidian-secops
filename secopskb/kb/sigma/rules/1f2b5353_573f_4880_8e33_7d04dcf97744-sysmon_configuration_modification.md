---
sigma_id: "1f2b5353-573f-4880-8e33-7d04dcf97744"
title: "Sysmon Configuration Modification"
framework: "sigma"
generated: "true"
source_path: "rules/windows/sysmon/sysmon_config_modification_status.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/sysmon/sysmon_config_modification_status.yml"
build_date: "2026-04-26 15:01:52"
status: "test"
level: "high"
logsource: "windows / sysmon_status"
aliases:
  - "1f2b5353-573f-4880-8e33-7d04dcf97744"
  - "Sysmon Configuration Modification"
attack_technique_ids:
  - "T1564"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Sysmon Configuration Modification

Detects when an attacker tries to hide from Sysmon by disabling or stopping it

## Metadata

- Rule ID: 1f2b5353-573f-4880-8e33-7d04dcf97744
- Status: test
- Level: high
- Author: frack113
- Date: 2021-06-04
- Modified: 2022-08-02
- Source Path: rules/windows/sysmon/sysmon_config_modification_status.yml

## Logsource

- category: sysmon_status
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1564-hide_artifacts|T1564]]

## Detection

```yaml
selection_stop:
  State: Stopped
selection_conf:
- Sysmon config state changed
filter:
  State: Started
condition: 1 of selection_* and not filter
```

## False Positives

- Legitimate administrative action

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1562.001/T1562.001.md
- https://talesfrominfosec.blogspot.com/2017/12/killing-sysmon-silently.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/sysmon/sysmon_config_modification_status.yml)
