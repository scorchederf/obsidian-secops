---
sigma_id: "9386d78a-7207-4048-9c9f-a93a7c2d1c05"
title: "Code Execution via Pcwutl.dll"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_pcwutl.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_pcwutl.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "9386d78a-7207-4048-9c9f-a93a7c2d1c05"
  - "Code Execution via Pcwutl.dll"
attack_technique_ids:
  - "T1218.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Code Execution via Pcwutl.dll

Detects launch of executable by calling the LaunchApplication function from pcwutl.dll library.

## Metadata

- Rule ID: 9386d78a-7207-4048-9c9f-a93a7c2d1c05
- Status: test
- Level: medium
- Author: Julia Fomina, oscd.community
- Date: 2020-10-05
- Modified: 2023-02-09
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_pcwutl.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

## Detection

```yaml
selection_img:
- Image|endswith: \rundll32.exe
- OriginalFileName: RUNDLL32.EXE
selection_cli:
  CommandLine|contains|all:
  - pcwutl
  - LaunchApplication
condition: all of selection_*
```

## False Positives

- Use of Program Compatibility Troubleshooter Helper

## References

- https://lolbas-project.github.io/lolbas/Libraries/Pcwutl/
- https://twitter.com/harr0ey/status/989617817849876488

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_pcwutl.yml)
