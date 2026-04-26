---
sigma_id: "eaa9ac35-1730-441f-9587-25767bde99d7"
title: "Github Outside Collaborator Detected"
framework: "sigma"
generated: "true"
source_path: "rules/application/github/audit/github_outside_collaborator_detected.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/github/audit/github_outside_collaborator_detected.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "medium"
logsource: "github / audit"
aliases:
  - "eaa9ac35-1730-441f-9587-25767bde99d7"
  - "Github Outside Collaborator Detected"
attack_technique_ids:
  - "T1098.001"
  - "T1098.003"
  - "T1213.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Github Outside Collaborator Detected

Detects when an organization member or an outside collaborator is added to or removed from a project board or has their permission level changed or when an owner removes an outside collaborator from an organization or when two-factor authentication is required in an organization and an outside collaborator does not use 2FA or disables 2FA.

## Metadata

- Rule ID: eaa9ac35-1730-441f-9587-25767bde99d7
- Status: test
- Level: medium
- Author: Muhammad Faisal (@faisalusuf)
- Date: 2023-01-20
- Source Path: rules/application/github/audit/github_outside_collaborator_detected.yml

## Logsource

- definition: Requirements: The audit log streaming feature must be enabled to be able to receive such logs. You can enable following the documentation here: https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise#setting-up-audit-log-streaming
- product: github
- service: audit

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1098-account_manipulation|T1098.001]]
- [[kb/attack/techniques/T1098-account_manipulation|T1098.003]]
- [[kb/attack/techniques/T1213-data_from_information_repositories|T1213.003]]

## Detection

```yaml
selection:
  action:
  - org.remove_outside_collaborator
  - project.update_user_permission
condition: selection
```

## False Positives

- Validate the actor if permitted to access the repo.
- Validate the Multifactor Authentication changes.

## References

- https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/reviewing-the-audit-log-for-your-organization#audit-log-actions
- https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-two-factor-authentication-for-your-organization/requiring-two-factor-authentication-in-your-organization

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/github/audit/github_outside_collaborator_detected.yml)
