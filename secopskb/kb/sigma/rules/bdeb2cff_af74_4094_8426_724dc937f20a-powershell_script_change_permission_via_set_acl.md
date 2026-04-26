---
sigma_id: "bdeb2cff-af74-4094-8426-724dc937f20a"
title: "PowerShell Script Change Permission Via Set-Acl"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_set_acl.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_set_acl.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "bdeb2cff-af74-4094-8426-724dc937f20a"
  - "PowerShell Script Change Permission Via Set-Acl"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PowerShell Script Change Permission Via Set-Acl

Detects PowerShell execution to set the ACL of a file or a folder

## Metadata

- Rule ID: bdeb2cff-af74-4094-8426-724dc937f20a
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-10-18
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_set_acl.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_img:
- OriginalFileName:
  - PowerShell.EXE
  - pwsh.dll
- Image|endswith:
  - \powershell.exe
  - \pwsh.exe
selection_cmdlet:
  CommandLine|contains|all:
  - 'Set-Acl '
  - '-AclObject '
  - '-Path '
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-acl?view=powershell-5.1
- https://github.com/redcanaryco/atomic-red-team/blob/74438b0237d141ee9c99747976447dc884cb1a39/atomics/T1505.005/T1505.005.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_set_acl.yml)
