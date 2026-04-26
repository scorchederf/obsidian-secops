---
sigma_id: "02cf536a-cf21-4876-8842-4159c8aee3cc"
title: "Github Push Protection Bypass Detected"
framework: "sigma"
generated: "true"
source_path: "rules/application/github/audit/github_push_protection_bypass_detected.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/github/audit/github_push_protection_bypass_detected.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "low"
logsource: "github / audit"
aliases:
  - "02cf536a-cf21-4876-8842-4159c8aee3cc"
  - "Github Push Protection Bypass Detected"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Github Push Protection Bypass Detected

Detects when a user bypasses the push protection on a secret detected by secret scanning.

## Metadata

- Rule ID: 02cf536a-cf21-4876-8842-4159c8aee3cc
- Status: test
- Level: low
- Author: Muhammad Faisal (@faisalusuf)
- Date: 2024-03-07
- Source Path: rules/application/github/audit/github_push_protection_bypass_detected.yml

## Logsource

- definition: Requirements: The audit log streaming feature must be enabled to be able to receive such logs. You can enable following the documentation here: https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise#setting-up-audit-log-streaming
- product: github
- service: audit

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
  action|contains: secret_scanning_push_protection.bypass
condition: selection
```

## False Positives

- Allowed administrative activities.

## References

- https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/push-protection-for-repositories-and-organizations
- https://thehackernews.com/2024/03/github-rolls-out-default-secret.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/github/audit/github_push_protection_bypass_detected.yml)
