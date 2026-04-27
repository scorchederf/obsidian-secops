---
sigma_id: "2fdefcb3-dbda-401e-ae23-f0db027628bc"
title: "Sticky Key Like Backdoor Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_cmd_sticky_key_like_backdoor_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_sticky_key_like_backdoor_execution.yml"
build_date: "2026-04-27 19:13:56"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the usage and installation of a backdoor that uses an option to register a malicious debugger for built-in tools that are accessible in the login screen

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution#^t1546008-accessibility-features|T1546.008: Accessibility Features]]

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
