---
sigma_id: "ae9c6a7c-9521-42a6-915e-5aaa8689d529"
title: "CobaltStrike Load by Rundll32"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_cobaltstrike_load_by_rundll32.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_cobaltstrike_load_by_rundll32.yml"
build_date: "2026-04-27 19:13:50"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Rundll32 can be use by Cobalt Strike with StartW function to load DLLs from the command line.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218011-rundll32|T1218.011: Rundll32]]

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
