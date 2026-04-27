---
sigma_id: "1f1a8509-2cbb-44f5-8751-8e1571518ce2"
title: "Suspicious Splwow64 Without Params"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_splwow64_cli_anomaly.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_splwow64_cli_anomaly.yml"
build_date: "2026-04-27 19:13:57"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "1f1a8509-2cbb-44f5-8751-8e1571518ce2"
  - "Suspicious Splwow64 Without Params"
attack_technique_ids:
  - "T1202"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious Splwow64.exe process without any command line parameters

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1202-indirect_command_execution|T1202: Indirect Command Execution]]

## Detection

```yaml
selection:
  Image|endswith: \splwow64.exe
  CommandLine|endswith: splwow64.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/sbousseaden/status/1429401053229891590?s=12

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_splwow64_cli_anomaly.yml)
