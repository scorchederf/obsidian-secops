---
sigma_id: "f8ed0e8f-7438-4b79-85eb-f358ef2fbebd"
title: "Github Self Hosted Runner Changes Detected"
framework: "sigma"
generated: "true"
source_path: "rules/application/github/audit/github_self_hosted_runner_changes_detected.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/github/audit/github_self_hosted_runner_changes_detected.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "low"
logsource: "github / audit"
aliases:
  - "f8ed0e8f-7438-4b79-85eb-f358ef2fbebd"
  - "Github Self Hosted Runner Changes Detected"
attack_technique_ids:
  - "T1526"
  - "T1213.003"
  - "T1078.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Github Self Hosted Runner Changes Detected

A self-hosted runner is a system that you deploy and manage to execute jobs from GitHub Actions on GitHub.com.
This rule detects changes to self-hosted runners configurations in the environment. The self-hosted runner configuration changes once detected,
it should be validated from GitHub UI because the log entry may not provide full context.

## Metadata

- Rule ID: f8ed0e8f-7438-4b79-85eb-f358ef2fbebd
- Status: test
- Level: low
- Author: Muhammad Faisal (@faisalusuf)
- Date: 2023-01-27
- Source Path: rules/application/github/audit/github_self_hosted_runner_changes_detected.yml

## Logsource

- definition: Requirements: The audit log streaming feature must be enabled to be able to receive such logs. You can enable following the documentation here: https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise#setting-up-audit-log-streaming
- product: github
- service: audit

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1526-cloud_service_discovery|T1526]]
- [[kb/attack/techniques/T1213-data_from_information_repositories|T1213.003]]
- [[kb/attack/techniques/T1078-valid_accounts|T1078.004]]

## Detection

```yaml
selection:
  action:
  - org.remove_self_hosted_runner
  - org.runner_group_created
  - org.runner_group_removed
  - org.runner_group_runner_removed
  - org.runner_group_runners_added
  - org.runner_group_runners_updated
  - org.runner_group_updated
  - repo.register_self_hosted_runner
  - repo.remove_self_hosted_runner
condition: selection
```

## False Positives

- Allowed self-hosted runners changes in the environment.
- A self-hosted runner is automatically removed from GitHub if it has not connected to GitHub Actions for more than 14 days.
- An ephemeral self-hosted runner is automatically removed from GitHub if it has not connected to GitHub Actions for more than 1 day.

## References

- https://docs.github.com/en/actions/hosting-your-own-runners/about-self-hosted-runners#about-self-hosted-runners
- https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/reviewing-the-audit-log-for-your-organization#search-based-on-operation

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/github/audit/github_self_hosted_runner_changes_detected.yml)
