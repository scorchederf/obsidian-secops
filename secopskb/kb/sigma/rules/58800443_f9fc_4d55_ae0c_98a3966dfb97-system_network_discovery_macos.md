---
sigma_id: "58800443-f9fc-4d55-ae0c-98a3966dfb97"
title: "System Network Discovery - macOS"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_susp_system_network_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_susp_system_network_discovery.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "informational"
logsource: "macos / process_creation"
aliases:
  - "58800443-f9fc-4d55-ae0c-98a3966dfb97"
  - "System Network Discovery - macOS"
attack_technique_ids:
  - "T1016"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# System Network Discovery - macOS

Detects enumeration of local network configuration

## Metadata

- Rule ID: 58800443-f9fc-4d55-ae0c-98a3966dfb97
- Status: test
- Level: informational
- Author: remotephone, oscd.community
- Date: 2020-10-06
- Modified: 2024-08-29
- Source Path: rules/macos/process_creation/proc_creation_macos_susp_system_network_discovery.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1016-system_network_configuration_discovery|T1016]]

## Detection

```yaml
selection_1:
  Image|endswith:
  - /arp
  - /ifconfig
  - /netstat
  - /networksetup
  - /socketfilterfw
selection_2:
  Image: /usr/bin/defaults
  CommandLine|contains|all:
  - /Library/Preferences/com.apple.alf
  - read
filter_main_wifivelocityd:
  ParentImage|endswith: /wifivelocityd
condition: 1 of selection_* and not 1 of filter_main_*
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1016/T1016.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_susp_system_network_discovery.yml)
