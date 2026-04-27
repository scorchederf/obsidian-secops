---
sigma_id: "e312efd0-35a1-407f-8439-b8d434b438a6"
title: "Potential PowerShell Obfuscation Via WCHAR/CHAR"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_obfuscation_via_utf8.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_obfuscation_via_utf8.yml"
build_date: "2026-04-27 19:13:54"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "e312efd0-35a1-407f-8439-b8d434b438a6"
  - "Potential PowerShell Obfuscation Via WCHAR/CHAR"
attack_technique_ids:
  - "T1059.001"
  - "T1027"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious encoded character syntax often used for defense evasion

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]
- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027: Obfuscated Files or Information]]

## Detection

```yaml
selection:
  CommandLine|contains:
  - '[char]0x'
  - (WCHAR)0x
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/0gtweet/status/1281103918693482496

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_obfuscation_via_utf8.yml)
