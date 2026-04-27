---
sigma_id: "36fbec91-fa1b-4d5d-8df1-8d8edcb632ad"
title: "Code Executed Via Office Add-in XLL File"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_office_comobject_registerxll.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_office_comobject_registerxll.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "36fbec91-fa1b-4d5d-8df1-8d8edcb632ad"
  - "Code Executed Via Office Add-in XLL File"
attack_technique_ids:
  - "T1137.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Code Executed Via Office Add-in XLL File

Adversaries may abuse Microsoft Office add-ins to obtain persistence on a compromised system.
Office add-ins can be used to add functionality to Office programs

## Metadata

- Rule ID: 36fbec91-fa1b-4d5d-8df1-8d8edcb632ad
- Status: test
- Level: high
- Author: frack113
- Date: 2021-12-28
- Source Path: rules/windows/powershell/powershell_script/posh_ps_office_comobject_registerxll.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1137-office_application_startup|T1137.006]]

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - 'new-object '
  - '-ComObject '
  - .application
  - .RegisterXLL
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1137.006/T1137.006.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_office_comobject_registerxll.yml)
