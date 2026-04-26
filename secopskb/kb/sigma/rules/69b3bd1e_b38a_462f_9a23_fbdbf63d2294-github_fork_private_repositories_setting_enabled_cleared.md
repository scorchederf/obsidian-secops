---
sigma_id: "69b3bd1e-b38a-462f-9a23-fbdbf63d2294"
title: "Github Fork Private Repositories Setting Enabled/Cleared"
framework: "sigma"
generated: "true"
source_path: "rules/application/github/audit/github_fork_private_repos_enabled_or_cleared.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/github/audit/github_fork_private_repos_enabled_or_cleared.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "medium"
logsource: "github / audit"
aliases:
  - "69b3bd1e-b38a-462f-9a23-fbdbf63d2294"
  - "Github Fork Private Repositories Setting Enabled/Cleared"
attack_technique_ids:
  - "T1020"
  - "T1537"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Github Fork Private Repositories Setting Enabled/Cleared

Detects when the policy allowing forks of private and internal repositories is changed (enabled or cleared).

## Metadata

- Rule ID: 69b3bd1e-b38a-462f-9a23-fbdbf63d2294
- Status: test
- Level: medium
- Author: Romain Gaillard (@romain-gaillard)
- Date: 2024-07-29
- Source Path: rules/application/github/audit/github_fork_private_repos_enabled_or_cleared.yml

## Logsource

- definition: Requirements: The audit log streaming feature must be enabled to be able to receive such logs. You can enable following the documentation here: https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise#setting-up-audit-log-streaming
- product: github
- service: audit

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1020-automated_exfiltration|T1020]]
- [[kb/attack/techniques/T1537-transfer_data_to_cloud_account|T1537]]

## Detection

```yaml
selection:
  action:
  - private_repository_forking.clear
  - private_repository_forking.enable
condition: selection
```

## False Positives

- Allowed administrative activities.

## References

- https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/audit-log-events-for-your-enterprise#private_repository_forking

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/github/audit/github_fork_private_repos_enabled_or_cleared.yml)
