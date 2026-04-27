---
sigma_id: "17d619c1-e020-4347-957e-1d1207455c93"
title: "Active Directory Replication from Non Machine Account"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_ad_replication_non_machine_account.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_ad_replication_non_machine_account.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "critical"
logsource: "windows / security"
aliases:
  - "17d619c1-e020-4347-957e-1d1207455c93"
  - "Active Directory Replication from Non Machine Account"
attack_technique_ids:
  - "T1003.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Active Directory Replication from Non Machine Account

Detects potential abuse of Active Directory Replication Service (ADRS) from a non machine account to request credentials.

## Metadata

- Rule ID: 17d619c1-e020-4347-957e-1d1207455c93
- Status: test
- Level: critical
- Author: Roberto Rodriguez @Cyb3rWard0g
- Date: 2019-07-26
- Modified: 2021-11-27
- Source Path: rules/windows/builtin/security/win_security_ad_replication_non_machine_account.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.006]]

## Detection

```yaml
selection:
  EventID: 4662
  AccessMask: '0x100'
  Properties|contains:
  - 1131f6aa-9c07-11d1-f79f-00c04fc2dcd2
  - 1131f6ad-9c07-11d1-f79f-00c04fc2dcd2
  - 89e95b76-444d-4c62-991a-0facbeda640c
filter:
- SubjectUserName|endswith: $
- SubjectUserName|startswith: MSOL_
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://threathunterplaybook.com/hunts/windows/180815-ADObjectAccessReplication/notebook.html
- https://threathunterplaybook.com/library/windows/active_directory_replication.html
- https://threathunterplaybook.com/hunts/windows/190101-ADModDirectoryReplication/notebook.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_ad_replication_non_machine_account.yml)
