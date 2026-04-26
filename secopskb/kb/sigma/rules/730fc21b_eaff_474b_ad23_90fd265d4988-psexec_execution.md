---
sigma_id: "730fc21b-eaff-474b-ad23-90fd265d4988"
title: "Psexec Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sysinternals_psexec_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_psexec_execution.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "730fc21b-eaff-474b-ad23-90fd265d4988"
  - "Psexec Execution"
attack_technique_ids:
  - "T1569"
  - "T1021"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Psexec Execution

Detects user accept agreement execution in psexec commandline

## Metadata

- Rule ID: 730fc21b-eaff-474b-ad23-90fd265d4988
- Status: test
- Level: medium
- Author: omkar72
- Date: 2020-10-30
- Modified: 2023-02-28
- Source Path: rules/windows/process_creation/proc_creation_win_sysinternals_psexec_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1569-system_services|T1569]]
- [[kb/attack/techniques/T1021-remote_services|T1021]]

## Detection

```yaml
selection:
- Image|endswith: \psexec.exe
- OriginalFileName: psexec.c
condition: selection
```

## False Positives

- Administrative scripts.

## References

- https://www.fireeye.com/blog/threat-research/2020/10/kegtap-and-singlemalt-with-a-ransomware-chaser.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_psexec_execution.yml)
