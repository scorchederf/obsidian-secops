---
sigma_id: "2dad0cba-c62a-4a4f-949f-5f6ecd619769"
title: "Split A File Into Pieces - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/syscall/lnx_auditd_split_file_into_pieces.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/syscall/lnx_auditd_split_file_into_pieces.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "low"
logsource: "linux / auditd"
aliases:
  - "2dad0cba-c62a-4a4f-949f-5f6ecd619769"
  - "Split A File Into Pieces - Linux"
attack_technique_ids:
  - "T1030"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Split A File Into Pieces - Linux

Detection use of the command "split" to split files into parts and possible transfer.

## Metadata

- Rule ID: 2dad0cba-c62a-4a4f-949f-5f6ecd619769
- Status: test
- Level: low
- Author: Igor Fits, oscd.community
- Date: 2020-10-15
- Modified: 2022-11-28
- Source Path: rules/linux/auditd/syscall/lnx_auditd_split_file_into_pieces.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1030-data_transfer_size_limits|T1030]]

## Detection

```yaml
selection:
  type: SYSCALL
  comm: split
condition: selection
```

## False Positives

- Legitimate administrative activity

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1030/T1030.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/syscall/lnx_auditd_split_file_into_pieces.yml)
