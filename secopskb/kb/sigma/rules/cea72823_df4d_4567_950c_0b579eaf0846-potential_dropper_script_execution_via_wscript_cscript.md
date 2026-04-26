---
sigma_id: "cea72823-df4d-4567-950c-0b579eaf0846"
title: "Potential Dropper Script Execution Via WScript/CScript"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wscript_cscript_dropper.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wscript_cscript_dropper.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "cea72823-df4d-4567-950c-0b579eaf0846"
  - "Potential Dropper Script Execution Via WScript/CScript"
attack_technique_ids:
  - "T1059.005"
  - "T1059.007"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Dropper Script Execution Via WScript/CScript

Detects wscript/cscript executions of scripts located in user directories

## Metadata

- Rule ID: cea72823-df4d-4567-950c-0b579eaf0846
- Status: test
- Level: medium
- Author: Margaritis Dimitrios (idea), Florian Roth (Nextron Systems), oscd.community, Nasreddine Bencherchali (Nextron Systems)
- Date: 2019-01-16
- Modified: 2024-01-30
- Source Path: rules/windows/process_creation/proc_creation_win_wscript_cscript_dropper.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.005]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.007]]

## Detection

```yaml
selection_exec:
  Image|endswith:
  - \wscript.exe
  - \cscript.exe
selection_paths:
  CommandLine|contains:
  - :\Temp\
  - :\Tmp\
  - :\Users\Public\
  - :\Windows\Temp\
  - \AppData\Local\Temp\
selection_ext:
  CommandLine|contains:
  - .js
  - .jse
  - .vba
  - .vbe
  - .vbs
  - .wsf
condition: all of selection_*
```

## False Positives

- Some installers might generate a similar behavior. An initial baseline is required

## References

- https://thedfirreport.com/2023/10/30/netsupport-intrusion-results-in-domain-compromise/
- https://redcanary.com/blog/gootloader/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wscript_cscript_dropper.yml)
