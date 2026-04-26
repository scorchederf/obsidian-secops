---
sigma_id: "f9405037-bc97-4eb7-baba-167dad399b83"
title: "Github New Secret Created"
framework: "sigma"
generated: "true"
source_path: "rules/application/github/audit/github_new_secret_created.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/github/audit/github_new_secret_created.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "low"
logsource: "github / audit"
aliases:
  - "f9405037-bc97-4eb7-baba-167dad399b83"
  - "Github New Secret Created"
attack_technique_ids:
  - "T1078.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Github New Secret Created

Detects when a user creates action secret for the organization, environment, codespaces or repository.

## Metadata

- Rule ID: f9405037-bc97-4eb7-baba-167dad399b83
- Status: test
- Level: low
- Author: Muhammad Faisal (@faisalusuf)
- Date: 2023-01-20
- Source Path: rules/application/github/audit/github_new_secret_created.yml

## Logsource

- definition: Requirements: The audit log streaming feature must be enabled to be able to receive such logs. You can enable following the documentation here: https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise#setting-up-audit-log-streaming
- product: github
- service: audit

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078.004]]

## Detection

```yaml
selection:
  action:
  - codespaces.create_an_org_secret
  - environment.create_actions_secret
  - org.create_actions_secret
  - repo.create_actions_secret
condition: selection
```

## False Positives

- This detection cloud be noisy depending on the environment. It is recommended to keep a check on the new secrets when created and validate the "actor".

## References

- https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/reviewing-the-audit-log-for-your-organization#audit-log-actions

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/github/audit/github_new_secret_created.yml)
