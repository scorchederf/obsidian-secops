---
sigma_id: "f598ea0c-c25a-4f72-a219-50c44411c791"
title: "Possible Shadow Credentials Added"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_susp_possible_shadow_credentials_added.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_possible_shadow_credentials_added.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "f598ea0c-c25a-4f72-a219-50c44411c791"
  - "Possible Shadow Credentials Added"
attack_technique_ids:
  - "T1556"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Possible Shadow Credentials Added

Detects possible addition of shadow credentials to an active directory object.

## Metadata

- Rule ID: f598ea0c-c25a-4f72-a219-50c44411c791
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems), Elastic (idea)
- Date: 2022-10-17
- Source Path: rules/windows/builtin/security/win_security_susp_possible_shadow_credentials_added.yml

## Logsource

- definition: The "Audit Directory Service Changes" logging policy must be configured in order to receive events. Audit events are generated only for objects with configured system access control lists (SACLs). Audit events are generated only for objects with configured system access control lists (SACLs) and only when accessed in a manner that matches their SACL settings. This policy covers the following events ids - 5136, 5137, 5138, 5139, 5141. Note that the default policy does not cover User objects. For that a custom AuditRule need to be setup (See https://github.com/OTRF/Set-AuditRule)
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1556-modify_authentication_process|T1556]]

## Detection

```yaml
selection:
  EventID: 5136
  AttributeLDAPDisplayName: msDS-KeyCredentialLink
condition: selection
```

## False Positives

- Modifications in the msDS-KeyCredentialLink attribute can be done legitimately by the Azure AD Connect synchronization account or the ADFS service account. These accounts can be added as Exceptions. (From elastic FP section)

## References

- https://www.elastic.co/guide/en/security/8.4/potential-shadow-credentials-added-to-ad-object.html
- https://cyberstoph.org/posts/2022/03/detecting-shadow-credentials/
- https://twitter.com/SBousseaden/status/1581300963650187264?

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_possible_shadow_credentials_added.yml)
