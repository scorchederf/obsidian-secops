---
sigma_id: "1a9bb21a-1bb5-42d7-aa05-3219c7c8f47d"
title: "PUA - Advanced IP/Port Scanner Update Check"
framework: "sigma"
generated: "true"
source_path: "rules/web/proxy_generic/proxy_pua_advanced_ip_scanner_update_check.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_pua_advanced_ip_scanner_update_check.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "proxy"
aliases:
  - "1a9bb21a-1bb5-42d7-aa05-3219c7c8f47d"
  - "PUA - Advanced IP/Port Scanner Update Check"
attack_technique_ids:
  - "T1590"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PUA - Advanced IP/Port Scanner Update Check

Detect the update check performed by Advanced IP/Port Scanner utilities.

## Metadata

- Rule ID: 1a9bb21a-1bb5-42d7-aa05-3219c7c8f47d
- Status: test
- Level: medium
- Author: Axel Olsson
- Date: 2022-08-14
- Modified: 2024-02-15
- Source Path: rules/web/proxy_generic/proxy_pua_advanced_ip_scanner_update_check.yml

## Logsource

- category: proxy

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1590-gather_victim_network_information|T1590]]

## Detection

```yaml
selection:
  c-uri|contains: /checkupdate.php
  c-uri-query|contains|all:
  - lng=
  - ver=
  - beta=
  - type=
  - rmode=
  - product=
condition: selection
```

## False Positives

- Expected if you legitimately use the Advanced IP or Port Scanner utilities in your environement.

## References

- https://www.advanced-ip-scanner.com/
- https://www.advanced-port-scanner.com/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_pua_advanced_ip_scanner_update_check.yml)
