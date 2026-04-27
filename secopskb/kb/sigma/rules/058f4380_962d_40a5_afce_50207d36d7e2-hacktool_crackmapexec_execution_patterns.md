---
sigma_id: "058f4380-962d-40a5-afce-50207d36d7e2"
title: "HackTool - CrackMapExec Execution Patterns"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_crackmapexec_execution_patterns.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_crackmapexec_execution_patterns.yml"
build_date: "2026-04-27 19:13:51"
status: "stable"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "058f4380-962d-40a5-afce-50207d36d7e2"
  - "HackTool - CrackMapExec Execution Patterns"
attack_technique_ids:
  - "T1047"
  - "T1053"
  - "T1059.003"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects various execution patterns of the CrackMapExec pentesting framework

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047: Windows Management Instrumentation]]
- [[kb/attack/techniques/T1053-scheduled_task_job|T1053: Scheduled Task/Job]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059003-windows-command-shell|T1059.003: Windows Command Shell]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]

### Software Tags

- S0106

## Detection

```yaml
selection:
  CommandLine|contains:
  - cmd.exe /Q /c * 1> \\\\*\\*\\* 2>&1
  - cmd.exe /C * > \\\\*\\*\\* 2>&1
  - cmd.exe /C * > *\\Temp\\* 2>&1
  - powershell.exe -exec bypass -noni -nop -w 1 -C "
  - 'powershell.exe -noni -nop -w 1 -enc '
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/byt3bl33d3r/CrackMapExec

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_crackmapexec_execution_patterns.yml)
