---
sigma_id: "512cff7a-683a-43ad-afe0-dd398e872f36"
title: "OpenCanary - Telnet Login Attempt"
framework: "sigma"
generated: "true"
source_path: "rules/application/opencanary/opencanary_telnet_login_attempt.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/opencanary/opencanary_telnet_login_attempt.yml"
build_date: "2026-04-26 15:01:47"
status: "test"
level: "high"
logsource: "opencanary / application"
aliases:
  - "512cff7a-683a-43ad-afe0-dd398e872f36"
  - "OpenCanary - Telnet Login Attempt"
attack_technique_ids:
  - "T1133"
  - "T1078"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# OpenCanary - Telnet Login Attempt

Detects instances where a Telnet service on an OpenCanary node has had a login attempt.

## Metadata

- Rule ID: 512cff7a-683a-43ad-afe0-dd398e872f36
- Status: test
- Level: high
- Author: Security Onion Solutions
- Date: 2024-03-08
- Source Path: rules/application/opencanary/opencanary_telnet_login_attempt.yml

## Logsource

- category: application
- product: opencanary

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1133-external_remote_services|T1133]]
- [[kb/attack/techniques/T1078-valid_accounts|T1078]]

## Detection

```yaml
selection:
  logtype: 6001
condition: selection
```

## False Positives

- Unlikely

## References

- https://opencanary.readthedocs.io/en/latest/starting/configuration.html#services-configuration
- https://github.com/thinkst/opencanary/blob/a0896adfcaf0328cfd5829fe10d2878c7445138e/opencanary/logger.py#L52

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/opencanary/opencanary_telnet_login_attempt.yml)
