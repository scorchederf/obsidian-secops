---
sigma_id: "7be5fb68-f9ef-476d-8b51-0256ebece19e"
title: "Suspicious Execution of Hostname"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hostname_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hostname_execution.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "7be5fb68-f9ef-476d-8b51-0256ebece19e"
  - "Suspicious Execution of Hostname"
attack_technique_ids:
  - "T1082"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Execution of Hostname

Use of hostname to get information

## Metadata

- Rule ID: 7be5fb68-f9ef-476d-8b51-0256ebece19e
- Status: test
- Level: low
- Author: frack113
- Date: 2022-01-01
- Source Path: rules/windows/process_creation/proc_creation_win_hostname_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]

## Detection

```yaml
selection:
  Image|endswith: \HOSTNAME.EXE
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1082/T1082.md#atomic-test-6---hostname-discovery-windows
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/hostname

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hostname_execution.yml)
