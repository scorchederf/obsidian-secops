---
sigma_id: "028c7842-4243-41cd-be6f-12f3cf1a26c7"
title: "AD Object WriteDAC Access"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_ad_object_writedac_access.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_ad_object_writedac_access.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "critical"
logsource: "windows / security"
aliases:
  - "028c7842-4243-41cd-be6f-12f3cf1a26c7"
  - "AD Object WriteDAC Access"
attack_technique_ids:
  - "T1222.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects WRITE_DAC access to a domain object

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1222-file_and_directory_permissions_modification#^t1222001-windows-file-and-directory-permissions-modification|T1222.001: Windows File and Directory Permissions Modification]]

## Detection

```yaml
selection:
  EventID: 4662
  ObjectServer: DS
  AccessMask: '0x40000'
  ObjectType:
  - 19195a5b-6da0-11d0-afd3-00c04fd930c9
  - domainDNS
condition: selection
```

## False Positives

- Unknown

## References

- https://threathunterplaybook.com/hunts/windows/180815-ADObjectAccessReplication/notebook.html
- https://threathunterplaybook.com/library/windows/active_directory_replication.html
- https://threathunterplaybook.com/hunts/windows/190101-ADModDirectoryReplication/notebook.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_ad_object_writedac_access.yml)
