---
sigma_id: "cf2e938e-9a3e-4fe8-a347-411642b28a9f"
title: "Potential PowerShell Execution Policy Tampering - ProcCreation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_registry_set_unsecure_powershell_policy.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_registry_set_unsecure_powershell_policy.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "cf2e938e-9a3e-4fe8-a347-411642b28a9f"
  - "Potential PowerShell Execution Policy Tampering - ProcCreation"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential PowerShell Execution Policy Tampering - ProcCreation

Detects changes to the PowerShell execution policy registry key in order to bypass signing requirements for script execution from the CommandLine

## Metadata

- Rule ID: cf2e938e-9a3e-4fe8-a347-411642b28a9f
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-01-11
- Source Path: rules/windows/process_creation/proc_creation_win_registry_set_unsecure_powershell_policy.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_path:
  CommandLine|contains:
  - \ShellIds\Microsoft.PowerShell\ExecutionPolicy
  - \Policies\Microsoft\Windows\PowerShell\ExecutionPolicy
selection_values:
  CommandLine|contains:
  - Bypass
  - RemoteSigned
  - Unrestricted
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/de-de/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-7.3

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_registry_set_unsecure_powershell_policy.yml)
