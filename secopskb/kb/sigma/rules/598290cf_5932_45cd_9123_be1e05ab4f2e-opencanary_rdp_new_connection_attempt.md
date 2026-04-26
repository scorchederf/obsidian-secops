---
sigma_id: "598290cf-5932-45cd-9123-be1e05ab4f2e"
title: "OpenCanary - RDP New Connection Attempt"
framework: "sigma"
generated: "true"
source_path: "rules/application/opencanary/opencanary_rdp_connection_attempt.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/opencanary/opencanary_rdp_connection_attempt.yml"
build_date: "2026-04-26 15:01:47"
status: "experimental"
level: "high"
logsource: "opencanary / application"
aliases:
  - "598290cf-5932-45cd-9123-be1e05ab4f2e"
  - "OpenCanary - RDP New Connection Attempt"
attack_technique_ids:
  - "T1133"
  - "T1021.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# OpenCanary - RDP New Connection Attempt

Detects instances where an RDP service on an OpenCanary node has had a connection attempt.

## Metadata

- Rule ID: 598290cf-5932-45cd-9123-be1e05ab4f2e
- Status: experimental
- Level: high
- Author: Marco Pedrinazzi (@pedrinazziM)
- Date: 2026-01-06
- Source Path: rules/application/opencanary/opencanary_rdp_connection_attempt.yml

## Logsource

- category: application
- product: opencanary

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1133-external_remote_services|T1133]]
- [[kb/attack/techniques/T1021-remote_services|T1021.001]]

## Detection

```yaml
selection:
  logtype: 14001
condition: selection
```

## False Positives

- Unlikely

## References

- https://opencanary.readthedocs.io/en/latest/starting/configuration.html#services-configuration
- https://github.com/thinkst/opencanary/blob/a0896adfcaf0328cfd5829fe10d2878c7445138e/opencanary/logger.py#L52

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/opencanary/opencanary_rdp_connection_attempt.yml)
