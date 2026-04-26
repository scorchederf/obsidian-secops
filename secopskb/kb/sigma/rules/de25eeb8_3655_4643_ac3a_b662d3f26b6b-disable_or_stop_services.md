---
sigma_id: "de25eeb8-3655-4643-ac3a-b662d3f26b6b"
title: "Disable Or Stop Services"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_services_stop_and_disable.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_services_stop_and_disable.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "de25eeb8-3655-4643-ac3a-b662d3f26b6b"
  - "Disable Or Stop Services"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Disable Or Stop Services

Detects the usage of utilities such as 'systemctl', 'service'...etc to stop or disable tools and services

## Metadata

- Rule ID: de25eeb8-3655-4643-ac3a-b662d3f26b6b
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-09-15
- Source Path: rules/linux/process_creation/proc_creation_lnx_services_stop_and_disable.yml

## Logsource

- category: process_creation
- product: linux

## Detection

```yaml
selection:
  Image|endswith:
  - /service
  - /systemctl
  - /chkconfig
  CommandLine|contains:
  - stop
  - disable
condition: selection
```

## False Positives

- Legitimate administration activities

## References

- https://www.trendmicro.com/pl_pl/research/20/i/the-evolution-of-malicious-shell-scripts.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_services_stop_and_disable.yml)
