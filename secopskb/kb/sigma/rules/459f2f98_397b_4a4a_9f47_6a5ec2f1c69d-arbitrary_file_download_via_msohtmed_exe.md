---
sigma_id: "459f2f98-397b-4a4a-9f47-6a5ec2f1c69d"
title: "Arbitrary File Download Via MSOHTMED.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_msohtmed_download.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_msohtmed_download.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "459f2f98-397b-4a4a-9f47-6a5ec2f1c69d"
  - "Arbitrary File Download Via MSOHTMED.EXE"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Arbitrary File Download Via MSOHTMED.EXE

Detects usage of "MSOHTMED" to download arbitrary files

## Metadata

- Rule ID: 459f2f98-397b-4a4a-9f47-6a5ec2f1c69d
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-19
- Modified: 2023-11-09
- Source Path: rules/windows/process_creation/proc_creation_win_msohtmed_download.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_img:
- Image|endswith: \MSOHTMED.exe
- OriginalFileName: MsoHtmEd.exe
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

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_msohtmed_download.yml)
