---
sigma_id: "b3cec4e7-6901-4b0d-a02d-8ab2d8eb818b"
title: "File Time Attribute Change - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/execve/lnx_auditd_change_file_time_attr.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_change_file_time_attr.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "medium"
logsource: "linux / auditd"
aliases:
  - "b3cec4e7-6901-4b0d-a02d-8ab2d8eb818b"
  - "File Time Attribute Change - Linux"
attack_technique_ids:
  - "T1070.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# File Time Attribute Change - Linux

Detect file time attribute change to hide new or changes to existing files.

## Metadata

- Rule ID: b3cec4e7-6901-4b0d-a02d-8ab2d8eb818b
- Status: test
- Level: medium
- Author: Igor Fits, oscd.community
- Date: 2020-10-15
- Modified: 2022-11-28
- Source Path: rules/linux/auditd/execve/lnx_auditd_change_file_time_attr.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070.006]]

## Detection

```yaml
execve:
  type: EXECVE
touch:
- touch
selection2:
- -t
- -acmr
- -d
- -r
condition: execve and touch and selection2
```

## False Positives

- Unknown

## Simulation

### Set a file's access timestamp

- atomic_guid: 5f9113d5-ed75-47ed-ba23-ea3573d05810
- name: Set a file's access timestamp
- technique: T1070.006
- type: atomic-red-team

### Set a file's modification timestamp

- atomic_guid: 20ef1523-8758-4898-b5a2-d026cc3d2c52
- name: Set a file's modification timestamp
- technique: T1070.006
- type: atomic-red-team

### Modify file timestamps using reference file

- atomic_guid: 631ea661-d661-44b0-abdb-7a7f3fc08e50
- name: Modify file timestamps using reference file
- technique: T1070.006
- type: atomic-red-team

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1070.006/T1070.006.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_change_file_time_attr.yml)
