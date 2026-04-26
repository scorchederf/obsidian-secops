---
sigma_id: "b7966f4a-b333-455b-8370-8ca53c229762"
title: "Dropping Of Password Filter DLL"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_reg_credential_access_via_password_filter.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_credential_access_via_password_filter.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "b7966f4a-b333-455b-8370-8ca53c229762"
  - "Dropping Of Password Filter DLL"
attack_technique_ids:
  - "T1556.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Dropping Of Password Filter DLL

Detects dropping of dll files in system32 that may be used to retrieve user credentials from LSASS

## Metadata

- Rule ID: b7966f4a-b333-455b-8370-8ca53c229762
- Status: test
- Level: medium
- Author: Sreeman
- Date: 2020-10-29
- Modified: 2022-10-09
- Source Path: rules/windows/process_creation/proc_creation_win_reg_credential_access_via_password_filter.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1556-modify_authentication_process|T1556.002]]

## Detection

```yaml
selection_cmdline:
  CommandLine|contains|all:
  - HKLM\SYSTEM\CurrentControlSet\Control\Lsa
  - scecli\0*
  - reg add
condition: selection_cmdline
```

## False Positives

- Unknown

## References

- https://pentestlab.blog/2020/02/10/credential-access-password-filter-dll/
- https://github.com/3gstudent/PasswordFilter/tree/master/PasswordFilter

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_credential_access_via_password_filter.yml)
