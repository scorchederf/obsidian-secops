---
sigma_id: "9e1bef8d-0fff-46f6-8465-9aa54e128c1e"
title: "Use Of Hidden Paths Or Files"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/path/lnx_auditd_hidden_binary_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/path/lnx_auditd_hidden_binary_execution.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "low"
logsource: "linux / auditd"
aliases:
  - "9e1bef8d-0fff-46f6-8465-9aa54e128c1e"
  - "Use Of Hidden Paths Or Files"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Use Of Hidden Paths Or Files

Detects calls to hidden files or files located in hidden directories in NIX systems.

## Metadata

- Rule ID: 9e1bef8d-0fff-46f6-8465-9aa54e128c1e
- Status: test
- Level: low
- Author: David Burkett, @signalblur
- Date: 2022-12-30
- Source Path: rules/linux/auditd/path/lnx_auditd_hidden_binary_execution.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  type: PATH
  name|contains: /.
filter:
  name|contains:
  - /.cache/
  - /.config/
  - /.pyenv/
  - /.rustup/toolchains
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1564.001/T1564.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/path/lnx_auditd_hidden_binary_execution.yml)
