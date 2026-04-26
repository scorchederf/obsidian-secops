---
sigma_id: "ca5583e9-8f80-46ac-ab91-7f314d13b984"
title: "Potentially Suspicious Child Process of KeyScrambler.exe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_keyscrambler_susp_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_keyscrambler_susp_child_process.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "ca5583e9-8f80-46ac-ab91-7f314d13b984"
  - "Potentially Suspicious Child Process of KeyScrambler.exe"
attack_technique_ids:
  - "T1203"
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potentially Suspicious Child Process of KeyScrambler.exe

Detects potentially suspicious child processes of KeyScrambler.exe

## Metadata

- Rule ID: ca5583e9-8f80-46ac-ab91-7f314d13b984
- Status: test
- Level: medium
- Author: Swachchhanda Shrawan Poudel
- Date: 2024-05-13
- Source Path: rules/windows/process_creation/proc_creation_win_keyscrambler_susp_child_process.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1203-exploitation_for_client_execution|T1203]]
- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection_parent:
  ParentImage|endswith: \KeyScrambler.exe
selection_binaries:
- Image|endswith:
  - \cmd.exe
  - \cscript.exe
  - \mshta.exe
  - \powershell.exe
  - \pwsh.exe
  - \regsvr32.exe
  - \rundll32.exe
  - \wscript.exe
- OriginalFileName:
  - Cmd.Exe
  - cscript.exe
  - mshta.exe
  - PowerShell.EXE
  - pwsh.dll
  - regsvr32.exe
  - RUNDLL32.EXE
  - wscript.exe
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://twitter.com/DTCERT/status/1712785421845790799

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_keyscrambler_susp_child_process.yml)
