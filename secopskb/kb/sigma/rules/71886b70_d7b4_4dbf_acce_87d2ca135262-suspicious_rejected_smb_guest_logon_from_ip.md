---
sigma_id: "71886b70-d7b4-4dbf-acce-87d2ca135262"
title: "Suspicious Rejected SMB Guest Logon From IP"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/smbclient/security/win_smbclient_security_susp_failed_guest_logon.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/smbclient/security/win_smbclient_security_susp_failed_guest_logon.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / smbclient-security"
aliases:
  - "71886b70-d7b4-4dbf-acce-87d2ca135262"
  - "Suspicious Rejected SMB Guest Logon From IP"
attack_technique_ids:
  - "T1110.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Rejected SMB Guest Logon From IP

Detect Attempt PrintNightmare (CVE-2021-1675) Remote code execution in Windows Spooler Service

## Metadata

- Rule ID: 71886b70-d7b4-4dbf-acce-87d2ca135262
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems), KevTheHermit, fuzzyf10w
- Date: 2021-06-30
- Modified: 2023-01-02
- Source Path: rules/windows/builtin/smbclient/security/win_smbclient_security_susp_failed_guest_logon.yml

## Logsource

- product: windows
- service: smbclient-security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1110-brute_force|T1110.001]]

## Detection

```yaml
selection:
  EventID: 31017
  UserName: ''
  ServerName|startswith: \1
condition: selection
```

## False Positives

- Account fallback reasons (after failed login with specific account)

## References

- https://twitter.com/KevTheHermit/status/1410203844064301056
- https://web.archive.org/web/20210629055600/https://github.com/hhlxf/PrintNightmare/
- https://web.archive.org/web/20210701042336/https://github.com/afwu/PrintNightmare

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/smbclient/security/win_smbclient_security_susp_failed_guest_logon.yml)
