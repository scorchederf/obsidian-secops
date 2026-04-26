---
sigma_id: "75edd216-1939-4c73-8d61-7f3a0d85b5cc"
title: "File Download Via InstallUtil.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_installutil_download.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_installutil_download.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "75edd216-1939-4c73-8d61-7f3a0d85b5cc"
  - "File Download Via InstallUtil.EXE"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# File Download Via InstallUtil.EXE

Detects use of .NET InstallUtil.exe in order to download arbitrary files. The files will be written to "%LOCALAPPDATA%\Microsoft\Windows\INetCache\IE\"

## Metadata

- Rule ID: 75edd216-1939-4c73-8d61-7f3a0d85b5cc
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-19
- Modified: 2023-11-09
- Source Path: rules/windows/process_creation/proc_creation_win_installutil_download.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_img:
- Image|endswith: \InstallUtil.exe
- OriginalFileName: InstallUtil.exe
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

- https://github.com/LOLBAS-Project/LOLBAS/pull/239

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_installutil_download.yml)
