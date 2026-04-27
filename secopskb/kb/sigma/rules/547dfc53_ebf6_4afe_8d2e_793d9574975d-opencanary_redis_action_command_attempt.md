---
sigma_id: "547dfc53-ebf6-4afe-8d2e-793d9574975d"
title: "OpenCanary - REDIS Action Command Attempt"
framework: "sigma"
generated: "true"
source_path: "rules/application/opencanary/opencanary_redis_command.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/opencanary/opencanary_redis_command.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "opencanary / application"
aliases:
  - "547dfc53-ebf6-4afe-8d2e-793d9574975d"
  - "OpenCanary - REDIS Action Command Attempt"
attack_technique_ids:
  - "T1003"
  - "T1213"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# OpenCanary - REDIS Action Command Attempt

Detects instances where a REDIS service on an OpenCanary node has had an action command attempted.

## Metadata

- Rule ID: 547dfc53-ebf6-4afe-8d2e-793d9574975d
- Status: test
- Level: high
- Author: Security Onion Solutions
- Date: 2024-03-08
- Source Path: rules/application/opencanary/opencanary_redis_command.yml

## Logsource

- category: application
- product: opencanary

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003]]
- [[kb/attack/techniques/T1213-data_from_information_repositories|T1213]]

## Detection

```yaml
selection:
  logtype: 17001
condition: selection
```

## False Positives

- Unlikely

## References

- https://opencanary.readthedocs.io/en/latest/starting/configuration.html#services-configuration
- https://github.com/thinkst/opencanary/blob/a0896adfcaf0328cfd5829fe10d2878c7445138e/opencanary/logger.py#L52

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/opencanary/opencanary_redis_command.yml)
