---
sigma_id: "2f575940-d85e-4ddc-af13-17dad6f1a0ef"
title: "Github SSH Certificate Configuration Changed"
framework: "sigma"
generated: "true"
source_path: "rules/application/github/audit/github_ssh_certificate_config_changed.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/github/audit/github_ssh_certificate_config_changed.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "medium"
logsource: "github / audit"
aliases:
  - "2f575940-d85e-4ddc-af13-17dad6f1a0ef"
  - "Github SSH Certificate Configuration Changed"
attack_technique_ids:
  - "T1078.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Github SSH Certificate Configuration Changed

Detects when changes are made to the SSH certificate configuration of the organization.

## Metadata

- Rule ID: 2f575940-d85e-4ddc-af13-17dad6f1a0ef
- Status: test
- Level: medium
- Author: Romain Gaillard (@romain-gaillard)
- Date: 2024-07-29
- Source Path: rules/application/github/audit/github_ssh_certificate_config_changed.yml

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
  - ssh_certificate_authority.create
  - ssh_certificate_requirement.disable
condition: selection
```

## False Positives

- Allowed administrative activities.

## References

- https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-git-access-to-your-organizations-repositories/about-ssh-certificate-authorities
- https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/audit-log-events-for-your-enterprise#ssh_certificate_authority

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/github/audit/github_ssh_certificate_config_changed.yml)
