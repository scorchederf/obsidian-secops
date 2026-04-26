---
sigma_id: "b124ddf4-778d-418e-907f-6dd3fc0d31cd"
title: "Arbitrary File Download Via PresentationHost.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_presentationhost_download.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_presentationhost_download.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "b124ddf4-778d-418e-907f-6dd3fc0d31cd"
  - "Arbitrary File Download Via PresentationHost.EXE"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Arbitrary File Download Via PresentationHost.EXE

Detects usage of "PresentationHost" which is a utility that runs ".xbap" (Browser Applications) files to download arbitrary files

## Metadata

- Rule ID: b124ddf4-778d-418e-907f-6dd3fc0d31cd
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-19
- Modified: 2023-11-09
- Source Path: rules/windows/process_creation/proc_creation_win_presentationhost_download.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_img:
- Image|endswith: \presentationhost.exe
- OriginalFileName: PresentationHost.exe
selection_cli:
  CommandLine|contains:
  - http://
  - https://
  - ftp://
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/LOLBAS-Project/LOLBAS/pull/239/files

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_presentationhost_download.yml)
