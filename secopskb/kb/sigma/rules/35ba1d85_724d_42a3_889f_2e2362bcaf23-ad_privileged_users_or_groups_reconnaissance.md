---
sigma_id: "35ba1d85-724d-42a3-889f-2e2362bcaf23"
title: "AD Privileged Users or Groups Reconnaissance"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_account_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_account_discovery.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "35ba1d85-724d-42a3-889f-2e2362bcaf23"
  - "AD Privileged Users or Groups Reconnaissance"
attack_technique_ids:
  - "T1087.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# AD Privileged Users or Groups Reconnaissance

Detect priv users or groups recon based on 4661 eventid and known privileged users or groups SIDs

## Metadata

- Rule ID: 35ba1d85-724d-42a3-889f-2e2362bcaf23
- Status: test
- Level: high
- Author: Samir Bousseaden
- Date: 2019-04-03
- Modified: 2022-07-13
- Source Path: rules/windows/builtin/security/win_security_account_discovery.yml

## Logsource

- definition: Requirements: enable Object Access SAM on your Domain Controllers
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1087-account_discovery|T1087.002]]

## Detection

```yaml
selection:
  EventID: 4661
  ObjectType:
  - SAM_USER
  - SAM_GROUP
selection_object:
- ObjectName|endswith:
  - '-512'
  - '-502'
  - '-500'
  - '-505'
  - '-519'
  - '-520'
  - '-544'
  - '-551'
  - '-555'
- ObjectName|contains: admin
filter:
  SubjectUserName|endswith: $
condition: selection and selection_object and not filter
```

## False Positives

- If source account name is not an admin then its super suspicious

## References

- https://web.archive.org/web/20230329163438/https://blog.menasec.net/2019/02/threat-hunting-5-detecting-enumeration.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_account_discovery.yml)
