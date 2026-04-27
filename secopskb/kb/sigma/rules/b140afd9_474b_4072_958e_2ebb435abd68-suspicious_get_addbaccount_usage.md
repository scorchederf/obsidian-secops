---
sigma_id: "b140afd9-474b-4072-958e-2ebb435abd68"
title: "Suspicious Get-ADDBAccount Usage"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_module/posh_pm_get_addbaccount.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_get_addbaccount.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / ps_module"
aliases:
  - "b140afd9-474b-4072-958e-2ebb435abd68"
  - "Suspicious Get-ADDBAccount Usage"
attack_technique_ids:
  - "T1003.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious Get-ADDBAccount Usage

Detects suspicious invocation of the Get-ADDBAccount script that reads from a ntds.dit file and may be used to get access to credentials without using any credential dumpers

## Metadata

- Rule ID: b140afd9-474b-4072-958e-2ebb435abd68
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-03-16
- Source Path: rules/windows/powershell/powershell_module/posh_pm_get_addbaccount.yml

## Logsource

- category: ps_module
- definition: 0ad03ef1-f21b-4a79-8ce8-e6900c54b65b
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.003]]

## Detection

```yaml
selection:
  Payload|contains|all:
  - Get-ADDBAccount
  - 'BootKey '
  - 'DatabasePath '
condition: selection
```

## False Positives

- Unknown

## References

- https://www.n00py.io/2022/03/manipulating-user-passwords-without-mimikatz/
- https://github.com/MichaelGrafnetter/DSInternals/blob/7ba59c12ee9a1cb430d7dc186a3366842dd612c8/Documentation/PowerShell/Get-ADDBAccount.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_get_addbaccount.yml)
