---
sigma_id: "b7ec41a4-042c-4f31-a5db-d0fcde9fa5c5"
title: "PowerShell PSAttack"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_psattack.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_psattack.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "b7ec41a4-042c-4f31-a5db-d0fcde9fa5c5"
  - "PowerShell PSAttack"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PowerShell PSAttack

Detects the use of PSAttack PowerShell hack tool

## Metadata

- Rule ID: b7ec41a4-042c-4f31-a5db-d0fcde9fa5c5
- Status: test
- Level: high
- Author: Sean Metcalf (source), Florian Roth (Nextron Systems)
- Date: 2017-03-05
- Modified: 2022-12-25
- Source Path: rules/windows/powershell/powershell_script/posh_ps_psattack.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection:
  ScriptBlockText|contains: PS ATTACK!!!
condition: selection
```

## False Positives

- Unknown

## References

- https://adsecurity.org/?p=2921

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_psattack.yml)
