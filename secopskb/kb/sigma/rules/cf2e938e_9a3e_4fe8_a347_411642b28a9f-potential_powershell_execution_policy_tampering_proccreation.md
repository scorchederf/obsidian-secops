---
sigma_id: "cf2e938e-9a3e-4fe8-a347-411642b28a9f"
title: "Potential PowerShell Execution Policy Tampering - ProcCreation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_registry_set_unsecure_powershell_policy.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_registry_set_unsecure_powershell_policy.yml"
build_date: "2026-04-27 19:13:54"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects changes to the PowerShell execution policy registry key in order to bypass signing requirements for script execution from the CommandLine

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
