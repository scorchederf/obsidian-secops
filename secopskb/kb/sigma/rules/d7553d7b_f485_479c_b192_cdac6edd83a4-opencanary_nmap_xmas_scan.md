---
sigma_id: "d7553d7b-f485-479c-b192-cdac6edd83a4"
title: "OpenCanary - NMAP XMAS Scan"
framework: "sigma"
generated: "true"
source_path: "rules/application/opencanary/opencanary_portscan_nmap_xmas_scan.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/opencanary/opencanary_portscan_nmap_xmas_scan.yml"
build_date: "2026-04-27 19:13:53"
status: "experimental"
level: "high"
logsource: "opencanary / application"
aliases:
  - "d7553d7b-f485-479c-b192-cdac6edd83a4"
  - "OpenCanary - NMAP XMAS Scan"
attack_technique_ids:
  - "T1046"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects instances where an OpenCanary node has been targeted by a NMAP XMAS Scan

## Logsource

- category: application
- product: opencanary

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1046-network_service_discovery|T1046: Network Service Discovery]]

## Detection

```yaml
selection:
  logtype: 5004
condition: selection
```

## False Positives

- Unlikely

## References

- https://opencanary.readthedocs.io/en/latest/starting/configuration.html#services-configuration
- https://github.com/thinkst/opencanary/blob/a0896adfcaf0328cfd5829fe10d2878c7445138e/opencanary/logger.py#L52

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/opencanary/opencanary_portscan_nmap_xmas_scan.yml)
