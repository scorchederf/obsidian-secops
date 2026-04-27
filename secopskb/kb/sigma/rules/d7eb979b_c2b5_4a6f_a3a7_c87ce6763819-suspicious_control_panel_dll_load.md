---
sigma_id: "d7eb979b-c2b5-4a6f-a3a7-c87ce6763819"
title: "Suspicious Control Panel DLL Load"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rundll32_susp_control_dll_load.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_susp_control_dll_load.yml"
build_date: "2026-04-27 19:13:56"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "d7eb979b-c2b5-4a6f-a3a7-c87ce6763819"
  - "Suspicious Control Panel DLL Load"
attack_technique_ids:
  - "T1218.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious Rundll32 execution from control.exe as used by Equation Group and Exploit Kits

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218011-rundll32|T1218.011: Rundll32]]

## Detection

```yaml
selection_parent:
  ParentImage|endswith: \System32\control.exe
selection_img:
- Image|endswith: \rundll32.exe
- OriginalFileName: RUNDLL32.EXE
filter:
  CommandLine|contains: Shell32.dll
condition: all of selection_* and not filter
```

## False Positives

- Unknown

## References

- https://twitter.com/rikvduijn/status/853251879320662017
- https://twitter.com/felixw3000/status/853354851128025088

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_susp_control_dll_load.yml)
