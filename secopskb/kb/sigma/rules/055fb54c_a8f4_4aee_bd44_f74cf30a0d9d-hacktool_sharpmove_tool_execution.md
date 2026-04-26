---
sigma_id: "055fb54c-a8f4-4aee-bd44-f74cf30a0d9d"
title: "HackTool - SharpMove Tool Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_sharpmove.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_sharpmove.yml"
build_date: "2026-04-26 15:01:45"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "055fb54c-a8f4-4aee-bd44-f74cf30a0d9d"
  - "HackTool - SharpMove Tool Execution"
attack_technique_ids:
  - "T1021.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - SharpMove Tool Execution

Detects the execution of SharpMove, a .NET utility performing multiple tasks such as "Task Creation", "SCM" query, VBScript execution using WMI via its PE metadata and command line options.

## Metadata

- Rule ID: 055fb54c-a8f4-4aee-bd44-f74cf30a0d9d
- Status: test
- Level: high
- Author: Luca Di Bartolomeo (CrimpSec)
- Date: 2024-01-29
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_sharpmove.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.002]]

## Detection

```yaml
selection_img:
- Image|endswith: \SharpMove.exe
- OriginalFileName: SharpMove.exe
selection_cli_computer:
  CommandLine|contains: computername=
selection_cli_actions:
  CommandLine|contains:
  - action=create
  - action=dcom
  - action=executevbs
  - action=hijackdcom
  - action=modschtask
  - action=modsvc
  - action=query
  - action=scm
  - action=startservice
  - action=taskscheduler
condition: selection_img or all of selection_cli_*
```

## False Positives

- Unknown

## References

- https://github.com/0xthirteen/SharpMove/
- https://pentestlab.blog/tag/sharpmove/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_sharpmove.yml)
