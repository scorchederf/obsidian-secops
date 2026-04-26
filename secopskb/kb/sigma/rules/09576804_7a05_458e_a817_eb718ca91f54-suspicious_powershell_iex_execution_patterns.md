---
sigma_id: "09576804-7a05-458e-a817-eb718ca91f54"
title: "Suspicious PowerShell IEX Execution Patterns"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_iex_patterns.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_iex_patterns.yml"
build_date: "2026-04-26 15:01:52"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "09576804-7a05-458e-a817-eb718ca91f54"
  - "Suspicious PowerShell IEX Execution Patterns"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious PowerShell IEX Execution Patterns

Detects suspicious ways to run Invoke-Execution using IEX alias

## Metadata

- Rule ID: 09576804-7a05-458e-a817-eb718ca91f54
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-03-24
- Modified: 2022-11-28
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_iex_patterns.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection_combined_1:
  Image|endswith:
  - \powershell.exe
  - \pwsh.exe
  CommandLine|contains:
  - ' | iex;'
  - ' | iex '
  - ' | iex}'
  - ' | IEX ;'
  - ' | IEX -Error'
  - ' | IEX (new'
  - ');IEX '
selection_combined_2:
  CommandLine|contains:
  - ::FromBase64String
  - '.GetString([System.Convert]::'
selection_standalone:
  CommandLine|contains:
  - )|iex;$
  - );iex($
  - );iex $
  - ' | IEX | '
  - ' | iex\"'
condition: all of selection_combined_* or selection_standalone
```

## False Positives

- Legitimate scripts that use IEX

## References

- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/invoke-expression?view=powershell-7.2
- https://www.huntress.com/blog/slashandgrab-screen-connect-post-exploitation-in-the-wild-cve-2024-1709-cve-2024-1708

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_iex_patterns.yml)
