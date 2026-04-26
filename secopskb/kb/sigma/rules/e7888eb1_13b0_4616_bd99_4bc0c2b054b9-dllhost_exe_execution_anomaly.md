---
sigma_id: "e7888eb1-13b0-4616-bd99-4bc0c2b054b9"
title: "Dllhost.EXE Execution Anomaly"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_dllhost_no_cli_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dllhost_no_cli_execution.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "e7888eb1-13b0-4616-bd99-4bc0c2b054b9"
  - "Dllhost.EXE Execution Anomaly"
attack_technique_ids:
  - "T1055"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Dllhost.EXE Execution Anomaly

Detects a "dllhost" process spawning with no commandline arguments which is very rare to happen and could indicate process injection activity or malware mimicking similar system processes.

## Metadata

- Rule ID: e7888eb1-13b0-4616-bd99-4bc0c2b054b9
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-06-27
- Modified: 2023-05-15
- Source Path: rules/windows/process_creation/proc_creation_win_dllhost_no_cli_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1055-process_injection|T1055]]

## Detection

```yaml
selection:
  Image|endswith: \dllhost.exe
  CommandLine:
  - dllhost.exe
  - dllhost
filter_main_null:
  CommandLine: null
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unlikely

## References

- https://redcanary.com/blog/child-processes/
- https://nasbench.medium.com/what-is-the-dllhost-exe-process-actually-running-ef9fe4c19c08
- https://www.ncsc.gov.uk/static-assets/documents/malware-analysis-reports/goofy-guineapig/NCSC-MAR-Goofy-Guineapig.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dllhost_no_cli_execution.yml)
