---
sigma_id: "ae215552-081e-44c7-805f-be16f975c8a2"
title: "Suspicious Debugger Registration Cmdline"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_registry_install_reg_debugger_backdoor.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_registry_install_reg_debugger_backdoor.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "ae215552-081e-44c7-805f-be16f975c8a2"
  - "Suspicious Debugger Registration Cmdline"
attack_technique_ids:
  - "T1546.008"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Debugger Registration Cmdline

Detects the registration of a debugger for a program that is available in the logon screen (sticky key backdoor).

## Metadata

- Rule ID: ae215552-081e-44c7-805f-be16f975c8a2
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), oscd.community, Jonhnathan Ribeiro
- Date: 2019-09-06
- Modified: 2022-08-06
- Source Path: rules/windows/process_creation/proc_creation_win_registry_install_reg_debugger_backdoor.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.008]]

## Detection

```yaml
selection1:
  CommandLine|contains: \CurrentVersion\Image File Execution Options\
selection2:
  CommandLine|contains:
  - sethc.exe
  - utilman.exe
  - osk.exe
  - magnify.exe
  - narrator.exe
  - displayswitch.exe
  - atbroker.exe
  - HelpPane.exe
condition: all of selection*
```

## False Positives

- Unknown

## References

- https://blogs.technet.microsoft.com/jonathantrull/2016/10/03/detecting-sticky-key-backdoors/
- https://bazaar.abuse.ch/sample/6f3aa9362d72e806490a8abce245331030d1ab5ac77e400dd475748236a6cc81/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_registry_install_reg_debugger_backdoor.yml)
