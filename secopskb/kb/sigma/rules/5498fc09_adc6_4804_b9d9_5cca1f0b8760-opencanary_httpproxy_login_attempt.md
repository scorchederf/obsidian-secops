---
sigma_id: "5498fc09-adc6-4804-b9d9-5cca1f0b8760"
title: "OpenCanary - HTTPPROXY Login Attempt"
framework: "sigma"
generated: "true"
source_path: "rules/application/opencanary/opencanary_httpproxy_login_attempt.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/opencanary/opencanary_httpproxy_login_attempt.yml"
build_date: "2026-04-26 15:01:47"
status: "test"
level: "high"
logsource: "opencanary / application"
aliases:
  - "5498fc09-adc6-4804-b9d9-5cca1f0b8760"
  - "OpenCanary - HTTPPROXY Login Attempt"
attack_technique_ids:
  - "T1090"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# OpenCanary - HTTPPROXY Login Attempt

Detects instances where an HTTPPROXY service on an OpenCanary node has had an attempt to proxy another page.

## Metadata

- Rule ID: 5498fc09-adc6-4804-b9d9-5cca1f0b8760
- Status: test
- Level: high
- Author: Security Onion Solutions
- Date: 2024-03-08
- Source Path: rules/application/opencanary/opencanary_httpproxy_login_attempt.yml

## Logsource

- category: application
- product: opencanary

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1090-proxy|T1090]]

## Detection

```yaml
selection:
  logtype: 7001
condition: selection
```

## False Positives

- Unlikely

## References

- https://opencanary.readthedocs.io/en/latest/starting/configuration.html#services-configuration
- https://github.com/thinkst/opencanary/blob/a0896adfcaf0328cfd5829fe10d2878c7445138e/opencanary/logger.py#L52

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/opencanary/opencanary_httpproxy_login_attempt.yml)
