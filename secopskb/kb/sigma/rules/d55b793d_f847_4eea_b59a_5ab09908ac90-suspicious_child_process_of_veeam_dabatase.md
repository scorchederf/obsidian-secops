---
sigma_id: "d55b793d-f847-4eea-b59a-5ab09908ac90"
title: "Suspicious Child Process Of Veeam Dabatase"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_mssql_veaam_susp_child_processes.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mssql_veaam_susp_child_processes.yml"
build_date: "2026-04-27 19:13:56"
status: "test"
level: "critical"
logsource: "windows / process_creation"
aliases:
  - "d55b793d-f847-4eea-b59a-5ab09908ac90"
  - "Suspicious Child Process Of Veeam Dabatase"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious child processes of the Veeam service process. This could indicate potential RCE or SQL Injection.

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_parent:
  ParentImage|endswith: \sqlservr.exe
  ParentCommandLine|contains: VEEAMSQL
selection_child_1:
  Image|endswith:
  - \cmd.exe
  - \powershell.exe
  - \pwsh.exe
  - \wsl.exe
  - \wt.exe
  CommandLine|contains:
  - '-ex '
  - bypass
  - cscript
  - DownloadString
  - http://
  - https://
  - mshta
  - regsvr32
  - rundll32
  - wscript
  - 'copy '
selection_child_2:
  Image|endswith:
  - \net.exe
  - \net1.exe
  - \netstat.exe
  - \nltest.exe
  - \ping.exe
  - \tasklist.exe
  - \whoami.exe
condition: selection_parent and 1 of selection_child_*
```

## References

- https://labs.withsecure.com/publications/fin7-target-veeam-servers

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mssql_veaam_susp_child_processes.yml)
