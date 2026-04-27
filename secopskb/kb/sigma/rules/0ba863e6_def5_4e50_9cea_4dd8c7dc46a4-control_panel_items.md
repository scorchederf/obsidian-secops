---
sigma_id: "0ba863e6-def5-4e50-9cea-4dd8c7dc46a4"
title: "Control Panel Items"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_control_panel_item.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_control_panel_item.yml"
build_date: "2026-04-27 19:13:51"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the malicious use of a control panel item

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218002-control-panel|T1218.002: Control Panel]]
- [[kb/attack/techniques/T1546-event_triggered_execution|T1546: Event Triggered Execution]]

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
