---
sigma_id: "d00a9a72-2c09-4459-ad03-5e0a23351e36"
title: "Suspicious LDAP-Attributes Used"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_susp_ldap_dataexchange.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_ldap_dataexchange.yml"
build_date: "2026-04-26 15:01:52"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "d00a9a72-2c09-4459-ad03-5e0a23351e36"
  - "Suspicious LDAP-Attributes Used"
attack_technique_ids:
  - "T1001.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious LDAP-Attributes Used

Detects the usage of particular AttributeLDAPDisplayNames, which are known for data exchange via LDAP by the tool LDAPFragger and are additionally not commonly used in companies.

## Metadata

- Rule ID: d00a9a72-2c09-4459-ad03-5e0a23351e36
- Status: test
- Level: high
- Author: xknow @xknow_infosec
- Date: 2019-03-24
- Modified: 2022-10-05
- Source Path: rules/windows/builtin/security/win_security_susp_ldap_dataexchange.yml

## Logsource

- definition: The "Audit Directory Service Changes" logging policy must be configured in order to receive events. Audit events are generated only for objects with configured system access control lists (SACLs). Audit events are generated only for objects with configured system access control lists (SACLs) and only when accessed in a manner that matches their SACL settings. This policy covers the following events ids - 5136, 5137, 5138, 5139, 5141. Note that the default policy does not cover User objects. For that a custom AuditRule need to be setup (See https://github.com/OTRF/Set-AuditRule)
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1001-data_obfuscation|T1001.003]]

## Detection

```yaml
selection:
  EventID: 5136
  AttributeValue|contains: '*'
  AttributeLDAPDisplayName:
  - primaryInternationalISDNNumber
  - otherFacsimileTelephoneNumber
  - primaryTelexNumber
condition: selection
```

## False Positives

- Companies, who may use these default LDAP-Attributes for personal information

## References

- https://medium.com/@ivecodoe/detecting-ldapfragger-a-newly-released-cobalt-strike-beacon-using-ldap-for-c2-communication-c274a7f00961
- https://blog.fox-it.com/2020/03/19/ldapfragger-command-and-control-over-ldap-attributes/
- https://github.com/fox-it/LDAPFragger

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_ldap_dataexchange.yml)
