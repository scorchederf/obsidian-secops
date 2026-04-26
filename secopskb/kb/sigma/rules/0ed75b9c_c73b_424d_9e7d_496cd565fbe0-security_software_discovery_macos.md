---
sigma_id: "0ed75b9c-c73b-424d-9e7d-496cd565fbe0"
title: "Security Software Discovery - MacOs"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_security_software_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_security_software_discovery.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "macos / process_creation"
aliases:
  - "0ed75b9c-c73b-424d-9e7d-496cd565fbe0"
  - "Security Software Discovery - MacOs"
attack_technique_ids:
  - "T1518.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Security Software Discovery - MacOs

Detects usage of system utilities (only grep for now) to discover security software discovery

## Metadata

- Rule ID: 0ed75b9c-c73b-424d-9e7d-496cd565fbe0
- Status: test
- Level: medium
- Author: Daniil Yugoslavskiy, oscd.community
- Date: 2020-10-19
- Modified: 2022-11-27
- Source Path: rules/macos/process_creation/proc_creation_macos_security_software_discovery.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1518-software_discovery|T1518.001]]

## Detection

```yaml
image:
  Image: /usr/bin/grep
selection_cli_1:
  CommandLine|contains:
  - nessusd
  - santad
  - CbDefense
  - falcond
  - td-agent
  - packetbeat
  - filebeat
  - auditbeat
  - osqueryd
  - BlockBlock
  - LuLu
selection_cli_2:
  CommandLine|contains|all:
  - Little
  - Snitch
condition: image and 1 of selection_cli_*
```

## False Positives

- Legitimate activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1518.001/T1518.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_security_software_discovery.yml)
