---
sigma_id: "2632954e-db1c-49cb-9936-67d1ef1d17d2"
title: "Addition of SID History to Active Directory Object"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_susp_add_sid_history.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_add_sid_history.yml"
build_date: "2026-04-26 14:14:20"
status: "stable"
level: "medium"
logsource: "windows / security"
aliases:
  - "2632954e-db1c-49cb-9936-67d1ef1d17d2"
  - "Addition of SID History to Active Directory Object"
attack_technique_ids:
  - "T1134.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Addition of SID History to Active Directory Object

An attacker can use the SID history attribute to gain additional privileges.

## Metadata

- Rule ID: 2632954e-db1c-49cb-9936-67d1ef1d17d2
- Status: stable
- Level: medium
- Author: Thomas Patzke, @atc_project (improvements)
- Date: 2017-02-19
- Source Path: rules/windows/builtin/security/win_security_susp_add_sid_history.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1134-access_token_manipulation|T1134.005]]

## Detection

```yaml
selection1:
  EventID:
  - 4765
  - 4766
selection2:
  EventID: 4738
selection3:
  SidHistory:
  - '-'
  - '%%1793'
filter_null:
  SidHistory: null
condition: selection1 or (selection2 and not selection3 and not filter_null)
```

## False Positives

- Migration of an account into a new domain

## References

- https://adsecurity.org/?p=1772

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_add_sid_history.yml)
