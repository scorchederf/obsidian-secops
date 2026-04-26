---
sigma_id: "dae8171c-5ec6-4396-b210-8466585b53e9"
title: "SCM Database Privileged Operation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_scm_database_privileged_operation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_scm_database_privileged_operation.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / security"
aliases:
  - "dae8171c-5ec6-4396-b210-8466585b53e9"
  - "SCM Database Privileged Operation"
attack_technique_ids:
  - "T1548"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# SCM Database Privileged Operation

Detects non-system users performing privileged operation os the SCM database

## Metadata

- Rule ID: dae8171c-5ec6-4396-b210-8466585b53e9
- Status: test
- Level: medium
- Author: Roberto Rodriguez @Cyb3rWard0g, Tim Shelton
- Date: 2019-08-15
- Modified: 2022-09-18
- Source Path: rules/windows/builtin/security/win_security_scm_database_privileged_operation.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548]]

## Detection

```yaml
selection:
  EventID: 4674
  ObjectType: SC_MANAGER OBJECT
  ObjectName: servicesactive
  PrivilegeList: SeTakeOwnershipPrivilege
filter:
  SubjectLogonId: '0x3e4'
  ProcessName|endswith: :\Windows\System32\services.exe
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://threathunterplaybook.com/hunts/windows/190826-RemoteSCMHandle/notebook.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_scm_database_privileged_operation.yml)
