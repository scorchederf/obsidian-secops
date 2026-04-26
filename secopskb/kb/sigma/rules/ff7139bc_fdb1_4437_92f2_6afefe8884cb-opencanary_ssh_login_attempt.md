---
sigma_id: "ff7139bc-fdb1-4437-92f2-6afefe8884cb"
title: "OpenCanary - SSH Login Attempt"
framework: "sigma"
generated: "true"
source_path: "rules/application/opencanary/opencanary_ssh_login_attempt.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/opencanary/opencanary_ssh_login_attempt.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "high"
logsource: "opencanary / application"
aliases:
  - "ff7139bc-fdb1-4437-92f2-6afefe8884cb"
  - "OpenCanary - SSH Login Attempt"
attack_technique_ids:
  - "T1133"
  - "T1021"
  - "T1078"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# OpenCanary - SSH Login Attempt

Detects instances where an SSH service on an OpenCanary node has had a login attempt.

## Metadata

- Rule ID: ff7139bc-fdb1-4437-92f2-6afefe8884cb
- Status: test
- Level: high
- Author: Security Onion Solutions
- Date: 2024-03-08
- Source Path: rules/application/opencanary/opencanary_ssh_login_attempt.yml

## Logsource

- category: application
- product: opencanary

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1133-external_remote_services|T1133]]
- [[kb/attack/techniques/T1021-remote_services|T1021]]
- [[kb/attack/techniques/T1078-valid_accounts|T1078]]

## Detection

```yaml
selection:
  logtype: 4002
condition: selection
```

## False Positives

- Unlikely

## References

- https://opencanary.readthedocs.io/en/latest/starting/configuration.html#services-configuration
- https://github.com/thinkst/opencanary/blob/a0896adfcaf0328cfd5829fe10d2878c7445138e/opencanary/logger.py#L52

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/opencanary/opencanary_ssh_login_attempt.yml)
