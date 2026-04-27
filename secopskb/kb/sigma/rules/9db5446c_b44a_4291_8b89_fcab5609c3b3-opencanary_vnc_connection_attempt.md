---
sigma_id: "9db5446c-b44a-4291-8b89-fcab5609c3b3"
title: "OpenCanary - VNC Connection Attempt"
framework: "sigma"
generated: "true"
source_path: "rules/application/opencanary/opencanary_vnc_connection_attempt.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/opencanary/opencanary_vnc_connection_attempt.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "opencanary / application"
aliases:
  - "9db5446c-b44a-4291-8b89-fcab5609c3b3"
  - "OpenCanary - VNC Connection Attempt"
attack_technique_ids:
  - "T1021"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# OpenCanary - VNC Connection Attempt

Detects instances where a VNC service on an OpenCanary node has had a connection attempt.

## Metadata

- Rule ID: 9db5446c-b44a-4291-8b89-fcab5609c3b3
- Status: test
- Level: high
- Author: Security Onion Solutions
- Date: 2024-03-08
- Source Path: rules/application/opencanary/opencanary_vnc_connection_attempt.yml

## Logsource

- category: application
- product: opencanary

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021]]

## Detection

```yaml
selection:
  logtype: 12001
condition: selection
```

## False Positives

- Unlikely

## References

- https://opencanary.readthedocs.io/en/latest/starting/configuration.html#services-configuration
- https://github.com/thinkst/opencanary/blob/a0896adfcaf0328cfd5829fe10d2878c7445138e/opencanary/logger.py#L52

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/opencanary/opencanary_vnc_connection_attempt.yml)
