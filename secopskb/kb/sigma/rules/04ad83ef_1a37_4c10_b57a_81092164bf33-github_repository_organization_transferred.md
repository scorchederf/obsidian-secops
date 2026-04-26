---
sigma_id: "04ad83ef-1a37-4c10-b57a-81092164bf33"
title: "Github Repository/Organization Transferred"
framework: "sigma"
generated: "true"
source_path: "rules/application/github/audit/github_repo_or_org_transferred.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/github/audit/github_repo_or_org_transferred.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "medium"
logsource: "github / audit"
aliases:
  - "04ad83ef-1a37-4c10-b57a-81092164bf33"
  - "Github Repository/Organization Transferred"
attack_technique_ids:
  - "T1020"
  - "T1537"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Github Repository/Organization Transferred

Detects when a repository or an organization is being transferred to another location.

## Metadata

- Rule ID: 04ad83ef-1a37-4c10-b57a-81092164bf33
- Status: test
- Level: medium
- Author: Romain Gaillard (@romain-gaillard)
- Date: 2024-07-29
- Source Path: rules/application/github/audit/github_repo_or_org_transferred.yml

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
  - migration.create
  - org.transfer_outgoing
  - org.transfer
  - repo.transfer_outgoing
condition: selection
```

## False Positives

- Allowed administrative activities.

## References

- https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository
- https://docs.github.com/en/organizations/managing-organization-settings/transferring-organization-ownership
- https://docs.github.com/en/migrations
- https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/audit-log-events-for-your-enterprise#migration

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/github/audit/github_repo_or_org_transferred.yml)
