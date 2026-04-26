---
sigma_id: "3908d64a-3c06-4091-b503-b3a94424533b"
title: "New Github Organization Member Added"
framework: "sigma"
generated: "true"
source_path: "rules/application/github/audit/github_new_org_member.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/github/audit/github_new_org_member.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "informational"
logsource: "github / audit"
aliases:
  - "3908d64a-3c06-4091-b503-b3a94424533b"
  - "New Github Organization Member Added"
attack_technique_ids:
  - "T1136.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New Github Organization Member Added

Detects when a new member is added or invited to a github organization.

## Metadata

- Rule ID: 3908d64a-3c06-4091-b503-b3a94424533b
- Status: test
- Level: informational
- Author: Muhammad Faisal (@faisalusuf)
- Date: 2023-01-29
- Source Path: rules/application/github/audit/github_new_org_member.yml

## Logsource

- definition: Requirements: The audit log streaming feature must be enabled to be able to receive such logs. You can enable following the documentation here: https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise#setting-up-audit-log-streaming
- product: github
- service: audit

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1136-create_account|T1136.003]]

## Detection

```yaml
selection:
  action:
  - org.add_member
  - org.invite_member
condition: selection
```

## False Positives

- Organization approved new members

## References

- https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/reviewing-the-audit-log-for-your-organization#dependabot_alerts-category-actions

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/github/audit/github_new_org_member.yml)
