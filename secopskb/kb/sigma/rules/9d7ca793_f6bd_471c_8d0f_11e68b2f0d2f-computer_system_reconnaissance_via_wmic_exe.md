---
sigma_id: "9d7ca793-f6bd-471c-8d0f-11e68b2f0d2f"
title: "Computer System Reconnaissance Via Wmic.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wmic_recon_computersystem.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_recon_computersystem.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "9d7ca793-f6bd-471c-8d0f-11e68b2f0d2f"
  - "Computer System Reconnaissance Via Wmic.EXE"
attack_technique_ids:
  - "T1047"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Computer System Reconnaissance Via Wmic.EXE

Detects execution of wmic utility with the "computersystem" flag in order to obtain information about the machine such as the domain, username, model, etc.

## Metadata

- Rule ID: 9d7ca793-f6bd-471c-8d0f-11e68b2f0d2f
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-09-08
- Modified: 2023-02-14
- Source Path: rules/windows/process_creation/proc_creation_win_wmic_recon_computersystem.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]

## Detection

```yaml
selection_img:
- Image|endswith: \wmic.exe
- OriginalFileName: wmic.exe
selection_cli:
  CommandLine|contains: computersystem
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://www.microsoft.com/security/blog/2022/09/07/profiling-dev-0270-phosphorus-ransomware-operations/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_recon_computersystem.yml)
