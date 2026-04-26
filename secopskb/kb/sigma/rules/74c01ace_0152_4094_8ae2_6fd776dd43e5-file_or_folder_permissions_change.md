---
sigma_id: "74c01ace-0152-4094-8ae2-6fd776dd43e5"
title: "File or Folder Permissions Change"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/execve/lnx_auditd_file_or_folder_permissions.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_file_or_folder_permissions.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "low"
logsource: "linux / auditd"
aliases:
  - "74c01ace-0152-4094-8ae2-6fd776dd43e5"
  - "File or Folder Permissions Change"
attack_technique_ids:
  - "T1222.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# File or Folder Permissions Change

Detects file and folder permission changes.

## Metadata

- Rule ID: 74c01ace-0152-4094-8ae2-6fd776dd43e5
- Status: test
- Level: low
- Author: Jakob Weinzettl, oscd.community
- Date: 2019-09-23
- Modified: 2021-11-27
- Source Path: rules/linux/auditd/execve/lnx_auditd_file_or_folder_permissions.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1222-file_and_directory_permissions_modification|T1222.002]]

## Detection

```yaml
selection:
  type: EXECVE
  a0|contains:
  - chmod
  - chown
condition: selection
```

## False Positives

- User interacting with files permissions (normal/daily behaviour).

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1222.002/T1222.002.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_file_or_folder_permissions.yml)
