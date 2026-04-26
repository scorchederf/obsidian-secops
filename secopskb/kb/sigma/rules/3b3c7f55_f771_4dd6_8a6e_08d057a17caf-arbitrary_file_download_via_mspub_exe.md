---
sigma_id: "3b3c7f55-f771-4dd6-8a6e-08d057a17caf"
title: "Arbitrary File Download Via MSPUB.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_mspub_download.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mspub_download.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "3b3c7f55-f771-4dd6-8a6e-08d057a17caf"
  - "Arbitrary File Download Via MSPUB.EXE"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Arbitrary File Download Via MSPUB.EXE

Detects usage of "MSPUB" (Microsoft Publisher) to download arbitrary files

## Metadata

- Rule ID: 3b3c7f55-f771-4dd6-8a6e-08d057a17caf
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-19
- Modified: 2023-02-08
- Source Path: rules/windows/process_creation/proc_creation_win_mspub_download.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_img:
- Image|endswith: \MSPUB.exe
- OriginalFileName: MSPUB.exe
selection_cli:
  CommandLine|contains:
  - ftp://
  - http://
  - https://
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/LOLBAS-Project/LOLBAS/pull/238/files

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mspub_download.yml)
