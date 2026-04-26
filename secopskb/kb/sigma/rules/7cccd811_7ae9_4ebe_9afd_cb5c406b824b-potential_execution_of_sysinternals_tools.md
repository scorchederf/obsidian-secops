---
sigma_id: "7cccd811-7ae9-4ebe-9afd-cb5c406b824b"
title: "Potential Execution of Sysinternals Tools"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sysinternals_eula_accepted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_eula_accepted.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "7cccd811-7ae9-4ebe-9afd-cb5c406b824b"
  - "Potential Execution of Sysinternals Tools"
attack_technique_ids:
  - "T1588.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Execution of Sysinternals Tools

Detects command lines that contain the 'accepteula' flag which could be a sign of execution of one of the Sysinternals tools

## Metadata

- Rule ID: 7cccd811-7ae9-4ebe-9afd-cb5c406b824b
- Status: test
- Level: low
- Author: Markus Neis
- Date: 2017-08-28
- Modified: 2024-03-13
- Source Path: rules/windows/process_creation/proc_creation_win_sysinternals_eula_accepted.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1588-obtain_capabilities|T1588.002]]

## Detection

```yaml
selection:
  CommandLine|contains|windash: ' -accepteula'
condition: selection
```

## False Positives

- Legitimate use of SysInternals tools
- Programs that use the same command line flag

## References

- https://twitter.com/Moti_B/status/1008587936735035392

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_eula_accepted.yml)
