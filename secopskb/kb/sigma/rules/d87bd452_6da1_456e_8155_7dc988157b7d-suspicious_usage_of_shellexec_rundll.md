---
sigma_id: "d87bd452-6da1-456e-8155-7dc988157b7d"
title: "Suspicious Usage Of ShellExec_RunDLL"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rundll32_susp_shellexec_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_susp_shellexec_execution.yml"
build_date: "2026-04-27 19:13:57"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "d87bd452-6da1-456e-8155-7dc988157b7d"
  - "Suspicious Usage Of ShellExec_RunDLL"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious usage of the ShellExec_RunDLL function to launch other commands as seen in the the raspberry-robin attack

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_openasrundll:
  CommandLine|contains: ShellExec_RunDLL
selection_suspcli:
  CommandLine|contains:
  - \Desktop\
  - \Temp\
  - \Users\Public\
  - comspec
  - iex
  - Invoke-
  - msiexec
  - odbcconf
  - regsvr32
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://redcanary.com/blog/raspberry-robin/
- https://www.microsoft.com/en-us/security/blog/2022/10/27/raspberry-robin-worm-part-of-larger-ecosystem-facilitating-pre-ransomware-activity/
- https://github.com/SigmaHQ/sigma/issues/1009

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_susp_shellexec_execution.yml)
