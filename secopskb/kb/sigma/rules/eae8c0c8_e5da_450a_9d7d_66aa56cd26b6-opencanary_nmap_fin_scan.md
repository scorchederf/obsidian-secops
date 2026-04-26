---
sigma_id: "eae8c0c8-e5da-450a-9d7d-66aa56cd26b6"
title: "OpenCanary - NMAP FIN Scan"
framework: "sigma"
generated: "true"
source_path: "rules/application/opencanary/opencanary_portscan_nmap_fin_scan.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/opencanary/opencanary_portscan_nmap_fin_scan.yml"
build_date: "2026-04-26 14:14:30"
status: "experimental"
level: "high"
logsource: "opencanary / application"
aliases:
  - "eae8c0c8-e5da-450a-9d7d-66aa56cd26b6"
  - "OpenCanary - NMAP FIN Scan"
attack_technique_ids:
  - "T1046"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# OpenCanary - NMAP FIN Scan

Detects instances where an OpenCanary node has been targeted by a NMAP FIN Scan

## Metadata

- Rule ID: eae8c0c8-e5da-450a-9d7d-66aa56cd26b6
- Status: experimental
- Level: high
- Author: Marco Pedrinazzi (@pedrinazziM)
- Date: 2026-01-06
- Source Path: rules/application/opencanary/opencanary_portscan_nmap_fin_scan.yml

## Logsource

- category: application
- product: opencanary

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1046-network_service_discovery|T1046]]

## Detection

```yaml
selection:
  logtype: 5005
condition: selection
```

## False Positives

- Unlikely

## References

- https://opencanary.readthedocs.io/en/latest/starting/configuration.html#services-configuration
- https://github.com/thinkst/opencanary/blob/a0896adfcaf0328cfd5829fe10d2878c7445138e/opencanary/logger.py#L52

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/opencanary/opencanary_portscan_nmap_fin_scan.yml)
