---
sigma_id: "dfa03a09-8b92-4d83-8e74-f72839b1c407"
title: "Potentially Suspicious Child Processes Spawned by ConHost"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_conhost_susp_winshell_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_conhost_susp_winshell_child_process.yml"
build_date: "2026-04-26 15:01:49"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "dfa03a09-8b92-4d83-8e74-f72839b1c407"
  - "Potentially Suspicious Child Processes Spawned by ConHost"
attack_technique_ids:
  - "T1202"
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potentially Suspicious Child Processes Spawned by ConHost

Detects suspicious child processes related to Windows Shell utilities spawned by `conhost.exe`, which could indicate malicious activity using trusted system components.

## Metadata

- Rule ID: dfa03a09-8b92-4d83-8e74-f72839b1c407
- Status: experimental
- Level: high
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-02-05
- Source Path: rules/windows/process_creation/proc_creation_win_conhost_susp_winshell_child_process.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_parent:
  ParentImage|endswith: \conhost.exe
selection_child:
- Image|endswith:
  - \cmd.exe
  - \cscript.exe
  - \mshta.exe
  - \powershell_ise.exe
  - \powershell.exe
  - \pwsh.exe
  - \regsvr32.exe
  - \wscript.exe
- OriginalFileName:
  - cmd.exe
  - cscript.exe
  - mshta.exe
  - powershell_ise.exe
  - powershell.exe
  - pwsh.dll
  - regsvr32.exe
  - wscript.exe
condition: all of selection_*
```

## False Positives

- Legitimate administrative tasks using `conhost.exe` to spawn child processes such as `cmd.exe`, `powershell.exe`, or `regsvr32.exe`.

## References

- https://tria.ge/241015-l98snsyeje/behavioral2

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_conhost_susp_winshell_child_process.yml)
