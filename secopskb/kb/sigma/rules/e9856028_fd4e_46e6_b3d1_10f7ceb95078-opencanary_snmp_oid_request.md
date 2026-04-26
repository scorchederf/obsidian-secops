---
sigma_id: "e9856028-fd4e-46e6-b3d1-10f7ceb95078"
title: "OpenCanary - SNMP OID Request"
framework: "sigma"
generated: "true"
source_path: "rules/application/opencanary/opencanary_snmp_cmd.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/opencanary/opencanary_snmp_cmd.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "opencanary / application"
aliases:
  - "e9856028-fd4e-46e6-b3d1-10f7ceb95078"
  - "OpenCanary - SNMP OID Request"
attack_technique_ids:
  - "T1016"
  - "T1021"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# OpenCanary - SNMP OID Request

Detects instances where an SNMP service on an OpenCanary node has had an OID request.

## Metadata

- Rule ID: e9856028-fd4e-46e6-b3d1-10f7ceb95078
- Status: test
- Level: high
- Author: Security Onion Solutions
- Date: 2024-03-08
- Source Path: rules/application/opencanary/opencanary_snmp_cmd.yml

## Logsource

- category: application
- product: opencanary

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1016-system_network_configuration_discovery|T1016]]
- [[kb/attack/techniques/T1021-remote_services|T1021]]

## Detection

```yaml
selection:
  logtype: 13001
condition: selection
```

## False Positives

- Unlikely

## References

- https://opencanary.readthedocs.io/en/latest/starting/configuration.html#services-configuration
- https://github.com/thinkst/opencanary/blob/a0896adfcaf0328cfd5829fe10d2878c7445138e/opencanary/logger.py#L52

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/opencanary/opencanary_snmp_cmd.yml)
