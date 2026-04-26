---
sigma_id: "d51694fe-484a-46ac-92d6-969e76d60d10"
title: "Access To Potentially Sensitive Sysvol Files By Uncommon Applications"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_access/file_access_win_susp_gpo_files.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_access/file_access_win_susp_gpo_files.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / file_access"
aliases:
  - "d51694fe-484a-46ac-92d6-969e76d60d10"
  - "Access To Potentially Sensitive Sysvol Files By Uncommon Applications"
attack_technique_ids:
  - "T1552.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Access To Potentially Sensitive Sysvol Files By Uncommon Applications

Detects file access requests to potentially sensitive files hosted on the Windows Sysvol share.

## Metadata

- Rule ID: d51694fe-484a-46ac-92d6-969e76d60d10
- Status: test
- Level: medium
- Author: frack113
- Date: 2023-12-21
- Modified: 2024-07-29
- Source Path: rules/windows/file/file_access/file_access_win_susp_gpo_files.yml

## Logsource

- category: file_access
- definition: Requirements: Microsoft-Windows-Kernel-File ETW provider
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.006]]

## Detection

```yaml
selection:
  FileName|startswith: \\
  FileName|contains|all:
  - \sysvol\
  - \Policies\
  FileName|endswith:
  - audit.csv
  - Files.xml
  - GptTmpl.inf
  - groups.xml
  - Registry.pol
  - Registry.xml
  - scheduledtasks.xml
  - scripts.ini
  - services.xml
filter_main_generic:
  Image|startswith:
  - C:\Program Files (x86)\
  - C:\Program Files\
  - C:\Windows\system32\
  - C:\Windows\SysWOW64\
filter_main_explorer:
  Image: C:\Windows\explorer.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://github.com/vletoux/pingcastle

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_access/file_access_win_susp_gpo_files.yml)
