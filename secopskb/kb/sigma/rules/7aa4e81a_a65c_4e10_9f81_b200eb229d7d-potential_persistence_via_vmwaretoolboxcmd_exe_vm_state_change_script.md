---
sigma_id: "7aa4e81a-a65c-4e10-9f81-b200eb229d7d"
title: "Potential Persistence Via VMwareToolBoxCmd.EXE VM State Change Script"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_vmware_toolbox_cmd_persistence.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_vmware_toolbox_cmd_persistence.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "7aa4e81a-a65c-4e10-9f81-b200eb229d7d"
  - "Potential Persistence Via VMwareToolBoxCmd.EXE VM State Change Script"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Persistence Via VMwareToolBoxCmd.EXE VM State Change Script

Detects execution of the "VMwareToolBoxCmd.exe" with the "script" and "set" flag to setup a specific script to run for a specific VM state

## Metadata

- Rule ID: 7aa4e81a-a65c-4e10-9f81-b200eb229d7d
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-06-14
- Source Path: rules/windows/process_creation/proc_creation_win_vmware_toolbox_cmd_persistence.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection_img:
- Image|endswith: \VMwareToolBoxCmd.exe
- OriginalFileName: toolbox-cmd.exe
selection_cli:
  CommandLine|contains|all:
  - ' script '
  - ' set '
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://bohops.com/2021/10/08/analyzing-and-detecting-a-vmtools-persistence-technique/
- https://www.hexacorn.com/blog/2017/01/14/beyond-good-ol-run-key-part-53/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_vmware_toolbox_cmd_persistence.yml)
