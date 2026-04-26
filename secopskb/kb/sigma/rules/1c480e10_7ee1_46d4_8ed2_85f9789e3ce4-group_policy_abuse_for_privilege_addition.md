---
sigma_id: "1c480e10-7ee1-46d4-8ed2-85f9789e3ce4"
title: "Group Policy Abuse for Privilege Addition"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_susp_group_policy_abuse_privilege_addition.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_group_policy_abuse_privilege_addition.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "medium"
logsource: "windows / security"
aliases:
  - "1c480e10-7ee1-46d4-8ed2-85f9789e3ce4"
  - "Group Policy Abuse for Privilege Addition"
attack_technique_ids:
  - "T1484.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Group Policy Abuse for Privilege Addition

Detects the first occurrence of a modification to Group Policy Object Attributes to add privileges to user accounts or use them to add users as local admins.

## Metadata

- Rule ID: 1c480e10-7ee1-46d4-8ed2-85f9789e3ce4
- Status: test
- Level: medium
- Author: Elastic, Josh Nickels, Marius Rothenbücher
- Date: 2024-09-04
- Source Path: rules/windows/builtin/security/win_security_susp_group_policy_abuse_privilege_addition.yml

## Logsource

- definition: Requirements: The "Audit Directory Service Changes" logging policy must be configured in order to receive events.
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1484-domain_or_tenant_policy_modification|T1484.001]]

## Detection

```yaml
selection:
  EventID: 5136
  AttributeLDAPDisplayName: gPCMachineExtensionNames
  AttributeValue|contains:
  - 827D319E-6EAC-11D2-A4EA-00C04F79F83A
  - 803E14A0-B4FB-11D0-A0D0-00A0C90F574B
condition: selection
```

## False Positives

- Users allowed to perform these modifications (user found in field SubjectUserName)

## References

- https://www.elastic.co/guide/en/security/current/group-policy-abuse-for-privilege-addition.html#_setup_275

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_group_policy_abuse_privilege_addition.yml)
