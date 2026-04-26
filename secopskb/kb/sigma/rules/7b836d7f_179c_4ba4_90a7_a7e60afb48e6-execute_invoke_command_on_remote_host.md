---
sigma_id: "7b836d7f-179c-4ba4-90a7-a7e60afb48e6"
title: "Execute Invoke-command on Remote Host"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_invoke_command_remote.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_invoke_command_remote.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "7b836d7f-179c-4ba4-90a7-a7e60afb48e6"
  - "Execute Invoke-command on Remote Host"
attack_technique_ids:
  - "T1021.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Execute Invoke-command on Remote Host

Adversaries may use Valid Accounts to interact with remote systems using Windows Remote Management (WinRM). The adversary may then perform actions as the logged-on user.

## Metadata

- Rule ID: 7b836d7f-179c-4ba4-90a7-a7e60afb48e6
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-01-07
- Source Path: rules/windows/powershell/powershell_script/posh_ps_invoke_command_remote.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.006]]

## Detection

```yaml
selection_cmdlet:
  ScriptBlockText|contains|all:
  - 'invoke-command '
  - ' -ComputerName '
condition: selection_cmdlet
```

## False Positives

- Legitimate script

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1021.006/T1021.006.md#atomic-test-2---invoke-command
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/invoke-command?view=powershell-7.4

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_invoke_command_remote.yml)
