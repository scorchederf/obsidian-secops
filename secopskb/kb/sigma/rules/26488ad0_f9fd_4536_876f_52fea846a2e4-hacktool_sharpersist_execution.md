---
sigma_id: "26488ad0-f9fd-4536-876f-52fea846a2e4"
title: "HackTool - SharPersist Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_sharpersist.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_sharpersist.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "26488ad0-f9fd-4536-876f-52fea846a2e4"
  - "HackTool - SharPersist Execution"
attack_technique_ids:
  - "T1053"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# HackTool - SharPersist Execution

Detects the execution of the hacktool SharPersist - used to deploy various different kinds of persistence mechanisms

## Metadata

- Rule ID: 26488ad0-f9fd-4536-876f-52fea846a2e4
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-09-15
- Modified: 2023-02-04
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_sharpersist.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053]]

## Detection

```yaml
selection_img:
- Image|endswith: \SharPersist.exe
- Product: SharPersist
selection_cli_1:
  CommandLine|contains:
  - ' -t schtask -c '
  - ' -t startupfolder -c '
selection_cli_2:
  CommandLine|contains|all:
  - ' -t reg -c '
  - ' -m add'
selection_cli_3:
  CommandLine|contains|all:
  - ' -t service -c '
  - ' -m add'
selection_cli_4:
  CommandLine|contains|all:
  - ' -t schtask -c '
  - ' -m add'
condition: 1 of selection_*
```

## False Positives

- Unknown

## References

- https://www.mandiant.com/resources/blog/sharpersist-windows-persistence-toolkit
- https://github.com/mandiant/SharPersist

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_sharpersist.yml)
