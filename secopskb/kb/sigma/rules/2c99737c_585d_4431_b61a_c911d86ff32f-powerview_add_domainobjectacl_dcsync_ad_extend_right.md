---
sigma_id: "2c99737c-585d-4431-b61a-c911d86ff32f"
title: "Powerview Add-DomainObjectAcl DCSync AD Extend Right"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_account_backdoor_dcsync_rights.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_account_backdoor_dcsync_rights.yml"
build_date: "2026-04-27 19:13:55"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "2c99737c-585d-4431-b61a-c911d86ff32f"
  - "Powerview Add-DomainObjectAcl DCSync AD Extend Right"
attack_technique_ids:
  - "T1098"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Backdooring domain object to grant the rights associated with DCSync to a regular user or machine account using Powerview\Add-DomainObjectAcl DCSync Extended Right cmdlet, will allow to re-obtain the pwd hashes of any user/computer

## Logsource

- definition: Requirements: The "Audit Directory Service Changes" logging policy must be configured in order to receive events. Audit events are generated only for objects with configured system access control lists (SACLs). Audit events are generated only for objects with configured system access control lists (SACLs) and only when accessed in a manner that matches their SACL settings. This policy covers the following events ids - 5136, 5137, 5138, 5139, 5141. Note that the default policy does not cover User objects. For that a custom AuditRule need to be setup (See https://github.com/OTRF/Set-AuditRule)
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1098-account_manipulation|T1098: Account Manipulation]]

## Detection

```yaml
selection:
  EventID: 5136
  AttributeLDAPDisplayName: ntSecurityDescriptor
  AttributeValue|contains:
  - 1131f6ad-9c07-11d1-f79f-00c04fc2dcd2
  - 1131f6aa-9c07-11d1-f79f-00c04fc2dcd2
  - 89e95b76-444d-4c62-991a-0facbeda640c
filter_main_dns_object_class:
  ObjectClass:
  - dnsNode
  - dnsZoneScope
  - dnsZone
condition: selection and not 1 of filter_main_*
```

## False Positives

- New Domain Controller computer account, check user SIDs within the value attribute of event 5136 and verify if it's a regular user or DC computer account.

## References

- https://twitter.com/menasec1/status/1111556090137903104
- https://www.specterops.io/assets/resources/an_ace_up_the_sleeve.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_account_backdoor_dcsync_rights.yml)
