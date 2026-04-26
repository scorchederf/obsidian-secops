---
sigma_id: "2fdefcb3-dbda-401e-ae23-f0db027628bc"
title: "Sticky Key Like Backdoor Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_cmd_sticky_key_like_backdoor_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_sticky_key_like_backdoor_execution.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "critical"
logsource: "windows / process_creation"
aliases:
  - "2fdefcb3-dbda-401e-ae23-f0db027628bc"
  - "Sticky Key Like Backdoor Execution"
attack_technique_ids:
  - "T1546.008"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Sticky Key Like Backdoor Execution

Detects the usage and installation of a backdoor that uses an option to register a malicious debugger for built-in tools that are accessible in the login screen

## Metadata

- Rule ID: 2fdefcb3-dbda-401e-ae23-f0db027628bc
- Status: test
- Level: critical
- Author: Florian Roth (Nextron Systems), @twjackomo, Jonhnathan Ribeiro, oscd.community
- Date: 2018-03-15
- Modified: 2023-03-07
- Source Path: rules/windows/process_creation/proc_creation_win_cmd_sticky_key_like_backdoor_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.008]]

## Detection

```yaml
selection:
  ParentImage|endswith: \winlogon.exe
  Image|endswith:
  - \cmd.exe
  - \cscript.exe
  - \mshta.exe
  - \powershell.exe
  - \pwsh.exe
  - \regsvr32.exe
  - \rundll32.exe
  - \wscript.exe
  - \wt.exe
  CommandLine|contains:
  - sethc.exe
  - utilman.exe
  - osk.exe
  - Magnify.exe
  - Narrator.exe
  - DisplaySwitch.exe
condition: selection
```

## False Positives

- Unlikely

## References

- https://learn.microsoft.com/en-us/archive/blogs/jonathantrull/detecting-sticky-key-backdoors

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_sticky_key_like_backdoor_execution.yml)
