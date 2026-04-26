---
sigma_id: "46612ae6-86be-4802-bc07-39b59feb1309"
title: "Access To Windows DPAPI Master Keys By Uncommon Applications"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_access/file_access_win_susp_dpapi_master_key_access.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_access/file_access_win_susp_dpapi_master_key_access.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / file_access"
aliases:
  - "46612ae6-86be-4802-bc07-39b59feb1309"
  - "Access To Windows DPAPI Master Keys By Uncommon Applications"
attack_technique_ids:
  - "T1555.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Access To Windows DPAPI Master Keys By Uncommon Applications

Detects file access requests to the the Windows Data Protection API Master keys by an uncommon application.
This can be a sign of credential stealing. Example case would be usage of mimikatz "dpapi::masterkey" function

## Metadata

- Rule ID: 46612ae6-86be-4802-bc07-39b59feb1309
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-10-17
- Modified: 2024-07-29
- Source Path: rules/windows/file/file_access/file_access_win_susp_dpapi_master_key_access.yml

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
  FileName|contains:
  - \Microsoft\Protect\S-1-5-18\
  - \Microsoft\Protect\S-1-5-21-
filter_system_folders:
  Image|startswith:
  - C:\Program Files\
  - C:\Program Files (x86)\
  - C:\Windows\system32\
  - C:\Windows\SysWOW64\
condition: selection and not 1 of filter_*
```

## False Positives

- Unknown

## References

- http://blog.harmj0y.net/redteaming/operational-guidance-for-offensive-user-dpapi-abuse/
- https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation/dpapi-extracting-passwords

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_access/file_access_win_susp_dpapi_master_key_access.yml)
