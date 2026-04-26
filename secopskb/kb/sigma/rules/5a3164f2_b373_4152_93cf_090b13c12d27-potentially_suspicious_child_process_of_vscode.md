---
sigma_id: "5a3164f2-b373-4152-93cf-090b13c12d27"
title: "Potentially Suspicious Child Process Of VsCode"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_vscode_child_processes_anomalies.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_vscode_child_processes_anomalies.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "5a3164f2-b373-4152-93cf-090b13c12d27"
  - "Potentially Suspicious Child Process Of VsCode"
attack_technique_ids:
  - "T1218"
  - "T1202"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potentially Suspicious Child Process Of VsCode

Detects uncommon or suspicious child processes spawning from a VsCode "code.exe" process. This could indicate an attempt of persistence via VsCode tasks or terminal profiles.

## Metadata

- Rule ID: 5a3164f2-b373-4152-93cf-090b13c12d27
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-01-26
- Modified: 2023-10-25
- Source Path: rules/windows/process_creation/proc_creation_win_vscode_child_processes_anomalies.yml

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
  ParentImage|endswith: \code.exe
selection_children_images:
  Image|endswith:
  - \calc.exe
  - \regsvr32.exe
  - \rundll32.exe
  - \cscript.exe
  - \wscript.exe
selection_children_cli:
  Image|endswith:
  - \powershell.exe
  - \pwsh.exe
  - \cmd.exe
  CommandLine|contains:
  - Invoke-Expressions
  - IEX
  - Invoke-Command
  - ICM
  - DownloadString
  - rundll32
  - regsvr32
  - wscript
  - cscript
selection_children_paths:
  Image|contains:
  - :\Users\Public\
  - :\Windows\Temp\
  - :\Temp\
condition: selection_parent and 1 of selection_children_*
```

## False Positives

- In development environment where VsCode is used heavily. False positives may occur when developers use task to compile or execute different types of code. Remove or add processes accordingly

## References

- https://twitter.com/nas_bench/status/1618021838407495681
- https://twitter.com/nas_bench/status/1618021415852335105

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_vscode_child_processes_anomalies.yml)
