---
sigma_id: "ae6f14e6-14de-45b0-9f44-c0986f50dc89"
title: "Change Default File Association To Executable Via Assoc"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_cmd_assoc_tamper_exe_file_association.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_assoc_tamper_exe_file_association.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "ae6f14e6-14de-45b0-9f44-c0986f50dc89"
  - "Change Default File Association To Executable Via Assoc"
attack_technique_ids:
  - "T1546.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects when a program changes the default file association of any extension to an executable.
When a file is opened, the default program used to open the file (also called the file association or handler) is checked. File association selections are stored in the Windows Registry and can be edited by users, administrators, or programs that have Registry access or by administrators using the built-in assoc utility. Applications can modify the file association for a given file extension to call an arbitrary program when a file with the given extension is opened.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution#^t1546001-change-default-file-association|T1546.001: Change Default File Association]]

## Detection

```yaml
selection_img:
- Image|endswith: \cmd.exe
- OriginalFileName: Cmd.Exe
selection_cli:
  CommandLine|contains|all:
  - 'assoc '
  - exefile
filter:
  CommandLine|contains: .exe=exefile
condition: all of selection_* and not filter
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/assoc

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_assoc_tamper_exe_file_association.yml)
