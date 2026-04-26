---
sigma_id: "80915f59-9b56-4616-9de0-fd0dea6c12fe"
title: "Clear Linux Logs"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_clear_logs.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_clear_logs.yml"
build_date: "2026-04-26 14:14:22"
status: "stable"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "80915f59-9b56-4616-9de0-fd0dea6c12fe"
  - "Clear Linux Logs"
attack_technique_ids:
  - "T1070.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Clear Linux Logs

Detects attempts to clear logs on the system. Adversaries may clear system logs to hide evidence of an intrusion

## Metadata

- Rule ID: 80915f59-9b56-4616-9de0-fd0dea6c12fe
- Status: stable
- Level: medium
- Author: Ömer Günal, oscd.community
- Date: 2020-10-07
- Modified: 2022-09-15
- Source Path: rules/linux/process_creation/proc_creation_lnx_clear_logs.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070.002]]

## Detection

```yaml
selection:
  Image|endswith:
  - /rm
  - /shred
  - /unlink
  CommandLine|contains:
  - /var/log
  - /var/spool/mail
condition: selection
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1070.002/T1070.002.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_clear_logs.yml)
