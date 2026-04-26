---
sigma_id: "c52a914f-3d8b-4b2a-bb75-b3991e75f8ba"
title: "Binary Padding - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/execve/lnx_auditd_binary_padding.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_binary_padding.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "linux / auditd"
aliases:
  - "c52a914f-3d8b-4b2a-bb75-b3991e75f8ba"
  - "Binary Padding - Linux"
attack_technique_ids:
  - "T1027.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Binary Padding - Linux

Adversaries may use binary padding to add junk data and change the on-disk representation of malware.
This rule detect using dd and truncate to add a junk data to file.

## Metadata

- Rule ID: c52a914f-3d8b-4b2a-bb75-b3991e75f8ba
- Status: test
- Level: high
- Author: Igor Fits, oscd.community
- Date: 2020-10-13
- Modified: 2023-05-03
- Source Path: rules/linux/auditd/execve/lnx_auditd_binary_padding.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027.001]]

## Detection

```yaml
selection_execve:
  type: EXECVE
keywords_truncate:
  '|all':
  - truncate
  - -s
keywords_dd:
  '|all':
  - dd
  - if=
keywords_filter:
- of=
condition: selection_execve and (keywords_truncate or (keywords_dd and not keywords_filter))
```

## False Positives

- Unknown

## Simulation

### Pad Binary to Change Hash - Linux/macOS dd

- Atomic Test: [[kb/atomic/tests/ffe2346c_abd5_4b45_a713_bf5f1ebd573a-pad_binary_to_change_hash_linux_macos_dd|ffe2346c-abd5-4b45-a713-bf5f1ebd573a]]
- atomic_guid: ffe2346c-abd5-4b45-a713-bf5f1ebd573a
- name: Pad Binary to Change Hash - Linux/macOS dd
- technique: T1027.001
- type: atomic-red-team

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1027.001/T1027.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_binary_padding.yml)
