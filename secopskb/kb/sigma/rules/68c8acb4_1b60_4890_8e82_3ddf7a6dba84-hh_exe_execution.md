---
sigma_id: "68c8acb4-1b60-4890-8e82-3ddf7a6dba84"
title: "HH.EXE Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hh_chm_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hh_chm_execution.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "68c8acb4-1b60-4890-8e82-3ddf7a6dba84"
  - "HH.EXE Execution"
attack_technique_ids:
  - "T1218.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# HH.EXE Execution

Detects the execution of "hh.exe" to open ".chm" files.

## Metadata

- Rule ID: 68c8acb4-1b60-4890-8e82-3ddf7a6dba84
- Status: test
- Level: low
- Author: E.M. Anhaus (originally from Atomic Blue Detections, Dan Beavin), oscd.community
- Date: 2019-10-24
- Modified: 2023-12-11
- Source Path: rules/windows/process_creation/proc_creation_win_hh_chm_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.001]]

## Detection

```yaml
selection_img:
- OriginalFileName: HH.exe
- Image|endswith: \hh.exe
selection_cli:
  CommandLine|contains: .chm
condition: all of selection_*
```

## False Positives

- False positives are expected with legitimate ".CHM"

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1218.001/T1218.001.md
- https://eqllib.readthedocs.io/en/latest/analytics/b25aa548-7937-11e9-8f5c-d46d6d62a49e.html
- https://www.zscaler.com/blogs/security-research/unintentional-leak-glimpse-attack-vectors-apt37

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hh_chm_execution.yml)
