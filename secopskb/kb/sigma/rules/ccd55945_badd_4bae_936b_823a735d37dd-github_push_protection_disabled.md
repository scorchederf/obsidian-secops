---
sigma_id: "ccd55945-badd-4bae-936b-823a735d37dd"
title: "Github Push Protection Disabled"
framework: "sigma"
generated: "true"
source_path: "rules/application/github/audit/github_push_protection_disabled.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/github/audit/github_push_protection_disabled.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "github / audit"
aliases:
  - "ccd55945-badd-4bae-936b-823a735d37dd"
  - "Github Push Protection Disabled"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects if the push protection feature is disabled for an organization, enterprise, repositories or custom pattern rules.

## Logsource

- definition: Requirements: The audit log streaming feature must be enabled to be able to receive such logs. You can enable following the documentation here: https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise#setting-up-audit-log-streaming
- product: github
- service: audit

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]

## Detection

```yaml
selection:
  action:
  - business_secret_scanning_custom_pattern_push_protection.disabled
  - business_secret_scanning_push_protection.disable
  - business_secret_scanning_push_protection.disabled_for_new_repos
  - org.secret_scanning_custom_pattern_push_protection_disabled
  - org.secret_scanning_push_protection_disable
  - org.secret_scanning_push_protection_new_repos_disable
  - repository_secret_scanning_custom_pattern_push_protection.disabled
condition: selection
```

## False Positives

- Allowed administrative activities.

## References

- https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/push-protection-for-repositories-and-organizations
- https://thehackernews.com/2024/03/github-rolls-out-default-secret.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/github/audit/github_push_protection_disabled.yml)
