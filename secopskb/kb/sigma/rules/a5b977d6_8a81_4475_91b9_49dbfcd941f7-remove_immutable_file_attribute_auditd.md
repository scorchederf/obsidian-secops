---
sigma_id: "a5b977d6-8a81-4475-91b9-49dbfcd941f7"
title: "Remove Immutable File Attribute - Auditd"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/execve/lnx_auditd_chattr_immutable_removal.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_chattr_immutable_removal.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "linux / auditd"
aliases:
  - "a5b977d6-8a81-4475-91b9-49dbfcd941f7"
  - "Remove Immutable File Attribute - Auditd"
attack_technique_ids:
  - "T1222.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remove Immutable File Attribute - Auditd

Detects removing immutable file attribute.

## Metadata

- Rule ID: a5b977d6-8a81-4475-91b9-49dbfcd941f7
- Status: test
- Level: medium
- Author: Jakob Weinzettl, oscd.community
- Date: 2019-09-23
- Modified: 2022-11-26
- Source Path: rules/linux/auditd/execve/lnx_auditd_chattr_immutable_removal.yml

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
  a0|contains: chattr
  a1|contains: -i
condition: selection
```

## False Positives

- Administrator interacting with immutable files (e.g. for instance backups).

## Simulation

### Remove immutable file attribute

- atomic_guid: e7469fe2-ad41-4382-8965-99b94dd3c13f
- name: Remove immutable file attribute
- technique: T1222.002
- type: atomic-red-team

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1222.002/T1222.002.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_chattr_immutable_removal.yml)
