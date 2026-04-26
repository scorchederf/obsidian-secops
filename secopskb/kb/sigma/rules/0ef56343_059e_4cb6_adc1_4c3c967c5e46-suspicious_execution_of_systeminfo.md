---
sigma_id: "0ef56343-059e-4cb6-adc1-4c3c967c5e46"
title: "Suspicious Execution of Systeminfo"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_systeminfo_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_systeminfo_execution.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "0ef56343-059e-4cb6-adc1-4c3c967c5e46"
  - "Suspicious Execution of Systeminfo"
attack_technique_ids:
  - "T1082"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Execution of Systeminfo

Detects usage of the "systeminfo" command to retrieve information

## Metadata

- Rule ID: 0ef56343-059e-4cb6-adc1-4c3c967c5e46
- Status: test
- Level: low
- Author: frack113
- Date: 2022-01-01
- Modified: 2022-07-14
- Source Path: rules/windows/process_creation/proc_creation_win_systeminfo_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]

## Detection

```yaml
selection:
- Image|endswith: \systeminfo.exe
- OriginalFileName: sysinfo.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1082/T1082.md#atomic-test-1---system-information-discovery
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/systeminfo

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_systeminfo_execution.yml)
