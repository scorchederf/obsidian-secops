---
sigma_id: "95361ce5-c891-4b0a-87ca-e24607884a96"
title: "Binary Padding - MacOS"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_binary_padding.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_binary_padding.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "macos / process_creation"
aliases:
  - "95361ce5-c891-4b0a-87ca-e24607884a96"
  - "Binary Padding - MacOS"
attack_technique_ids:
  - "T1027.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Binary Padding - MacOS

Adversaries may use binary padding to add junk data and change the on-disk representation of malware. This rule detect using dd and truncate to add a junk data to file.

## Metadata

- Rule ID: 95361ce5-c891-4b0a-87ca-e24607884a96
- Status: test
- Level: high
- Author: Igor Fits, Mikhail Larin, oscd.community
- Date: 2020-10-19
- Modified: 2023-02-17
- Source Path: rules/macos/process_creation/proc_creation_macos_binary_padding.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027.001]]

## Detection

```yaml
selection_truncate:
  Image|endswith: /truncate
  CommandLine|contains: -s +
selection_dd:
  Image|endswith: /dd
  CommandLine|contains:
  - if=/dev/zero
  - if=/dev/random
  - if=/dev/urandom
condition: 1 of selection_*
```

## False Positives

- Legitimate script work

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1027.001/T1027.001.md
- https://linux.die.net/man/1/truncate
- https://linux.die.net/man/1/dd

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_binary_padding.yml)
