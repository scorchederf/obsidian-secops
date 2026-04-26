---
sigma_id: "16a71777-0b2e-4db7-9888-9d59cb75200b"
title: "Github Delete Action Invoked"
framework: "sigma"
generated: "true"
source_path: "rules/application/github/audit/github_delete_action_invoked.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/github/audit/github_delete_action_invoked.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "medium"
logsource: "github / audit"
aliases:
  - "16a71777-0b2e-4db7-9888-9d59cb75200b"
  - "Github Delete Action Invoked"
attack_technique_ids:
  - "T1213.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Github Delete Action Invoked

Detects delete action in the Github audit logs for codespaces, environment, project and repo.

## Metadata

- Rule ID: 16a71777-0b2e-4db7-9888-9d59cb75200b
- Status: test
- Level: medium
- Author: Muhammad Faisal (@faisalusuf)
- Date: 2023-01-19
- Source Path: rules/application/github/audit/github_delete_action_invoked.yml

## Logsource

- definition: Requirements: The audit log streaming feature must be enabled to be able to receive such logs. You can enable following the documentation here: https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise#setting-up-audit-log-streaming
- product: github
- service: audit

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1213-data_from_information_repositories|T1213.003]]

## Detection

```yaml
selection:
  action:
  - codespaces.delete
  - environment.delete
  - project.delete
  - repo.destroy
condition: selection
```

## False Positives

- Validate the deletion activity is permitted. The "actor" field need to be validated.

## References

- https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/reviewing-the-audit-log-for-your-organization#audit-log-actions

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/github/audit/github_delete_action_invoked.yml)
