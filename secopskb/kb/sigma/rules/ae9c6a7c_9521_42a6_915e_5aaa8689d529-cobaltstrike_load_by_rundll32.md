---
sigma_id: "ae9c6a7c-9521-42a6-915e-5aaa8689d529"
title: "CobaltStrike Load by Rundll32"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_cobaltstrike_load_by_rundll32.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_cobaltstrike_load_by_rundll32.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "ae9c6a7c-9521-42a6-915e-5aaa8689d529"
  - "CobaltStrike Load by Rundll32"
attack_technique_ids:
  - "T1218.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# CobaltStrike Load by Rundll32

Rundll32 can be use by Cobalt Strike with StartW function to load DLLs from the command line.

## Metadata

- Rule ID: ae9c6a7c-9521-42a6-915e-5aaa8689d529
- Status: test
- Level: high
- Author: Wojciech Lesicki
- Date: 2021-06-01
- Modified: 2022-09-16
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_cobaltstrike_load_by_rundll32.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

## Detection

```yaml
selection_rundll:
- Image|endswith: \rundll32.exe
- OriginalFileName: RUNDLL32.EXE
- CommandLine|contains:
  - rundll32.exe
  - 'rundll32 '
selection_params:
  CommandLine|contains: .dll
  CommandLine|endswith:
  - ' StartW'
  - ',StartW'
condition: all of selection*
```

## False Positives

- Unknown

## References

- https://www.cobaltstrike.com/help-windows-executable
- https://redcanary.com/threat-detection-report/
- https://thedfirreport.com/2020/10/18/ryuk-in-5-hours/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_cobaltstrike_load_by_rundll32.yml)
