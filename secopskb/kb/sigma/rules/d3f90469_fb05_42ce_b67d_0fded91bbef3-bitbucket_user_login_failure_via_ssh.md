---
sigma_id: "d3f90469-fb05-42ce-b67d-0fded91bbef3"
title: "Bitbucket User Login Failure Via SSH"
framework: "sigma"
generated: "true"
source_path: "rules/application/bitbucket/audit/bitbucket_audit_user_login_failure_via_ssh_detected.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/bitbucket/audit/bitbucket_audit_user_login_failure_via_ssh_detected.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "bitbucket / audit"
aliases:
  - "d3f90469-fb05-42ce-b67d-0fded91bbef3"
  - "Bitbucket User Login Failure Via SSH"
attack_technique_ids:
  - "T1021.004"
  - "T1110"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Bitbucket User Login Failure Via SSH

Detects SSH user login access failures.
Please note that this rule can be noisy and is recommended to use with correlation based on "author.name" field.

## Metadata

- Rule ID: d3f90469-fb05-42ce-b67d-0fded91bbef3
- Status: test
- Level: medium
- Author: Muhammad Faisal (@faisalusuf)
- Date: 2024-02-25
- Source Path: rules/application/bitbucket/audit/bitbucket_audit_user_login_failure_via_ssh_detected.yml

## Logsource

- definition: Requirements: "Advance" log level is required to receive these audit events.
- product: bitbucket
- service: audit

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.004]]
- [[kb/attack/techniques/T1110-brute_force|T1110]]

## Detection

```yaml
selection:
  auditType.category: Authentication
  auditType.action: User login failed(SSH)
condition: selection
```

## False Positives

- Legitimate user wrong password attempts.

## References

- https://confluence.atlassian.com/bitbucketserver/view-and-configure-the-audit-log-776640417.html
- https://confluence.atlassian.com/bitbucketserver/enable-ssh-access-to-git-repositories-776640358.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/bitbucket/audit/bitbucket_audit_user_login_failure_via_ssh_detected.yml)
