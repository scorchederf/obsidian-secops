---
sigma_id: "af1ac430-df6b-4b38-b976-0b52f07a0252"
title: "OpenCanary - HTTP POST Login Attempt"
framework: "sigma"
generated: "true"
source_path: "rules/application/opencanary/opencanary_http_post_login_attempt.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/opencanary/opencanary_http_post_login_attempt.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "opencanary / application"
aliases:
  - "af1ac430-df6b-4b38-b976-0b52f07a0252"
  - "OpenCanary - HTTP POST Login Attempt"
attack_technique_ids:
  - "T1190"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects instances where an HTTP service on an OpenCanary node has had login attempt via Form POST.

## Logsource

- category: application
- product: opencanary

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1190-exploit_public-facing_application|T1190: Exploit Public-Facing Application]]

## Detection

```yaml
selection:
  logtype: 3001
condition: selection
```

## False Positives

- Unlikely

## References

- https://opencanary.readthedocs.io/en/latest/starting/configuration.html#services-configuration
- https://github.com/thinkst/opencanary/blob/a0896adfcaf0328cfd5829fe10d2878c7445138e/opencanary/logger.py#L52

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/opencanary/opencanary_http_post_login_attempt.yml)
