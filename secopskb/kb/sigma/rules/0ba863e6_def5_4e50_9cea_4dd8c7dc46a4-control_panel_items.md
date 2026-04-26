---
sigma_id: "0ba863e6-def5-4e50-9cea-4dd8c7dc46a4"
title: "Control Panel Items"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_control_panel_item.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_control_panel_item.yml"
build_date: "2026-04-26 15:01:44"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "0ba863e6-def5-4e50-9cea-4dd8c7dc46a4"
  - "Control Panel Items"
attack_technique_ids:
  - "T1218.002"
  - "T1546"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Control Panel Items

Detects the malicious use of a control panel item

## Metadata

- Rule ID: 0ba863e6-def5-4e50-9cea-4dd8c7dc46a4
- Status: test
- Level: high
- Author: Kyaw Min Thein, Furkan Caliskan (@caliskanfurkan_)
- Date: 2020-06-22
- Modified: 2023-10-11
- Source Path: rules/windows/process_creation/proc_creation_win_control_panel_item.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.002]]
- [[kb/attack/techniques/T1546-event_triggered_execution|T1546]]

## Detection

```yaml
selection_reg_img:
- Image|endswith: \reg.exe
- OriginalFileName: reg.exe
selection_reg_cli:
  CommandLine|contains|all:
  - add
  - CurrentVersion\Control Panel\CPLs
selection_cpl:
  CommandLine|endswith: .cpl
filter_cpl_sys:
  CommandLine|contains:
  - \System32\
  - '%System%'
  - '|C:\Windows\system32|'
filter_cpl_igfx:
  CommandLine|contains|all:
  - 'regsvr32 '
  - ' /s '
  - igfxCPL.cpl
condition: all of selection_reg_* or (selection_cpl and not 1 of filter_cpl_*)
```

## False Positives

- Unknown

## References

- https://ired.team/offensive-security/code-execution/code-execution-through-control-panel-add-ins

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_control_panel_item.yml)
