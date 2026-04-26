---
sigma_id: "12f6b752-042d-483e-bf9c-915a6d06ad75"
title: "Windows Firewall Disabled via PowerShell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_disable_firewall.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_disable_firewall.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "12f6b752-042d-483e-bf9c-915a6d06ad75"
  - "Windows Firewall Disabled via PowerShell"
attack_technique_ids:
  - "T1562"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows Firewall Disabled via PowerShell

Detects attempts to disable the Windows Firewall using PowerShell

## Metadata

- Rule ID: 12f6b752-042d-483e-bf9c-915a6d06ad75
- Status: test
- Level: medium
- Author: Tim Rauch, Elastic (idea)
- Date: 2022-09-14
- Modified: 2023-02-13
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_disable_firewall.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562]]

## Detection

```yaml
selection_name:
- Image|endswith:
  - \powershell.exe
  - \pwsh.exe
  - \powershell_ise.exe
- OriginalFileName:
  - PowerShell.EXE
  - pwsh.dll
selection_args:
  CommandLine|contains|all:
  - 'Set-NetFirewallProfile '
  - ' -Enabled '
  - ' False'
selection_opt:
  CommandLine|contains:
  - ' -All '
  - Public
  - Domain
  - Private
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://www.elastic.co/guide/en/security/current/windows-firewall-disabled-via-powershell.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_disable_firewall.yml)
