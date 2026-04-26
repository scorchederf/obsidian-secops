---
sigma_id: "f8ad2e2c-40b6-4117-84d7-20b89896ab23"
title: "Suspicious Scan Loop Network"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_network_scan_loop.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_network_scan_loop.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "f8ad2e2c-40b6-4117-84d7-20b89896ab23"
  - "Suspicious Scan Loop Network"
attack_technique_ids:
  - "T1059"
  - "T1018"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Scan Loop Network

Adversaries may attempt to get a listing of other systems by IP address, hostname, or other logical identifier on a network that may be used for Lateral Movement from the current system

## Metadata

- Rule ID: f8ad2e2c-40b6-4117-84d7-20b89896ab23
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-03-12
- Source Path: rules/windows/process_creation/proc_creation_win_susp_network_scan_loop.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]
- [[kb/attack/techniques/T1018-remote_system_discovery|T1018]]

## Detection

```yaml
selection_loop:
  CommandLine|contains:
  - 'for '
  - 'foreach '
selection_tools:
  CommandLine|contains:
  - nslookup
  - ping
condition: all of selection_*
```

## False Positives

- Legitimate script

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1018/T1018.md
- https://ss64.com/nt/for.html
- https://ss64.com/ps/foreach-object.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_network_scan_loop.yml)
