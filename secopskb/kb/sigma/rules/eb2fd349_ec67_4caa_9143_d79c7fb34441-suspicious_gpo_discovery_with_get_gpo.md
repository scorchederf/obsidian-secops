---
sigma_id: "eb2fd349-ec67-4caa-9143-d79c7fb34441"
title: "Suspicious GPO Discovery With Get-GPO"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_get_gpo.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_get_gpo.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "low"
logsource: "windows / ps_script"
aliases:
  - "eb2fd349-ec67-4caa-9143-d79c7fb34441"
  - "Suspicious GPO Discovery With Get-GPO"
attack_technique_ids:
  - "T1615"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious GPO Discovery With Get-GPO

Detect use of Get-GPO to get one GPO or all the GPOs in a domain.

## Metadata

- Rule ID: eb2fd349-ec67-4caa-9143-d79c7fb34441
- Status: test
- Level: low
- Author: frack113
- Date: 2022-06-04
- Source Path: rules/windows/powershell/powershell_script/posh_ps_susp_get_gpo.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1615-group_policy_discovery|T1615]]

## Detection

```yaml
selection:
  ScriptBlockText|contains: Get-GPO
condition: selection
```

## False Positives

- Legitimate PowerShell scripts

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1615/T1615.md
- https://learn.microsoft.com/en-us/powershell/module/grouppolicy/get-gpo?view=windowsserver2022-ps

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_get_gpo.yml)
