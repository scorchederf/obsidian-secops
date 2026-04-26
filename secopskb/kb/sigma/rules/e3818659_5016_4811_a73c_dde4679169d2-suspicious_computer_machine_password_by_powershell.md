---
sigma_id: "e3818659-5016-4811-a73c-dde4679169d2"
title: "Suspicious Computer Machine Password by PowerShell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_module/posh_pm_susp_reset_computermachinepassword.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_susp_reset_computermachinepassword.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / ps_module"
aliases:
  - "e3818659-5016-4811-a73c-dde4679169d2"
  - "Suspicious Computer Machine Password by PowerShell"
attack_technique_ids:
  - "T1078"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Computer Machine Password by PowerShell

The Reset-ComputerMachinePassword cmdlet changes the computer account password that the computers use to authenticate to the domain controllers in the domain.
You can use it to reset the password of the local computer.

## Metadata

- Rule ID: e3818659-5016-4811-a73c-dde4679169d2
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-02-21
- Source Path: rules/windows/powershell/powershell_module/posh_pm_susp_reset_computermachinepassword.yml

## Logsource

- category: ps_module
- definition: 0ad03ef1-f21b-4a79-8ce8-e6900c54b65b
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078]]

## Detection

```yaml
selection:
  ContextInfo|contains: Reset-ComputerMachinePassword
condition: selection
```

## False Positives

- Administrator PowerShell scripts

## References

- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/reset-computermachinepassword?view=powershell-5.1
- https://thedfirreport.com/2022/02/21/qbot-and-zerologon-lead-to-full-domain-compromise/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_susp_reset_computermachinepassword.yml)
