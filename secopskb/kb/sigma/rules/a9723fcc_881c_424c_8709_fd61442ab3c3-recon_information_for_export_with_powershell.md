---
sigma_id: "a9723fcc-881c-424c-8709-fd61442ab3c3"
title: "Recon Information for Export with PowerShell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_recon_export.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_recon_export.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "a9723fcc-881c-424c-8709-fd61442ab3c3"
  - "Recon Information for Export with PowerShell"
attack_technique_ids:
  - "T1119"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Recon Information for Export with PowerShell

Once established within a system or network, an adversary may use automated techniques for collecting internal data

## Metadata

- Rule ID: a9723fcc-881c-424c-8709-fd61442ab3c3
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-07-30
- Modified: 2022-12-25
- Source Path: rules/windows/powershell/powershell_script/posh_ps_susp_recon_export.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1119-automated_collection|T1119]]

## Detection

```yaml
selection_action:
  ScriptBlockText|contains:
  - 'Get-Service '
  - 'Get-ChildItem '
  - 'Get-Process '
selection_redirect:
  ScriptBlockText|contains: '> $env:TEMP\'
condition: all of selection*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1119/T1119.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_recon_export.yml)
