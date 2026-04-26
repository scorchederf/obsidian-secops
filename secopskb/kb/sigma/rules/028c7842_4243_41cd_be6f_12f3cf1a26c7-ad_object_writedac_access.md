---
sigma_id: "028c7842-4243-41cd-be6f-12f3cf1a26c7"
title: "AD Object WriteDAC Access"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_ad_object_writedac_access.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_ad_object_writedac_access.yml"
build_date: "2026-04-26 15:01:43"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# AD Object WriteDAC Access

Detects WRITE_DAC access to a domain object

## Metadata

- Rule ID: 028c7842-4243-41cd-be6f-12f3cf1a26c7
- Status: test
- Level: critical
- Author: Roberto Rodriguez @Cyb3rWard0g
- Date: 2019-09-12
- Modified: 2021-11-27
- Source Path: rules/windows/builtin/security/win_security_ad_object_writedac_access.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1222-file_and_directory_permissions_modification|T1222.001]]

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
