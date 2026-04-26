---
sigma_id: "2267fe65-0681-42ad-9a6d-46553d3f3480"
title: "WSL Child Process Anomaly"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wsl_child_processes_anomalies.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wsl_child_processes_anomalies.yml"
build_date: "2026-04-26 14:14:39"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "2267fe65-0681-42ad-9a6d-46553d3f3480"
  - "WSL Child Process Anomaly"
attack_technique_ids:
  - "T1218"
  - "T1202"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# WSL Child Process Anomaly

Detects uncommon or suspicious child processes spawning from a WSL process. This could indicate an attempt to evade parent/child relationship detections or persistence attempts via cron using WSL

## Metadata

- Rule ID: 2267fe65-0681-42ad-9a6d-46553d3f3480
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-01-23
- Modified: 2023-08-15
- Source Path: rules/windows/process_creation/proc_creation_win_wsl_child_processes_anomalies.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]
- [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Detection

```yaml
selection_parent:
  ParentImage|endswith:
  - \wsl.exe
  - \wslhost.exe
selection_children_images:
  Image|endswith:
  - \calc.exe
  - \cmd.exe
  - \cscript.exe
  - \mshta.exe
  - \powershell.exe
  - \pwsh.exe
  - \regsvr32.exe
  - \rundll32.exe
  - \wscript.exe
selection_children_paths:
  Image|contains:
  - \AppData\Local\Temp\
  - C:\Users\Public\
  - C:\Windows\Temp\
  - C:\Temp\
  - \Downloads\
  - \Desktop\
condition: selection_parent and 1 of selection_children_*
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/OtherMSBinaries/Wsl/
- https://twitter.com/nas_bench/status/1535431474429808642

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wsl_child_processes_anomalies.yml)
