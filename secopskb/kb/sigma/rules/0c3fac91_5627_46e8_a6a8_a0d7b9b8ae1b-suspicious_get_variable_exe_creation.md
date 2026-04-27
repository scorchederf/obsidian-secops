---
sigma_id: "0c3fac91-5627-46e8-a6a8-a0d7b9b8ae1b"
title: "Suspicious Get-Variable.exe Creation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_susp_get_variable.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_get_variable.yml"
build_date: "2026-04-27 19:13:56"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "0c3fac91-5627-46e8-a6a8-a0d7b9b8ae1b"
  - "Suspicious Get-Variable.exe Creation"
attack_technique_ids:
  - "T1546"
  - "T1027"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Get-Variable is a valid PowerShell cmdlet
WindowsApps is by default in the path where PowerShell is executed.
So when the Get-Variable command is issued on PowerShell execution, the system first looks for the Get-Variable executable in the path and executes the malicious binary instead of looking for the PowerShell cmdlet.

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546: Event Triggered Execution]]
- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027: Obfuscated Files or Information]]

## Detection

```yaml
selection:
  TargetFilename|endswith: Local\Microsoft\WindowsApps\Get-Variable.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://blog.malwarebytes.com/threat-intelligence/2022/04/colibri-loader-combines-task-scheduler-and-powershell-in-clever-persistence-technique/
- https://www.joesandbox.com/analysis/465533/0/html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_get_variable.yml)
