---
sigma_id: "df3fcaea-2715-4214-99c5-0056ea59eb35"
title: "Credentials In Files - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/execve/lnx_auditd_find_cred_in_files.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_find_cred_in_files.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "linux / auditd"
aliases:
  - "df3fcaea-2715-4214-99c5-0056ea59eb35"
  - "Credentials In Files - Linux"
attack_technique_ids:
  - "T1552.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Credentials In Files - Linux

Detecting attempts to extract passwords with grep

## Metadata

- Rule ID: df3fcaea-2715-4214-99c5-0056ea59eb35
- Status: test
- Level: high
- Author: Igor Fits, oscd.community
- Date: 2020-10-15
- Modified: 2023-04-30
- Source Path: rules/linux/auditd/execve/lnx_auditd_find_cred_in_files.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.001]]

## Detection

```yaml
selection:
  type: EXECVE
keywords:
  '|all':
  - grep
  - password
condition: selection and keywords
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1552.001/T1552.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_find_cred_in_files.yml)
