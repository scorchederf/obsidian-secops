---
sigma_id: "18988e1b-9087-4f8a-82fe-0414dce49878"
title: "Execute Code with Pester.bat as Parent"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_pester.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_pester.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "18988e1b-9087-4f8a-82fe-0414dce49878"
  - "Execute Code with Pester.bat as Parent"
attack_technique_ids:
  - "T1059.001"
  - "T1216"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Execute Code with Pester.bat as Parent

Detects code execution via Pester.bat (Pester - Powershell Modulte for testing)

## Metadata

- Rule ID: 18988e1b-9087-4f8a-82fe-0414dce49878
- Status: test
- Level: medium
- Author: frack113, Nasreddine Bencherchali
- Date: 2022-08-20
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_pester.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]
- [[kb/attack/techniques/T1216-system_script_proxy_execution|T1216]]

## Detection

```yaml
selection_module:
  ParentImage|endswith:
  - \powershell.exe
  - \pwsh.exe
  ParentCommandLine|contains: \WindowsPowerShell\Modules\Pester\
selection_cli:
  ParentCommandLine|contains:
  - '{ Invoke-Pester -EnableExit ;'
  - '{ Get-Help "'
condition: all of selection_*
```

## False Positives

- Legitimate use of Pester for writing tests for Powershell scripts and modules

## References

- https://twitter.com/Oddvarmoe/status/993383596244258816
- https://twitter.com/_st0pp3r_/status/1560072680887525378

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_pester.yml)
