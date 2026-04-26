---
sigma_id: "84bae5d4-b518-4ae0-b331-6d4afd34d00f"
title: "MacOS Network Service Scanning"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_network_service_scanning.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_network_service_scanning.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "low"
logsource: "macos / process_creation"
aliases:
  - "84bae5d4-b518-4ae0-b331-6d4afd34d00f"
  - "MacOS Network Service Scanning"
attack_technique_ids:
  - "T1046"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# MacOS Network Service Scanning

Detects enumeration of local or remote network services.

## Metadata

- Rule ID: 84bae5d4-b518-4ae0-b331-6d4afd34d00f
- Status: test
- Level: low
- Author: Alejandro Ortuno, oscd.community
- Date: 2020-10-21
- Modified: 2021-11-27
- Source Path: rules/macos/process_creation/proc_creation_macos_network_service_scanning.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1046-network_service_discovery|T1046]]

## Detection

```yaml
selection_1:
  Image|endswith:
  - /nc
  - /netcat
selection_2:
  Image|endswith:
  - /nmap
  - /telnet
filter:
  CommandLine|contains: l
condition: (selection_1 and not filter) or selection_2
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1046/T1046.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_network_service_scanning.yml)
