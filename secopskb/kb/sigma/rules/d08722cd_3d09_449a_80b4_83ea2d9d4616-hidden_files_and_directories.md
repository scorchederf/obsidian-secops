---
sigma_id: "d08722cd-3d09-449a-80b4-83ea2d9d4616"
title: "Hidden Files and Directories"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/execve/lnx_auditd_hidden_files_directories.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_hidden_files_directories.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "low"
logsource: "linux / auditd"
aliases:
  - "d08722cd-3d09-449a-80b4-83ea2d9d4616"
  - "Hidden Files and Directories"
attack_technique_ids:
  - "T1564.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Hidden Files and Directories

Detects adversary creating hidden file or directory, by detecting directories or files with . as the first character

## Metadata

- Rule ID: d08722cd-3d09-449a-80b4-83ea2d9d4616
- Status: test
- Level: low
- Author: Pawel Mazur
- Date: 2021-09-06
- Modified: 2025-06-16
- Source Path: rules/linux/auditd/execve/lnx_auditd_hidden_files_directories.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1564-hide_artifacts|T1564.001]]

## Detection

```yaml
selection_commands:
  type: EXECVE
  a0:
  - mkdir
  - nano
  - touch
  - vi
  - vim
selection_arguments:
- a1|re: (^|\/)\.[^.\/]
- a2|re: (^|\/)\.[^.\/]
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1564.001/T1564.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_hidden_files_directories.yml)
