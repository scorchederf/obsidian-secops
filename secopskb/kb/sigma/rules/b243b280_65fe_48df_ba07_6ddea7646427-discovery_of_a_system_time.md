---
sigma_id: "b243b280-65fe-48df-ba07-6ddea7646427"
title: "Discovery of a System Time"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_remote_time_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_remote_time_discovery.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "b243b280-65fe-48df-ba07-6ddea7646427"
  - "Discovery of a System Time"
attack_technique_ids:
  - "T1124"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Discovery of a System Time

Identifies use of various commands to query a systems time. This technique may be used before executing a scheduled task or to discover the time zone of a target system.

## Metadata

- Rule ID: b243b280-65fe-48df-ba07-6ddea7646427
- Status: test
- Level: low
- Author: E.M. Anhaus (originally from Atomic Blue Detections, Endgame), oscd.community
- Date: 2019-10-24
- Modified: 2022-06-28
- Source Path: rules/windows/process_creation/proc_creation_win_remote_time_discovery.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1124-system_time_discovery|T1124]]

## Detection

```yaml
selection_time:
  Image|endswith:
  - \net.exe
  - \net1.exe
  CommandLine|contains: time
selection_w32tm:
  Image|endswith: \w32tm.exe
  CommandLine|contains: tz
condition: 1 of selection_*
```

## False Positives

- Legitimate use of the system utilities to discover system time for legitimate reason

## References

- https://eqllib.readthedocs.io/en/latest/analytics/fcdb99c2-ac3c-4bde-b664-4b336329bed2.html
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1124/T1124.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_remote_time_discovery.yml)
