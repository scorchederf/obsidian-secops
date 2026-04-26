---
sigma_id: "70ed1d26-0050-4b38-a599-92c53d57d45a"
title: "Bitbucket User Login Failure"
framework: "sigma"
generated: "true"
source_path: "rules/application/bitbucket/audit/bitbucket_audit_user_login_failure_detected.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/bitbucket/audit/bitbucket_audit_user_login_failure_detected.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "bitbucket / audit"
aliases:
  - "70ed1d26-0050-4b38-a599-92c53d57d45a"
  - "Bitbucket User Login Failure"
attack_technique_ids:
  - "T1078.004"
  - "T1110"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Bitbucket User Login Failure

Detects user authentication failure events.
Please note that this rule can be noisy and it is recommended to use with correlation based on "author.name" field.

## Metadata

- Rule ID: 70ed1d26-0050-4b38-a599-92c53d57d45a
- Status: test
- Level: medium
- Author: Muhammad Faisal (@faisalusuf)
- Date: 2024-02-25
- Source Path: rules/application/bitbucket/audit/bitbucket_audit_user_login_failure_detected.yml

## Logsource

- definition: Requirements: "Advance" log level is required to receive these audit events.
- product: bitbucket
- service: audit

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078.004]]
- [[kb/attack/techniques/T1110-brute_force|T1110]]

## Detection

```yaml
selection:
  auditType.category: Authentication
  auditType.action: User login failed
condition: selection
```

## False Positives

- Legitimate user wrong password attempts.

## References

- https://confluence.atlassian.com/bitbucketserver/audit-log-events-776640423.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/bitbucket/audit/bitbucket_audit_user_login_failure_detected.yml)
