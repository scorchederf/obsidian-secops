---
sigma_id: "59e938ff-0d6d-4dc3-b13f-36cc28734d4e"
title: "Execute Code with Pester.bat"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_pester_1.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_pester_1.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "59e938ff-0d6d-4dc3-b13f-36cc28734d4e"
  - "Execute Code with Pester.bat"
attack_technique_ids:
  - "T1059.001"
  - "T1216"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Execute Code with Pester.bat

Detects code execution via Pester.bat (Pester - Powershell Modulte for testing)

## Metadata

- Rule ID: 59e938ff-0d6d-4dc3-b13f-36cc28734d4e
- Status: test
- Level: medium
- Author: Julia Fomina, oscd.community
- Date: 2020-10-08
- Modified: 2023-11-09
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_pester_1.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]
- [[kb/attack/techniques/T1216-system_script_proxy_execution|T1216]]

## Detection

```yaml
powershell_module:
  Image|endswith:
  - \powershell.exe
  - \pwsh.exe
  CommandLine|contains|all:
  - Pester
  - Get-Help
cmd_execution:
  Image|endswith: \cmd.exe
  CommandLine|contains|all:
  - pester
  - ;
get_help:
  CommandLine|contains:
  - help
  - \?
condition: powershell_module or (cmd_execution and get_help)
```

## False Positives

- Legitimate use of Pester for writing tests for Powershell scripts and modules

## References

- https://twitter.com/Oddvarmoe/status/993383596244258816
- https://github.com/api0cradle/LOLBAS/blob/d148d278f5f205ce67cfaf49afdfb68071c7252a/OSScripts/pester.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_pester_1.yml)
