---
sigma_id: "53b1b378-9b06-4992-b972-dde6e423d2b4"
title: "Credentials In Files"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_find_cred_in_files.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_find_cred_in_files.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "high"
logsource: "macos / process_creation"
aliases:
  - "53b1b378-9b06-4992-b972-dde6e423d2b4"
  - "Credentials In Files"
attack_technique_ids:
  - "T1552.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Credentials In Files

Detecting attempts to extract passwords with grep and laZagne

## Metadata

- Rule ID: 53b1b378-9b06-4992-b972-dde6e423d2b4
- Status: test
- Level: high
- Author: Igor Fits, Mikhail Larin, oscd.community
- Date: 2020-10-19
- Modified: 2021-11-27
- Source Path: rules/macos/process_creation/proc_creation_macos_find_cred_in_files.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.001]]

## Detection

```yaml
selection1:
  Image|endswith: /grep
  CommandLine|contains: password
selection2:
  CommandLine|contains: laZagne
condition: 1 of selection*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1552.001/T1552.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_find_cred_in_files.yml)
