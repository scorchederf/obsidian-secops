---
sigma_id: "ddf36b67-e872-4507-ab2e-46bda21b842c"
title: "Local System Accounts Discovery - MacOs"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_local_account.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_local_account.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "low"
logsource: "macos / process_creation"
aliases:
  - "ddf36b67-e872-4507-ab2e-46bda21b842c"
  - "Local System Accounts Discovery - MacOs"
attack_technique_ids:
  - "T1087.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Local System Accounts Discovery - MacOs

Detects enumeration of local systeam accounts on MacOS

## Metadata

- Rule ID: ddf36b67-e872-4507-ab2e-46bda21b842c
- Status: test
- Level: low
- Author: Alejandro Ortuno, oscd.community
- Date: 2020-10-08
- Modified: 2022-11-27
- Source Path: rules/macos/process_creation/proc_creation_macos_local_account.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1087-account_discovery|T1087.001]]

## Detection

```yaml
selection_1:
  Image|endswith: /dscl
  CommandLine|contains|all:
  - list
  - /users
selection_2:
  Image|endswith: /dscacheutil
  CommandLine|contains|all:
  - -q
  - user
selection_3:
  CommandLine|contains: '''x:0:'''
selection_4:
  Image|endswith: /cat
  CommandLine|contains:
  - /etc/passwd
  - /etc/sudoers
selection_5:
  Image|endswith: /id
selection_6:
  Image|endswith: /lsof
  CommandLine|contains: -u
condition: 1 of selection*
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1087.001/T1087.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_local_account.yml)
