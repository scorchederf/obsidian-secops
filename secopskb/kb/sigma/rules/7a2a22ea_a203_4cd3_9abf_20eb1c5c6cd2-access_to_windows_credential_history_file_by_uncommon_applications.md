---
sigma_id: "7a2a22ea-a203-4cd3-9abf-20eb1c5c6cd2"
title: "Access To Windows Credential History File By Uncommon Applications"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_access/file_access_win_susp_credhist.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_access/file_access_win_susp_credhist.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / file_access"
aliases:
  - "7a2a22ea-a203-4cd3-9abf-20eb1c5c6cd2"
  - "Access To Windows Credential History File By Uncommon Applications"
attack_technique_ids:
  - "T1555.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Access To Windows Credential History File By Uncommon Applications

Detects file access requests to the Windows Credential History File by an uncommon application.
This can be a sign of credential stealing. Example case would be usage of mimikatz "dpapi::credhist" function

## Metadata

- Rule ID: 7a2a22ea-a203-4cd3-9abf-20eb1c5c6cd2
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-10-17
- Modified: 2024-07-29
- Source Path: rules/windows/file/file_access/file_access_win_susp_credhist.yml

## Logsource

- category: file_access
- definition: Requirements: Microsoft-Windows-Kernel-File ETW provider
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1555-credentials_from_password_stores|T1555.004]]

## Detection

```yaml
selection:
  FileName|endswith: \Microsoft\Protect\CREDHIST
filter_main_system_folders:
  Image|startswith:
  - C:\Program Files\
  - C:\Program Files (x86)\
  - C:\Windows\system32\
  - C:\Windows\SysWOW64\
filter_main_explorer:
  Image: C:\Windows\explorer.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://tools.thehacker.recipes/mimikatz/modules/dpapi/credhist
- https://www.passcape.com/windows_password_recovery_dpapi_credhist

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_access/file_access_win_susp_credhist.yml)
