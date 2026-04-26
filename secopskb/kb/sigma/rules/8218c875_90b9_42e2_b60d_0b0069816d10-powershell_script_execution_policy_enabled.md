---
sigma_id: "8218c875-90b9-42e2-b60d-0b0069816d10"
title: "PowerShell Script Execution Policy Enabled"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_powershell_enablescripts_enabled.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_powershell_enablescripts_enabled.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "low"
logsource: "windows / registry_set"
aliases:
  - "8218c875-90b9-42e2-b60d-0b0069816d10"
  - "PowerShell Script Execution Policy Enabled"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PowerShell Script Execution Policy Enabled

Detects the enabling of the PowerShell script execution policy. Once enabled, this policy allows scripts to be executed.

## Metadata

- Rule ID: 8218c875-90b9-42e2-b60d-0b0069816d10
- Status: test
- Level: low
- Author: Nasreddine Bencherchali (Nextron Systems), Thurein Oo
- Date: 2023-10-18
- Source Path: rules/windows/registry/registry_set/registry_set_powershell_enablescripts_enabled.yml

## Logsource

- category: registry_set
- product: windows

## Detection

```yaml
selection:
  TargetObject|endswith: \Policies\Microsoft\Windows\PowerShell\EnableScripts
  Details: DWORD (0x00000001)
condition: selection
```

## False Positives

- Likely

## References

- https://admx.help/?Category=Windows_10_2016&Policy=Microsoft.Policies.PowerShell::EnableScripts

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_powershell_enablescripts_enabled.yml)
