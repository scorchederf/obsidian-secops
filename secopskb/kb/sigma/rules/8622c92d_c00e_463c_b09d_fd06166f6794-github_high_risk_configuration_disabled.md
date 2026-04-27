---
sigma_id: "8622c92d-c00e-463c-b09d-fd06166f6794"
title: "Github High Risk Configuration Disabled"
framework: "sigma"
generated: "true"
source_path: "rules/application/github/audit/github_disable_high_risk_configuration.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/github/audit/github_disable_high_risk_configuration.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "github / audit"
aliases:
  - "8622c92d-c00e-463c-b09d-fd06166f6794"
  - "Github High Risk Configuration Disabled"
attack_technique_ids:
  - "T1556"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects when a user disables a critical security feature for an organization.

## Logsource

- definition: Requirements: The audit log streaming feature must be enabled to be able to receive such logs. You can enable following the documentation here: https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise#setting-up-audit-log-streaming
- product: github
- service: audit

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1556-modify_authentication_process|T1556: Modify Authentication Process]]

## Detection

```yaml
selection:
  action:
  - business_advanced_security.disabled_for_new_repos
  - business_advanced_security.disabled_for_new_user_namespace_repos
  - business_advanced_security.disabled
  - business_advanced_security.user_namespace_repos_disabled
  - org.advanced_security_disabled_for_new_repos
  - org.advanced_security_disabled_on_all_repos
  - org.advanced_security_policy_selected_member_disabled
  - org.disable_oauth_app_restrictions
  - org.disable_two_factor_requirement
  - repo.advanced_security_disabled
condition: selection
```

## False Positives

- Approved administrator/owner activities.

## References

- https://docs.github.com/en/organizations/managing-oauth-access-to-your-organizations-data/disabling-oauth-app-access-restrictions-for-your-organization
- https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/reviewing-the-audit-log-for-your-organization#dependabot_alerts-category-actions
- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-security-and-analysis-settings-for-your-repository
- https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/audit-log-events-for-your-enterprise

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/github/audit/github_disable_high_risk_configuration.yml)
