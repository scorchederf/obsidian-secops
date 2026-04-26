---
sigma_id: "300bac00-e041-4ee2-9c36-e262656a6ecc"
title: "Active Directory User Backdoors"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_alert_ad_user_backdoors.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_alert_ad_user_backdoors.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "300bac00-e041-4ee2-9c36-e262656a6ecc"
  - "Active Directory User Backdoors"
attack_technique_ids:
  - "T1098"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Active Directory User Backdoors

Detects scenarios where one can control another users or computers account without having to use their credentials.

## Metadata

- Rule ID: 300bac00-e041-4ee2-9c36-e262656a6ecc
- Status: test
- Level: high
- Author: @neu5ron
- Date: 2017-04-13
- Modified: 2024-02-26
- Source Path: rules/windows/builtin/security/win_security_alert_ad_user_backdoors.yml

## Logsource

- definition: Requirements: Audit Policy : Account Management > Audit User Account Management, Group Policy : Computer Configuration\Windows Settings\Security Settings\Advanced Audit Policy Configuration\Audit Policies\Account Management\Audit User Account Management, DS Access > Audit Directory Service Changes, Group Policy : Computer Configuration\Windows Settings\Security Settings\Advanced Audit Policy Configuration\Audit Policies\DS Access\Audit Directory Service Changes
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1098-account_manipulation|T1098]]

## Detection

```yaml
selection1:
  EventID: 4738
filter_empty:
  AllowedToDelegateTo:
  - ''
  - '-'
filter_null:
  AllowedToDelegateTo: null
selection_5136_1:
  EventID: 5136
  AttributeLDAPDisplayName: msDS-AllowedToDelegateTo
selection_5136_2:
  EventID: 5136
  ObjectClass: user
  AttributeLDAPDisplayName: servicePrincipalName
selection_5136_3:
  EventID: 5136
  AttributeLDAPDisplayName: msDS-AllowedToActOnBehalfOfOtherIdentity
condition: (selection1 and not 1 of filter_*) or 1 of selection_5136_*
```

## False Positives

- Unknown

## References

- https://msdn.microsoft.com/en-us/library/cc220234.aspx
- https://adsecurity.org/?p=3466
- https://blog.harmj0y.net/redteaming/another-word-on-delegation/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_alert_ad_user_backdoors.yml)
