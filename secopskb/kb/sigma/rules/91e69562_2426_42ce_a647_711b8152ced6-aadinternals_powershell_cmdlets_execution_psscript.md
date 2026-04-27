---
sigma_id: "91e69562-2426-42ce-a647-711b8152ced6"
title: "AADInternals PowerShell Cmdlets Execution - PsScript"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_aadinternals_cmdlets_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_aadinternals_cmdlets_execution.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "91e69562-2426-42ce-a647-711b8152ced6"
  - "AADInternals PowerShell Cmdlets Execution - PsScript"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# AADInternals PowerShell Cmdlets Execution - PsScript

Detects ADDInternals Cmdlet execution. A tool for administering Azure AD and Office 365. Which can be abused by threat actors to attack Azure AD or Office 365.

## Metadata

- Rule ID: 91e69562-2426-42ce-a647-711b8152ced6
- Status: test
- Level: high
- Author: Austin Songer (@austinsonger), Nasreddine Bencherchali (Nextron Systems), Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2022-12-23
- Modified: 2025-02-06
- Source Path: rules/windows/powershell/powershell_script/posh_ps_aadinternals_cmdlets_execution.yml

## Logsource

- category: ps_script
- definition: Script Block Logging must be enable
- product: windows

## Detection

```yaml
selection:
  ScriptBlockText|contains:
  - Add-AADInt
  - ConvertTo-AADInt
  - Disable-AADInt
  - Enable-AADInt
  - Export-AADInt
  - Find-AADInt
  - Get-AADInt
  - Grant-AADInt
  - Initialize-AADInt
  - Install-AADInt
  - Invoke-AADInt
  - Join-AADInt
  - New-AADInt
  - Open-AADInt
  - Read-AADInt
  - Register-AADInt
  - Remove-AADInt
  - Reset-AADInt
  - Resolve-AADInt
  - Restore-AADInt
  - Save-AADInt
  - Search-AADInt
  - Send-AADInt
  - Set-AADInt
  - Start-AADInt
  - Unprotect-AADInt
  - Update-AADInt
condition: selection
```

## False Positives

- Legitimate use of the library for administrative activity

## References

- https://o365blog.com/aadinternals/
- https://github.com/Gerenios/AADInternals

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_aadinternals_cmdlets_execution.yml)
