---
sigma_id: "f1edd233-30b5-4823-9e6a-c4171b24d316"
title: "Rundll32 Registered COM Objects"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rundll32_registered_com_objects.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_registered_com_objects.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "f1edd233-30b5-4823-9e6a-c4171b24d316"
  - "Rundll32 Registered COM Objects"
attack_technique_ids:
  - "T1546.015"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Rundll32 Registered COM Objects

load malicious registered COM objects

## Metadata

- Rule ID: f1edd233-30b5-4823-9e6a-c4171b24d316
- Status: test
- Level: high
- Author: frack113
- Date: 2022-02-13
- Modified: 2023-02-09
- Source Path: rules/windows/process_creation/proc_creation_win_rundll32_registered_com_objects.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.015]]

## Detection

```yaml
selection_img:
- Image|endswith: \rundll32.exe
- OriginalFileName: RUNDLL32.EXE
selection_cli:
  CommandLine|contains:
  - '-sta '
  - '-localserver '
  CommandLine|contains|all:
  - '{'
  - '}'
condition: all of selection_*
```

## False Positives

- Legitimate use

## References

- https://nasbench.medium.com/a-deep-dive-into-rundll32-exe-642344b41e90
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1546.015/T1546.015.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_registered_com_objects.yml)
