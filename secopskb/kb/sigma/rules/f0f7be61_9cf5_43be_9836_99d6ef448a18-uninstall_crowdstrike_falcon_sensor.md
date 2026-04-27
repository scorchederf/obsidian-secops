---
sigma_id: "f0f7be61-9cf5-43be-9836-99d6ef448a18"
title: "Uninstall Crowdstrike Falcon Sensor"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_uninstall_crowdstrike_falcon.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uninstall_crowdstrike_falcon.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "f0f7be61-9cf5-43be-9836-99d6ef448a18"
  - "Uninstall Crowdstrike Falcon Sensor"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Uninstall Crowdstrike Falcon Sensor

Adversaries may disable security tools to avoid possible detection of their tools and activities by uninstalling Crowdstrike Falcon

## Metadata

- Rule ID: f0f7be61-9cf5-43be-9836-99d6ef448a18
- Status: test
- Level: high
- Author: frack113
- Date: 2021-07-12
- Modified: 2023-03-09
- Source Path: rules/windows/process_creation/proc_creation_win_uninstall_crowdstrike_falcon.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - \WindowsSensor.exe
  - ' /uninstall'
  - ' /quiet'
condition: selection
```

## False Positives

- Administrator might leverage the same command line for debugging or other purposes. However this action must be always investigated

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1562.001/T1562.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uninstall_crowdstrike_falcon.yml)
