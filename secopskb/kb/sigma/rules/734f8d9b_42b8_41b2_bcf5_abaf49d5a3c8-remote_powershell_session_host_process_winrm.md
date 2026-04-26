---
sigma_id: "734f8d9b-42b8-41b2-bcf5-abaf49d5a3c8"
title: "Remote PowerShell Session Host Process (WinRM)"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_winrm_remote_powershell_session_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_winrm_remote_powershell_session_process.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "734f8d9b-42b8-41b2-bcf5-abaf49d5a3c8"
  - "Remote PowerShell Session Host Process (WinRM)"
attack_technique_ids:
  - "T1059.001"
  - "T1021.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote PowerShell Session Host Process (WinRM)

Detects remote PowerShell sections by monitoring for wsmprovhost (WinRM host process) as a parent or child process (sign of an active PowerShell remote session).

## Metadata

- Rule ID: 734f8d9b-42b8-41b2-bcf5-abaf49d5a3c8
- Status: test
- Level: medium
- Author: Roberto Rodriguez @Cyb3rWard0g
- Date: 2019-09-12
- Modified: 2022-10-09
- Source Path: rules/windows/process_creation/proc_creation_win_winrm_remote_powershell_session_process.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]
- [[kb/attack/techniques/T1021-remote_services|T1021.006]]

## Detection

```yaml
selection:
- Image|endswith: \wsmprovhost.exe
- ParentImage|endswith: \wsmprovhost.exe
condition: selection
```

## False Positives

- Legitimate usage of remote Powershell, e.g. for monitoring purposes.

## References

- https://threathunterplaybook.com/hunts/windows/190511-RemotePwshExecution/notebook.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_winrm_remote_powershell_session_process.yml)
