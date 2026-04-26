---
sigma_id: "fabfb3a7-3ce1-4445-9c7c-3c27f1051cdd"
title: "Potential ReflectDebugger Content Execution Via WerFault.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_werfault_reflect_debugger_exec.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_werfault_reflect_debugger_exec.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "fabfb3a7-3ce1-4445-9c7c-3c27f1051cdd"
  - "Potential ReflectDebugger Content Execution Via WerFault.EXE"
attack_technique_ids:
  - "T1036"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential ReflectDebugger Content Execution Via WerFault.EXE

Detects execution of "WerFault.exe" with the "-pr" commandline flag that is used to run files stored in the ReflectDebugger key which could be used to store the path to the malware in order to masquerade the execution flow

## Metadata

- Rule ID: fabfb3a7-3ce1-4445-9c7c-3c27f1051cdd
- Status: test
- Level: medium
- Author: X__Junior (Nextron Systems)
- Date: 2023-06-30
- Source Path: rules/windows/process_creation/proc_creation_win_werfault_reflect_debugger_exec.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036]]

## Detection

```yaml
selection_img:
- Image|endswith: \WerFault.exe
- OriginalFileName: WerFault.exe
selection_cli:
  CommandLine|contains: ' -pr '
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://cocomelonc.github.io/malware/2022/11/02/malware-pers-18.html
- https://www.hexacorn.com/blog/2018/08/31/beyond-good-ol-run-key-part-85/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_werfault_reflect_debugger_exec.yml)
