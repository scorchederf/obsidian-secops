---
sigma_id: "69bd9b97-2be2-41b6-9816-fb08757a4d1a"
title: "Potentially Suspicious Execution From Parent Process In Public Folder"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_execution_from_public_folder_as_parent.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_execution_from_public_folder_as_parent.yml"
build_date: "2026-04-27 19:13:54"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "69bd9b97-2be2-41b6-9816-fb08757a4d1a"
  - "Potentially Suspicious Execution From Parent Process In Public Folder"
attack_technique_ids:
  - "T1564"
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a potentially suspicious execution of a parent process located in the "\Users\Public" folder executing a child process containing references to shell or scripting binaries and commandlines.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1564-hide_artifacts|T1564: Hide Artifacts]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]

## Detection

```yaml
selection_parent:
  ParentImage|contains: :\Users\Public\
selection_child:
- Image|endswith:
  - \bitsadmin.exe
  - \certutil.exe
  - \cmd.exe
  - \cscript.exe
  - \mshta.exe
  - \powershell.exe
  - \pwsh.exe
  - \regsvr32.exe
  - \rundll32.exe
  - \wscript.exe
- CommandLine|contains:
  - bitsadmin
  - certutil
  - cscript
  - mshta
  - powershell
  - regsvr32
  - rundll32
  - wscript
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://redcanary.com/blog/blackbyte-ransomware/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_execution_from_public_folder_as_parent.yml)
