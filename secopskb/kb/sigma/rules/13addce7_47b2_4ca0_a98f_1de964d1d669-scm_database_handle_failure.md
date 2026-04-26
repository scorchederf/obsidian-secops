---
sigma_id: "13addce7-47b2-4ca0-a98f-1de964d1d669"
title: "SCM Database Handle Failure"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_scm_database_handle_failure.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_scm_database_handle_failure.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / security"
aliases:
  - "13addce7-47b2-4ca0-a98f-1de964d1d669"
  - "SCM Database Handle Failure"
attack_technique_ids:
  - "T1010"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# SCM Database Handle Failure

Detects non-system users failing to get a handle of the SCM database.

## Metadata

- Rule ID: 13addce7-47b2-4ca0-a98f-1de964d1d669
- Status: test
- Level: medium
- Author: Roberto Rodriguez @Cyb3rWard0g
- Date: 2019-08-12
- Modified: 2022-07-11
- Source Path: rules/windows/builtin/security/win_security_scm_database_handle_failure.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1010-application_window_discovery|T1010]]

## Detection

```yaml
selection:
  EventID: 4656
  ObjectType: SC_MANAGER OBJECT
  ObjectName: ServicesActive
  AccessMask: '0xf003f'
filter:
  SubjectLogonId: '0x3e4'
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://threathunterplaybook.com/hunts/windows/190826-RemoteSCMHandle/notebook.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_scm_database_handle_failure.yml)
