---
sigma_id: "236d8e89-ed95-4789-a982-36f4643738ba"
title: "Suspicious Persistence Via VMwareToolBoxCmd.EXE VM State Change Script"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_vmware_toolbox_cmd_persistence_susp.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_vmware_toolbox_cmd_persistence_susp.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "236d8e89-ed95-4789-a982-36f4643738ba"
  - "Suspicious Persistence Via VMwareToolBoxCmd.EXE VM State Change Script"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Persistence Via VMwareToolBoxCmd.EXE VM State Change Script

Detects execution of the "VMwareToolBoxCmd.exe" with the "script" and "set" flag to setup a specific script that's located in a potentially suspicious location to run for a specific VM state

## Metadata

- Rule ID: 236d8e89-ed95-4789-a982-36f4643738ba
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-06-14
- Source Path: rules/windows/process_creation/proc_creation_win_vmware_toolbox_cmd_persistence_susp.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection_bin_img:
- Image|endswith: \VMwareToolBoxCmd.exe
- OriginalFileName: toolbox-cmd.exe
selection_bin_cli:
  CommandLine|contains|all:
  - ' script '
  - ' set '
selection_susp_paths:
  CommandLine|contains:
  - :\PerfLogs\
  - :\Temp\
  - :\Windows\System32\Tasks\
  - :\Windows\Tasks\
  - :\Windows\Temp\
  - \AppData\Local\Temp
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://bohops.com/2021/10/08/analyzing-and-detecting-a-vmtools-persistence-technique/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_vmware_toolbox_cmd_persistence_susp.yml)
