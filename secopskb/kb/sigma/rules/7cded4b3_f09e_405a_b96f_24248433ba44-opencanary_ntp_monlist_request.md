---
sigma_id: "7cded4b3-f09e-405a-b96f-24248433ba44"
title: "OpenCanary - NTP Monlist Request"
framework: "sigma"
generated: "true"
source_path: "rules/application/opencanary/opencanary_ntp_monlist.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/opencanary/opencanary_ntp_monlist.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "high"
logsource: "opencanary / application"
aliases:
  - "7cded4b3-f09e-405a-b96f-24248433ba44"
  - "OpenCanary - NTP Monlist Request"
attack_technique_ids:
  - "T1498"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# OpenCanary - NTP Monlist Request

Detects instances where an NTP service on an OpenCanary node has had a NTP monlist request.

## Metadata

- Rule ID: 7cded4b3-f09e-405a-b96f-24248433ba44
- Status: test
- Level: high
- Author: Security Onion Solutions
- Date: 2024-03-08
- Source Path: rules/application/opencanary/opencanary_ntp_monlist.yml

## Logsource

- category: application
- product: opencanary

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1498-network_denial_of_service|T1498]]

## Detection

```yaml
selection:
  logtype: 11001
condition: selection
```

## False Positives

- Unlikely

## References

- https://opencanary.readthedocs.io/en/latest/starting/configuration.html#services-configuration
- https://github.com/thinkst/opencanary/blob/a0896adfcaf0328cfd5829fe10d2878c7445138e/opencanary/logger.py#L52

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/opencanary/opencanary_ntp_monlist.yml)
