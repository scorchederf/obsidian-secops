---
sigma_id: "4b046706-5789-4673-b111-66f25fe99534"
title: "Deleted Data Overwritten Via Cipher.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_cipher_overwrite_deleted_data.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cipher_overwrite_deleted_data.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "4b046706-5789-4673-b111-66f25fe99534"
  - "Deleted Data Overwritten Via Cipher.EXE"
attack_technique_ids:
  - "T1485"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Deleted Data Overwritten Via Cipher.EXE

Detects usage of the "cipher" built-in utility in order to overwrite deleted data from disk.
Adversaries may destroy data and files on specific systems or in large numbers on a network to interrupt availability to systems, services, and network resources.
Data destruction is likely to render stored data irrecoverable by forensic techniques through overwriting files or data on local and remote drives

## Metadata

- Rule ID: 4b046706-5789-4673-b111-66f25fe99534
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-12-26
- Modified: 2023-02-21
- Source Path: rules/windows/process_creation/proc_creation_win_cipher_overwrite_deleted_data.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1485-data_destruction|T1485]]

## Detection

```yaml
selection_img:
- OriginalFileName: CIPHER.EXE
- Image|endswith: \cipher.exe
selection_cli:
  CommandLine|contains: ' /w:'
condition: all of selection_*
```

## False Positives

- Unknown

## Simulation

### Overwrite deleted data on C drive

- atomic_guid: 321fd25e-0007-417f-adec-33232252be19
- name: Overwrite deleted data on C drive
- technique: T1485
- type: atomic-red-team

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1485/T1485.md#atomic-test-3---overwrite-deleted-data-on-c-drive

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cipher_overwrite_deleted_data.yml)
