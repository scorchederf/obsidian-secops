---
sigma_id: "c9d8b7fd-78e4-44fe-88f6-599135d46d60"
title: "Security Software Discovery - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_security_software_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_security_software_discovery.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "low"
logsource: "linux / process_creation"
aliases:
  - "c9d8b7fd-78e4-44fe-88f6-599135d46d60"
  - "Security Software Discovery - Linux"
attack_technique_ids:
  - "T1518.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Security Software Discovery - Linux

Detects usage of system utilities (only grep and egrep for now) to discover security software discovery

## Metadata

- Rule ID: c9d8b7fd-78e4-44fe-88f6-599135d46d60
- Status: test
- Level: low
- Author: Daniil Yugoslavskiy, oscd.community
- Date: 2020-10-19
- Modified: 2022-11-27
- Source Path: rules/linux/process_creation/proc_creation_lnx_security_software_discovery.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1518-software_discovery|T1518.001]]

## Detection

```yaml
selection:
  Image|endswith:
  - /grep
  - /egrep
  CommandLine|contains:
  - nessusd
  - td-agent
  - packetbeat
  - filebeat
  - auditbeat
  - osqueryd
  - cbagentd
  - falcond
condition: selection
```

## False Positives

- Legitimate activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1518.001/T1518.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_security_software_discovery.yml)
