---
sigma_id: "3bf1d859-3a7e-44cb-8809-a99e066d3478"
title: "PowerShell Set-Acl On Windows Folder - PsScript"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_set_acl_susp_location.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_set_acl_susp_location.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "3bf1d859-3a7e-44cb-8809-a99e066d3478"
  - "PowerShell Set-Acl On Windows Folder - PsScript"
attack_technique_ids:
  - "T1222"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# PowerShell Set-Acl On Windows Folder - PsScript

Detects PowerShell scripts to set the ACL to a file in the Windows folder

## Metadata

- Rule ID: 3bf1d859-3a7e-44cb-8809-a99e066d3478
- Status: test
- Level: high
- Author: frack113, Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-07-18
- Source Path: rules/windows/powershell/powershell_script/posh_ps_set_acl_susp_location.yml

## Logsource

- category: ps_script
- definition: bade5735-5ab0-4aa7-a642-a11be0e40872
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1222-file_and_directory_permissions_modification|T1222]]

## Detection

```yaml
selection_cmdlet:
  ScriptBlockText|contains|all:
  - 'Set-Acl '
  - '-AclObject '
selection_paths:
  ScriptBlockText|contains:
  - -Path "C:\Windows
  - -Path "C:/Windows
  - -Path 'C:\Windows
  - -Path 'C:/Windows
  - -Path C:\\Windows
  - -Path C:/Windows
  - -Path $env:windir
  - -Path "$env:windir
  - -Path '$env:windir
selection_permissions:
  ScriptBlockText|contains:
  - FullControl
  - Allow
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/74438b0237d141ee9c99747976447dc884cb1a39/atomics/T1505.005/T1505.005.md
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-acl?view=powershell-5.1

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_set_acl_susp_location.yml)
