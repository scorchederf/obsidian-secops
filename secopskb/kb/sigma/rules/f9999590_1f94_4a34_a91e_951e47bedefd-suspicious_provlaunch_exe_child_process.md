---
sigma_id: "f9999590-1f94-4a34-a91e-951e47bedefd"
title: "Suspicious Provlaunch.EXE Child Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_provlaunch_susp_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_provlaunch_susp_child_process.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "f9999590-1f94-4a34-a91e-951e47bedefd"
  - "Suspicious Provlaunch.EXE Child Process"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Provlaunch.EXE Child Process

Detects suspicious child processes of "provlaunch.exe" which might indicate potential abuse to proxy execution.

## Metadata

- Rule ID: f9999590-1f94-4a34-a91e-951e47bedefd
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-08-08
- Source Path: rules/windows/process_creation/proc_creation_win_provlaunch_susp_child_process.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_parent:
  ParentImage|endswith: \provlaunch.exe
selection_child:
- Image|endswith:
  - \calc.exe
  - \cmd.exe
  - \cscript.exe
  - \mshta.exe
  - \notepad.exe
  - \powershell.exe
  - \pwsh.exe
  - \regsvr32.exe
  - \rundll32.exe
  - \wscript.exe
- Image|contains:
  - :\PerfLogs\
  - :\Temp\
  - :\Users\Public\
  - \AppData\Temp\
  - \Windows\System32\Tasks\
  - \Windows\Tasks\
  - \Windows\Temp\
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Binaries/Provlaunch/
- https://twitter.com/0gtweet/status/1674399582162153472

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_provlaunch_susp_child_process.yml)
