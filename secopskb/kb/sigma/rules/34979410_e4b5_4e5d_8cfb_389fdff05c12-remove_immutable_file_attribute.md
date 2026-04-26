---
sigma_id: "34979410-e4b5-4e5d-8cfb-389fdff05c12"
title: "Remove Immutable File Attribute"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_chattr_immutable_removal.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_chattr_immutable_removal.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "34979410-e4b5-4e5d-8cfb-389fdff05c12"
  - "Remove Immutable File Attribute"
attack_technique_ids:
  - "T1222.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remove Immutable File Attribute

Detects usage of the 'chattr' utility to remove immutable file attribute.

## Metadata

- Rule ID: 34979410-e4b5-4e5d-8cfb-389fdff05c12
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-09-15
- Source Path: rules/linux/process_creation/proc_creation_lnx_chattr_immutable_removal.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1222-file_and_directory_permissions_modification|T1222.002]]

## Detection

```yaml
selection:
  Image|endswith: /chattr
  CommandLine|contains: ' -i '
condition: selection
```

## False Positives

- Administrator interacting with immutable files (e.g. for instance backups).

## References

- https://www.trendmicro.com/en_us/research/22/i/how-malicious-actors-abuse-native-linux-tools-in-their-attacks.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_chattr_immutable_removal.yml)
