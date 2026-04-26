---
sigma_id: "32e19d25-4aed-4860-a55a-be99cb0bf7ed"
title: "Possible DC Shadow Attack"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_possible_dc_shadow.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_possible_dc_shadow.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / security"
aliases:
  - "32e19d25-4aed-4860-a55a-be99cb0bf7ed"
  - "Possible DC Shadow Attack"
attack_technique_ids:
  - "T1207"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Possible DC Shadow Attack

Detects DCShadow via create new SPN

## Metadata

- Rule ID: 32e19d25-4aed-4860-a55a-be99cb0bf7ed
- Status: test
- Level: medium
- Author: Ilyas Ochkov, oscd.community, Chakib Gzenayi (@Chak092), Hosni Mribah
- Date: 2019-10-25
- Modified: 2022-10-17
- Source Path: rules/windows/builtin/security/win_security_possible_dc_shadow.yml

## Logsource

- definition: The "Audit Directory Service Changes" logging policy must be configured in order to receive events. Audit events are generated only for objects with configured system access control lists (SACLs). Audit events are generated only for objects with configured system access control lists (SACLs) and only when accessed in a manner that matches their SACL settings. This policy covers the following events ids - 5136, 5137, 5138, 5139, 5141. Note that the default policy does not cover User objects. For that a custom AuditRule need to be setup (See https://github.com/OTRF/Set-AuditRule)
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1207-rogue_domain_controller|T1207]]

## Detection

```yaml
selection1:
  EventID: 4742
  ServicePrincipalNames|contains: GC/
selection2:
  EventID: 5136
  AttributeLDAPDisplayName: servicePrincipalName
  AttributeValue|startswith: GC/
condition: 1 of selection*
```

## False Positives

- Valid on domain controllers; exclude known DCs

## References

- https://twitter.com/gentilkiwi/status/1003236624925413376
- https://gist.github.com/gentilkiwi/dcc132457408cf11ad2061340dcb53c2
- https://web.archive.org/web/20180203014709/https://blog.alsid.eu/dcshadow-explained-4510f52fc19d?gi=c426ac876c48

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_possible_dc_shadow.yml)
