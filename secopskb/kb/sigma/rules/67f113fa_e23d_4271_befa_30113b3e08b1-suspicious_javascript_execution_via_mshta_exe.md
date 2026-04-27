---
sigma_id: "67f113fa-e23d-4271-befa-30113b3e08b1"
title: "Suspicious JavaScript Execution Via Mshta.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_mshta_javascript.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mshta_javascript.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "67f113fa-e23d-4271-befa-30113b3e08b1"
  - "Suspicious JavaScript Execution Via Mshta.EXE"
attack_technique_ids:
  - "T1218.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious JavaScript Execution Via Mshta.EXE

Detects execution of javascript code using "mshta.exe".

## Metadata

- Rule ID: 67f113fa-e23d-4271-befa-30113b3e08b1
- Status: test
- Level: high
- Author: E.M. Anhaus (originally from Atomic Blue Detections, Endgame), oscd.community
- Date: 2019-10-24
- Modified: 2023-02-07
- Source Path: rules/windows/process_creation/proc_creation_win_mshta_javascript.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.005]]

## Detection

```yaml
selection_img:
- Image|endswith: \mshta.exe
- OriginalFileName: MSHTA.EXE
selection_cli:
  CommandLine|contains: javascript
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://eqllib.readthedocs.io/en/latest/analytics/6bc283c4-21f2-4aed-a05c-a9a3ffa95dd4.html
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1218.005/T1218.005.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mshta_javascript.yml)
