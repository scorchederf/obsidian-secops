---
sigma_id: "18ee686c-38a3-4f65-9f44-48a077141f42"
title: "Uncommon Extension Shim Database Installation Via Sdbinst.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sdbinst_susp_extension.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sdbinst_susp_extension.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "18ee686c-38a3-4f65-9f44-48a077141f42"
  - "Uncommon Extension Shim Database Installation Via Sdbinst.EXE"
attack_technique_ids:
  - "T1546.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Uncommon Extension Shim Database Installation Via Sdbinst.EXE

Detects installation of a potentially suspicious new shim with an uncommon extension using sdbinst.exe.
Adversaries may establish persistence and/or elevate privileges by executing malicious content triggered by application shims

## Metadata

- Rule ID: 18ee686c-38a3-4f65-9f44-48a077141f42
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-08-01
- Modified: 2024-01-10
- Source Path: rules/windows/process_creation/proc_creation_win_sdbinst_susp_extension.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.011]]

## Detection

```yaml
selection:
- Image|endswith: \sdbinst.exe
- OriginalFileName: sdbinst.exe
filter_main_legit_ext:
  CommandLine|contains: .sdb
filter_main_legit_extensions:
- CommandLine|endswith:
  - ' -c'
  - ' -f'
  - ' -mm'
  - ' -t'
- CommandLine|contains: ' -m -bg'
filter_main_null:
  CommandLine: null
filter_main_empty:
  CommandLine: ''
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://www.fireeye.com/blog/threat-research/2017/05/fin7-shim-databases-persistence.html
- https://github.com/nasbench/Misc-Research/blob/8ee690e43a379cbce8c9d61107442c36bd9be3d3/Other/Undocumented-Flags-Sdbinst.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sdbinst_susp_extension.yml)
