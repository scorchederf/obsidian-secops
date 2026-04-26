---
sigma_id: "b6676963-0353-4f88-90f5-36c20d443c6a"
title: "Cscript/Wscript Potentially Suspicious Child Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wscript_cscript_susp_child_processes.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wscript_cscript_susp_child_processes.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "b6676963-0353-4f88-90f5-36c20d443c6a"
  - "Cscript/Wscript Potentially Suspicious Child Process"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Cscript/Wscript Potentially Suspicious Child Process

Detects potentially suspicious child processes of Wscript/Cscript. These include processes such as rundll32 with uncommon exports or PowerShell spawning rundll32 or regsvr32.
Malware such as Pikabot and Qakbot were seen using similar techniques as well as many others.

## Metadata

- Rule ID: b6676963-0353-4f88-90f5-36c20d443c6a
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), Alejandro Houspanossian ('@lekz86')
- Date: 2023-05-15
- Modified: 2024-01-02
- Source Path: rules/windows/process_creation/proc_creation_win_wscript_cscript_susp_child_processes.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_parent:
  ParentImage|endswith:
  - \wscript.exe
  - \cscript.exe
selection_cli_script_main:
  Image|endswith:
  - \cmd.exe
  - \powershell.exe
  - \pwsh.exe
selection_cli_script_option_mshta:
  CommandLine|contains|all:
  - mshta
  - http
selection_cli_script_option_other:
  CommandLine|contains:
  - rundll32
  - regsvr32
  - msiexec
selection_cli_standalone:
  Image|endswith: \rundll32.exe
filter_main_rundll32_known_exports:
  Image|endswith: \rundll32.exe
  CommandLine|contains:
  - UpdatePerUserSystemParameters
  - PrintUIEntry
  - ClearMyTracksByProcess
condition: selection_parent and ( selection_cli_standalone or (selection_cli_script_main
  and 1 of selection_cli_script_option_*) ) and not 1 of filter_main_*
```

## False Positives

- Some false positives might occur with admin or third party software scripts. Investigate and apply additional filters accordingly.

## References

- Internal Research
- https://github.com/pr0xylife/Pikabot/blob/fc58126127adf0f65e78f4eec59675523f48f086/Pikabot_30.10.2023.txt
- https://github.com/pr0xylife/Pikabot/blob/fc58126127adf0f65e78f4eec59675523f48f086/Pikabot_22.12.2023.txt

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wscript_cscript_susp_child_processes.yml)
