---
sigma_id: "10227522-8429-47e6-a301-f2b2d014e7ad"
title: "Macos Remote System Discovery"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_remote_system_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_remote_system_discovery.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "informational"
logsource: "macos / process_creation"
aliases:
  - "10227522-8429-47e6-a301-f2b2d014e7ad"
  - "Macos Remote System Discovery"
attack_technique_ids:
  - "T1018"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Macos Remote System Discovery

Detects the enumeration of other remote systems.

## Metadata

- Rule ID: 10227522-8429-47e6-a301-f2b2d014e7ad
- Status: test
- Level: informational
- Author: Alejandro Ortuno, oscd.community
- Date: 2020-10-22
- Modified: 2021-11-27
- Source Path: rules/macos/process_creation/proc_creation_macos_remote_system_discovery.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1018-remote_system_discovery|T1018]]

## Detection

```yaml
selection_1:
  Image|endswith: /arp
  CommandLine|contains: -a
selection_2:
  Image|endswith: /ping
  CommandLine|contains:
  - ' 10.'
  - ' 192.168.'
  - ' 172.16.'
  - ' 172.17.'
  - ' 172.18.'
  - ' 172.19.'
  - ' 172.20.'
  - ' 172.21.'
  - ' 172.22.'
  - ' 172.23.'
  - ' 172.24.'
  - ' 172.25.'
  - ' 172.26.'
  - ' 172.27.'
  - ' 172.28.'
  - ' 172.29.'
  - ' 172.30.'
  - ' 172.31.'
  - ' 127.'
  - ' 169.254.'
condition: 1 of selection*
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1018/T1018.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_remote_system_discovery.yml)
