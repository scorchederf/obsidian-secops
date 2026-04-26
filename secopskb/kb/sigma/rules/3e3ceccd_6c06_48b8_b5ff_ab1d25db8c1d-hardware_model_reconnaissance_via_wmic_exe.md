---
sigma_id: "3e3ceccd-6c06-48b8-b5ff-ab1d25db8c1d"
title: "Hardware Model Reconnaissance Via Wmic.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wmic_recon_csproduct.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_recon_csproduct.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "3e3ceccd-6c06-48b8-b5ff-ab1d25db8c1d"
  - "Hardware Model Reconnaissance Via Wmic.EXE"
attack_technique_ids:
  - "T1047"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Hardware Model Reconnaissance Via Wmic.EXE

Detects the execution of WMIC with the "csproduct" which is used to obtain information such as hardware models and vendor information

## Metadata

- Rule ID: 3e3ceccd-6c06-48b8-b5ff-ab1d25db8c1d
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2023-02-14
- Source Path: rules/windows/process_creation/proc_creation_win_wmic_recon_csproduct.yml

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
  CommandLine|contains: csproduct
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://jonconwayuk.wordpress.com/2014/01/31/wmic-csproduct-using-wmi-to-identify-make-and-model-of-hardware/
- https://www.uptycs.com/blog/kuraystealer-a-bandit-using-discord-webhooks

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_recon_csproduct.yml)
