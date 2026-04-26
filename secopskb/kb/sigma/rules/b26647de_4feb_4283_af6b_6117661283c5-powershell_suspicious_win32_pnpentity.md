---
sigma_id: "b26647de-4feb-4283-af6b-6117661283c5"
title: "Powershell Suspicious Win32_PnPEntity"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_win32_pnpentity.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_win32_pnpentity.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "low"
logsource: "windows / ps_script"
aliases:
  - "b26647de-4feb-4283-af6b-6117661283c5"
  - "Powershell Suspicious Win32_PnPEntity"
attack_technique_ids:
  - "T1120"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Powershell Suspicious Win32_PnPEntity

Adversaries may attempt to gather information about attached peripheral devices and components connected to a computer system.

## Metadata

- Rule ID: b26647de-4feb-4283-af6b-6117661283c5
- Status: test
- Level: low
- Author: frack113
- Date: 2021-08-23
- Modified: 2022-12-25
- Source Path: rules/windows/powershell/powershell_script/posh_ps_susp_win32_pnpentity.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1120-peripheral_device_discovery|T1120]]

## Detection

```yaml
selection:
  ScriptBlockText|contains: Win32_PnPEntity
condition: selection
```

## False Positives

- Admin script

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1120/T1120.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_win32_pnpentity.yml)
