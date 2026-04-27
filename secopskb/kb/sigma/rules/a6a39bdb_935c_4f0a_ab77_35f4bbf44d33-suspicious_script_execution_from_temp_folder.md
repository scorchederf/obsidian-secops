---
sigma_id: "a6a39bdb-935c-4f0a-ab77-35f4bbf44d33"
title: "Suspicious Script Execution From Temp Folder"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_script_exec_from_temp.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_script_exec_from_temp.yml"
build_date: "2026-04-27 19:13:57"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "a6a39bdb-935c-4f0a-ab77-35f4bbf44d33"
  - "Suspicious Script Execution From Temp Folder"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a suspicious script executions from temporary folder

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]

## Detection

```yaml
selection:
  Image|endswith:
  - \powershell.exe
  - \pwsh.exe
  - \mshta.exe
  - \wscript.exe
  - \cscript.exe
  CommandLine|contains:
  - \Windows\Temp
  - \Temporary Internet
  - \AppData\Local\Temp
  - \AppData\Roaming\Temp
  - '%TEMP%'
  - '%TMP%'
  - '%LocalAppData%\Temp'
filter:
  CommandLine|contains:
  - ' >'
  - Out-File
  - ConvertTo-Json
  - -WindowStyle hidden -Verb runAs
  - \Windows\system32\config\systemprofile\AppData\Local\Temp\Amazon\EC2-Windows\
condition: selection and not filter
```

## False Positives

- Administrative scripts

## References

- https://www.microsoft.com/security/blog/2021/07/13/microsoft-discovers-threat-actor-targeting-solarwinds-serv-u-software-with-0-day-exploit/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_script_exec_from_temp.yml)
