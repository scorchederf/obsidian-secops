---
sigma_id: "eae8ce9f-bde9-47a6-8e79-f20d18419910"
title: "Suspicious History File Operations - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/execve/lnx_auditd_susp_histfile_operations.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_susp_histfile_operations.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "linux / auditd"
aliases:
  - "eae8ce9f-bde9-47a6-8e79-f20d18419910"
  - "Suspicious History File Operations - Linux"
attack_technique_ids:
  - "T1552.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious History File Operations - Linux

Detects commandline operations on shell history files

## Metadata

- Rule ID: eae8ce9f-bde9-47a6-8e79-f20d18419910
- Status: test
- Level: medium
- Author: Mikhail Larin, oscd.community
- Date: 2020-10-17
- Modified: 2022-11-28
- Source Path: rules/linux/auditd/execve/lnx_auditd_susp_histfile_operations.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.003]]

## Detection

```yaml
execve:
  type: EXECVE
history:
- .bash_history
- .zsh_history
- .zhistory
- .history
- .sh_history
- fish_history
condition: execve and history
```

## False Positives

- Legitimate administrative activity
- Legitimate software, cleaning hist file

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1552.003/T1552.003.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_susp_histfile_operations.yml)
