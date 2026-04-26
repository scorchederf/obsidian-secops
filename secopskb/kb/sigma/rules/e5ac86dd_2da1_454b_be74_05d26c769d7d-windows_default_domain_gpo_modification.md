---
sigma_id: "e5ac86dd-2da1-454b-be74-05d26c769d7d"
title: "Windows Default Domain GPO Modification"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_default_domain_gpo_modification.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_default_domain_gpo_modification.yml"
build_date: "2026-04-26 14:14:40"
status: "experimental"
level: "medium"
logsource: "windows / security"
aliases:
  - "e5ac86dd-2da1-454b-be74-05d26c769d7d"
  - "Windows Default Domain GPO Modification"
attack_technique_ids:
  - "T1484.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows Default Domain GPO Modification

Detects modifications to Default Domain or Default Domain Controllers Group Policy Objects (GPOs).
Adversaries may modify these default GPOs to deploy malicious configurations across the domain.

## Metadata

- Rule ID: e5ac86dd-2da1-454b-be74-05d26c769d7d
- Status: experimental
- Level: medium
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-11-22
- Source Path: rules/windows/builtin/security/win_security_default_domain_gpo_modification.yml

## Logsource

- definition: Enable 'Audit Directory Service Changes' in the Default Domain Controllers Policy under:
Computer Configuration -> Policies -> Windows Settings -> Security Settings -> Advanced Audit Policy Configuration -> Audit Policies -> DS Access -> Audit Directory Service Changes (Success).
Additionally, proper SACL needs to be configured on the 'CN=Policies,CN=System,DC=<domain>,DC=<tld>' container in Active Directory to capture changes to Group Policy Objects.

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1484-domain_or_tenant_policy_modification|T1484.001]]

## Detection

```yaml
selection:
  EventID: 5136
  ObjectClass: groupPolicyContainer
  ObjectDN|startswith:
  - CN={31B2F340-016D-11D2-945F-00C04FB984F9},CN=POLICIES,CN=SYSTEM
  - CN={6AC1786C-016F-11D2-945F-00C04FB984F9},CN=POLICIES,CN=SYSTEM
condition: selection
```

## False Positives

- Legitimate modifications to Default Domain or Default Domain Controllers GPOs

## References

- https://www.trendmicro.com/en_us/research/25/i/unmasking-the-gentlemen-ransomware.html
- https://adsecurity.org/?p=3377
- https://www.pentestpartners.com/security-blog/living-off-the-land-gpo-style/
- https://jgspiers.com/audit-group-policy-changes/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_default_domain_gpo_modification.yml)
