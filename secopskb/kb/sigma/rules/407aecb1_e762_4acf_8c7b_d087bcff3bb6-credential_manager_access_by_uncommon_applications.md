---
sigma_id: "407aecb1-e762-4acf-8c7b-d087bcff3bb6"
title: "Credential Manager Access By Uncommon Applications"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_access/file_access_win_susp_credential_manager_access.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_access/file_access_win_susp_credential_manager_access.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "medium"
logsource: "windows / file_access"
aliases:
  - "407aecb1-e762-4acf-8c7b-d087bcff3bb6"
  - "Credential Manager Access By Uncommon Applications"
attack_technique_ids:
  - "T1003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Credential Manager Access By Uncommon Applications

Detects suspicious processes based on name and location that access the windows credential manager and vault.
Which can be a sign of credential stealing. Example case would be usage of mimikatz "dpapi::cred" function

## Metadata

- Rule ID: 407aecb1-e762-4acf-8c7b-d087bcff3bb6
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-10-11
- Modified: 2024-07-29
- Source Path: rules/windows/file/file_access/file_access_win_susp_credential_manager_access.yml

## Logsource

- category: file_access
- definition: Requirements: Microsoft-Windows-Kernel-File ETW provider
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003]]

## Detection

```yaml
selection:
  FileName|contains:
  - \AppData\Local\Microsoft\Credentials\
  - \AppData\Roaming\Microsoft\Credentials\
  - \AppData\Local\Microsoft\Vault\
  - \ProgramData\Microsoft\Vault\
filter_system_folders:
  Image|startswith:
  - C:\Program Files\
  - C:\Program Files (x86)\
  - C:\Windows\system32\
  - C:\Windows\SysWOW64\
condition: selection and not 1 of filter_*
```

## False Positives

- Legitimate software installed by the users for example in the "AppData" directory may access these files (for any reason).

## References

- https://hunter2.gitbook.io/darthsidious/privilege-escalation/mimikatz
- https://www.absolomb.com/2018-01-26-Windows-Privilege-Escalation-Guide/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_access/file_access_win_susp_credential_manager_access.yml)
