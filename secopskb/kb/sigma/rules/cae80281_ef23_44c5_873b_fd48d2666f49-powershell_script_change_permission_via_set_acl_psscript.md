---
sigma_id: "cae80281-ef23-44c5-873b-fd48d2666f49"
title: "PowerShell Script Change Permission Via Set-Acl - PsScript"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_set_acl.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_set_acl.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "low"
logsource: "windows / ps_script"
aliases:
  - "cae80281-ef23-44c5-873b-fd48d2666f49"
  - "PowerShell Script Change Permission Via Set-Acl - PsScript"
attack_technique_ids:
  - "T1222"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PowerShell Script Change Permission Via Set-Acl - PsScript

Detects PowerShell scripts set ACL to of a file or a folder

## Metadata

- Rule ID: cae80281-ef23-44c5-873b-fd48d2666f49
- Status: test
- Level: low
- Author: frack113, Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-07-18
- Source Path: rules/windows/powershell/powershell_script/posh_ps_set_acl.yml

## Logsource

- category: ps_script
- definition: bade5735-5ab0-4aa7-a642-a11be0e40872
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1222-file_and_directory_permissions_modification|T1222]]

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - 'Set-Acl '
  - '-AclObject '
  - '-Path '
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/74438b0237d141ee9c99747976447dc884cb1a39/atomics/T1505.005/T1505.005.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_set_acl.yml)
