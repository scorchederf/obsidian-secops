---
sigma_id: "b91e8d5e-0033-44fe-973f-b730316f23a1"
title: "Bitbucket Secret Scanning Exempt Repository Added"
framework: "sigma"
generated: "true"
source_path: "rules/application/bitbucket/audit/bitbucket_audit_secret_scanning_exempt_repository_detected.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/bitbucket/audit/bitbucket_audit_secret_scanning_exempt_repository_detected.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "high"
logsource: "bitbucket / audit"
aliases:
  - "b91e8d5e-0033-44fe-973f-b730316f23a1"
  - "Bitbucket Secret Scanning Exempt Repository Added"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects when a repository is exempted from secret scanning feature.

## Logsource

- definition: Requirements: "Basic" log level is required to receive these audit events.
- product: bitbucket
- service: audit

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]

## Detection

```yaml
selection:
  auditType.category: Repositories
  auditType.action: Secret scanning exempt repository added
condition: selection
```

## False Positives

- Legitimate user activity.

## References

- https://confluence.atlassian.com/bitbucketserver/audit-log-events-776640423.html
- https://confluence.atlassian.com/bitbucketserver/secret-scanning-1157471613.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/bitbucket/audit/bitbucket_audit_secret_scanning_exempt_repository_detected.yml)
