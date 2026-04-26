---
sigma_id: "fad91067-08c5-4d1a-8d8c-d96a21b37814"
title: "Potential PowerShell Execution Policy Tampering"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_powershell_execution_policy.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_powershell_execution_policy.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "fad91067-08c5-4d1a-8d8c-d96a21b37814"
  - "Potential PowerShell Execution Policy Tampering"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential PowerShell Execution Policy Tampering

Detects changes to the PowerShell execution policy in order to bypass signing requirements for script execution

## Metadata

- Rule ID: fad91067-08c5-4d1a-8d8c-d96a21b37814
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-01-11
- Modified: 2023-12-14
- Source Path: rules/windows/registry/registry_set/registry_set_powershell_execution_policy.yml

## Logsource

- category: registry_set
- product: windows

## Detection

```yaml
selection:
  TargetObject|endswith:
  - \ShellIds\Microsoft.PowerShell\ExecutionPolicy
  - \Policies\Microsoft\Windows\PowerShell\ExecutionPolicy
  Details|contains:
  - Bypass
  - Unrestricted
filter_main_svchost:
  Image|contains:
  - :\Windows\System32\
  - :\Windows\SysWOW64\
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-7.3

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_powershell_execution_policy.yml)
