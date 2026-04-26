---
sigma_id: "5817e76f-4804-41e6-8f1d-5fa0b3ecae2d"
title: "PUA - Radmin Viewer Utility Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_radmin.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_radmin.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "5817e76f-4804-41e6-8f1d-5fa0b3ecae2d"
  - "PUA - Radmin Viewer Utility Execution"
attack_technique_ids:
  - "T1072"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PUA - Radmin Viewer Utility Execution

Detects the execution of Radmin which can be abused by an adversary to remotely control Windows machines

## Metadata

- Rule ID: 5817e76f-4804-41e6-8f1d-5fa0b3ecae2d
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-01-22
- Modified: 2023-12-11
- Source Path: rules/windows/process_creation/proc_creation_win_pua_radmin.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1072-software_deployment_tools|T1072]]

## Detection

```yaml
selection:
- Description: Radmin Viewer
- Product: Radmin Viewer
- OriginalFileName: Radmin.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1072/T1072.md
- https://www.radmin.fr/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_radmin.yml)
