---
sigma_id: "1f0f6176-6482-4027-b151-00071af39d7e"
title: "Arbitrary File Download Via ConfigSecurityPolicy.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_configsecuritypolicy_download_file.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_configsecuritypolicy_download_file.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "1f0f6176-6482-4027-b151-00071af39d7e"
  - "Arbitrary File Download Via ConfigSecurityPolicy.EXE"
attack_technique_ids:
  - "T1567"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Arbitrary File Download Via ConfigSecurityPolicy.EXE

Detects the execution of "ConfigSecurityPolicy.EXE", a binary part of Windows Defender used to manage settings in Windows Defender.
Users can configure different pilot collections for each of the co-management workloads.
It can be abused by attackers in order to upload or download files.

## Metadata

- Rule ID: 1f0f6176-6482-4027-b151-00071af39d7e
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-11-26
- Modified: 2022-05-16
- Source Path: rules/windows/process_creation/proc_creation_win_configsecuritypolicy_download_file.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1567-exfiltration_over_web_service|T1567]]

## Detection

```yaml
selection_img:
- CommandLine|contains: ConfigSecurityPolicy.exe
- Image|endswith: \ConfigSecurityPolicy.exe
- OriginalFileName: ConfigSecurityPolicy.exe
selection_url:
  CommandLine|contains:
  - ftp://
  - http://
  - https://
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Binaries/ConfigSecurityPolicy/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_configsecuritypolicy_download_file.yml)
