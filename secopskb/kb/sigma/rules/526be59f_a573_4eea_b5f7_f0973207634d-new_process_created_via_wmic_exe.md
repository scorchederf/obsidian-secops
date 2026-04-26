---
sigma_id: "526be59f-a573-4eea-b5f7-f0973207634d"
title: "New Process Created Via Wmic.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wmic_process_creation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_process_creation.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "526be59f-a573-4eea-b5f7-f0973207634d"
  - "New Process Created Via Wmic.EXE"
attack_technique_ids:
  - "T1047"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New Process Created Via Wmic.EXE

Detects new process creation using WMIC via the "process call create" flag

## Metadata

- Rule ID: 526be59f-a573-4eea-b5f7-f0973207634d
- Status: test
- Level: medium
- Author: Michael Haag, Florian Roth (Nextron Systems), juju4, oscd.community
- Date: 2019-01-16
- Modified: 2023-02-14
- Source Path: rules/windows/process_creation/proc_creation_win_wmic_process_creation.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]

## Detection

```yaml
selection_img:
- Image|endswith: \wmic.exe
- OriginalFileName: wmic.exe
selection_cli:
  CommandLine|contains|all:
  - process
  - call
  - create
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://www.sans.org/blog/wmic-for-incident-response/
- https://github.com/redcanaryco/atomic-red-team/blob/84215139ee5127f8e3a117e063b604812bd71928/atomics/T1047/T1047.md#atomic-test-5---wmi-execute-local-process

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_process_creation.yml)
