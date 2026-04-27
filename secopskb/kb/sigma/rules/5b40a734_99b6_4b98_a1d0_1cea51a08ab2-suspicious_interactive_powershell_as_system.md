---
sigma_id: "5b40a734-99b6-4b98-a1d0-1cea51a08ab2"
title: "Suspicious Interactive PowerShell as SYSTEM"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_susp_system_interactive_powershell.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_system_interactive_powershell.yml"
build_date: "2026-04-27 19:13:56"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "5b40a734-99b6-4b98-a1d0-1cea51a08ab2"
  - "Suspicious Interactive PowerShell as SYSTEM"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the creation of files that indicator an interactive use of PowerShell in the SYSTEM user context

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]

## Detection

```yaml
selection:
  TargetFilename:
  - C:\Windows\System32\config\systemprofile\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
  - C:\Windows\System32\config\systemprofile\AppData\Local\Microsoft\Windows\PowerShell\StartupProfileData-Interactive
condition: selection
```

## False Positives

- Administrative activity
- PowerShell scripts running as SYSTEM user

## References

- https://jpcertcc.github.io/ToolAnalysisResultSheet/details/PowerSploit_Invoke-Mimikatz.htm

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_system_interactive_powershell.yml)
