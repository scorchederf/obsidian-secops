---
sigma_id: "b9d9cc83-380b-4ba3-8d8f-60c0e7e2930c"
title: "Suspicious PowerShell Encoded Command Patterns"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_base64_encoded_cmd_patterns.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_base64_encoded_cmd_patterns.yml"
build_date: "2026-04-27 19:13:57"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "b9d9cc83-380b-4ba3-8d8f-60c0e7e2930c"
  - "Suspicious PowerShell Encoded Command Patterns"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects PowerShell command line patterns in combincation with encoded commands that often appear in malware infection chains

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \powershell.exe
  - \pwsh.exe
- OriginalFileName:
  - PowerShell.Exe
  - pwsh.dll
selection_flags:
  CommandLine|contains:
  - ' -e '
  - ' -en '
  - ' -enc '
  - ' -enco'
selection_encoded:
  CommandLine|contains:
  - ' JAB'
  - ' SUVYI'
  - ' SQBFAFgA'
  - ' aWV4I'
  - ' IAB'
  - ' PAA'
  - ' aQBlAHgA'
filter_gcworker:
  ParentImage|contains:
  - C:\Packages\Plugins\Microsoft.GuestConfiguration.ConfigurationforWindows\
  - \gc_worker.exe
condition: all of selection_* and not 1 of filter_*
```

## False Positives

- Other tools that work with encoded scripts in the command line instead of script files

## References

- https://app.any.run/tasks/b9040c63-c140-479b-ad59-f1bb56ce7a97/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_base64_encoded_cmd_patterns.yml)
