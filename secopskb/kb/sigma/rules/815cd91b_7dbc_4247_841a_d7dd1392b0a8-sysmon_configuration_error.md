---
sigma_id: "815cd91b-7dbc-4247-841a-d7dd1392b0a8"
title: "Sysmon Configuration Error"
framework: "sigma"
generated: "true"
source_path: "rules/windows/sysmon/sysmon_config_modification_error.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/sysmon/sysmon_config_modification_error.yml"
build_date: "2026-04-27 19:13:57"
status: "test"
level: "high"
logsource: "windows / sysmon_error"
aliases:
  - "815cd91b-7dbc-4247-841a-d7dd1392b0a8"
  - "Sysmon Configuration Error"
attack_technique_ids:
  - "T1564"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects when an adversary is trying to hide it's action from Sysmon logging based on error messages

## Logsource

- category: sysmon_error
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1564-hide_artifacts|T1564: Hide Artifacts]]

## Detection

```yaml
selection_error:
  Description|contains:
  - Failed to open service configuration with error
  - Failed to connect to the driver to update configuration
filter_generic_english:
  Description|contains|all:
  - Failed to open service configuration with error
  - 'Last error: The media is write protected.'
filter_by_errorcode:
  Description|contains:
  - Failed to open service configuration with error 19
  - Failed to open service configuration with error 93
condition: selection_error and not 1 of filter*
```

## False Positives

- Legitimate administrative action

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1562.001/T1562.001.md
- https://talesfrominfosec.blogspot.com/2017/12/killing-sysmon-silently.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/sysmon/sysmon_config_modification_error.yml)
