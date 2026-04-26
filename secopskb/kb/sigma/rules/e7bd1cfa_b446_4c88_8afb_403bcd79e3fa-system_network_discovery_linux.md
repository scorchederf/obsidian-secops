---
sigma_id: "e7bd1cfa-b446-4c88-8afb-403bcd79e3fa"
title: "System Network Discovery - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_system_network_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_system_network_discovery.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "informational"
logsource: "linux / process_creation"
aliases:
  - "e7bd1cfa-b446-4c88-8afb-403bcd79e3fa"
  - "System Network Discovery - Linux"
attack_technique_ids:
  - "T1016"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# System Network Discovery - Linux

Detects enumeration of local network configuration

## Metadata

- Rule ID: e7bd1cfa-b446-4c88-8afb-403bcd79e3fa
- Status: test
- Level: informational
- Author: Ömer Günal and remotephone, oscd.community
- Date: 2020-10-06
- Modified: 2022-09-15
- Source Path: rules/linux/process_creation/proc_creation_lnx_system_network_discovery.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1016-system_network_configuration_discovery|T1016]]

## Detection

```yaml
selection_img:
  Image|endswith:
  - /firewall-cmd
  - /ufw
  - /iptables
  - /netstat
  - /ss
  - /ip
  - /ifconfig
  - /systemd-resolve
  - /route
selection_cli:
  CommandLine|contains: /etc/resolv.conf
condition: 1 of selection_*
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1016/T1016.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_system_network_discovery.yml)
