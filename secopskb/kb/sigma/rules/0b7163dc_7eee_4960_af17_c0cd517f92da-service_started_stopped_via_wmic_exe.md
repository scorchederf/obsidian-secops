---
sigma_id: "0b7163dc-7eee-4960-af17-c0cd517f92da"
title: "Service Started/Stopped Via Wmic.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wmic_service_manipulation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_service_manipulation.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "0b7163dc-7eee-4960-af17-c0cd517f92da"
  - "Service Started/Stopped Via Wmic.EXE"
attack_technique_ids:
  - "T1047"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Service Started/Stopped Via Wmic.EXE

Detects usage of wmic to start or stop a service

## Metadata

- Rule ID: 0b7163dc-7eee-4960-af17-c0cd517f92da
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-06-20
- Modified: 2023-02-14
- Source Path: rules/windows/process_creation/proc_creation_win_wmic_service_manipulation.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]

## Detection

```yaml
selection_img:
- OriginalFileName: wmic.exe
- Image|endswith: \WMIC.exe
selection_cli:
  CommandLine|contains|all:
  - ' service '
  - ' call '
  CommandLine|contains:
  - stopservice
  - startservice
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://sushant747.gitbooks.io/total-oscp-guide/content/privilege_escalation_windows.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_service_manipulation.yml)
