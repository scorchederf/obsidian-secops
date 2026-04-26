---
sigma_id: "42df45e7-e6e9-43b5-8f26-bec5b39cc239"
title: "System Information Discovery"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_system_info_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_system_info_discovery.yml"
build_date: "2026-04-26 14:14:37"
status: "stable"
level: "informational"
logsource: "linux / process_creation"
aliases:
  - "42df45e7-e6e9-43b5-8f26-bec5b39cc239"
  - "System Information Discovery"
attack_technique_ids:
  - "T1082"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# System Information Discovery

Detects system information discovery commands

## Metadata

- Rule ID: 42df45e7-e6e9-43b5-8f26-bec5b39cc239
- Status: stable
- Level: informational
- Author: Ömer Günal, oscd.community
- Date: 2020-10-08
- Modified: 2021-09-14
- Source Path: rules/linux/process_creation/proc_creation_lnx_system_info_discovery.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]

## Detection

```yaml
selection:
  Image|endswith:
  - /uname
  - /hostname
  - /uptime
  - /lspci
  - /dmidecode
  - /lscpu
  - /lsmod
condition: selection
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1082/T1082.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_system_info_discovery.yml)
