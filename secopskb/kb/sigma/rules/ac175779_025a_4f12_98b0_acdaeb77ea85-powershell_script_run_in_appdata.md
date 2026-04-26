---
sigma_id: "ac175779-025a-4f12-98b0-acdaeb77ea85"
title: "PowerShell Script Run in AppData"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_susp_ps_appdata.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_susp_ps_appdata.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "ac175779-025a-4f12-98b0-acdaeb77ea85"
  - "PowerShell Script Run in AppData"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PowerShell Script Run in AppData

Detects a suspicious command line execution that invokes PowerShell with reference to an AppData folder

## Metadata

- Rule ID: ac175779-025a-4f12-98b0-acdaeb77ea85
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems), Jonhnathan Ribeiro, oscd.community
- Date: 2019-01-09
- Modified: 2022-07-14
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_susp_ps_appdata.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection1:
  CommandLine|contains:
  - powershell.exe
  - \powershell
  - \pwsh
  - pwsh.exe
selection2:
  CommandLine|contains|all:
  - '/c '
  - \AppData\
  CommandLine|contains:
  - Local\
  - Roaming\
condition: all of selection*
```

## False Positives

- Administrative scripts

## References

- https://twitter.com/JohnLaTwC/status/1082851155481288706
- https://app.any.run/tasks/f87f1c4e-47e2-4c46-9cf4-31454c06ce03

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_susp_ps_appdata.yml)
