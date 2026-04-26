---
sigma_id: "3883d9a0-fd0f-440f-afbb-445a2a799bb8"
title: "Github Secret Scanning Feature Disabled"
framework: "sigma"
generated: "true"
source_path: "rules/application/github/audit/github_secret_scanning_feature_disabled.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/github/audit/github_secret_scanning_feature_disabled.yml"
build_date: "2026-04-26 15:01:44"
status: "test"
level: "high"
logsource: "github / audit"
aliases:
  - "3883d9a0-fd0f-440f-afbb-445a2a799bb8"
  - "Github Secret Scanning Feature Disabled"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Github Secret Scanning Feature Disabled

Detects if the secret scanning feature is disabled for an enterprise or repository.

## Metadata

- Rule ID: 3883d9a0-fd0f-440f-afbb-445a2a799bb8
- Status: test
- Level: high
- Author: Muhammad Faisal (@faisalusuf)
- Date: 2024-03-07
- Modified: 2024-07-19
- Source Path: rules/application/github/audit/github_secret_scanning_feature_disabled.yml

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
  action:
  - business_secret_scanning.disable
  - business_secret_scanning.disabled_for_new_repos
  - repository_secret_scanning.disable
  - secret_scanning_new_repos.disable
  - secret_scanning.disable
condition: selection
```

## False Positives

- Allowed administrative activities.

## References

- https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/about-secret-scanning

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/github/audit/github_secret_scanning_feature_disabled.yml)
