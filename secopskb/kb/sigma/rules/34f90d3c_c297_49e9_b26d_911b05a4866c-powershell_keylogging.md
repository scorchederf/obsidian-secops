---
sigma_id: "34f90d3c-c297-49e9-b26d-911b05a4866c"
title: "Powershell Keylogging"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_keylogging.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_keylogging.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "34f90d3c-c297-49e9-b26d-911b05a4866c"
  - "Powershell Keylogging"
attack_technique_ids:
  - "T1056.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Powershell Keylogging

Adversaries may log user keystrokes to intercept credentials as the user types them.

## Metadata

- Rule ID: 34f90d3c-c297-49e9-b26d-911b05a4866c
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-07-30
- Modified: 2022-07-11
- Source Path: rules/windows/powershell/powershell_script/posh_ps_keylogging.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1056-input_capture|T1056.001]]

## Detection

```yaml
selection_basic:
  ScriptBlockText|contains: Get-Keystrokes
selection_high:
  ScriptBlockText|contains|all:
  - Get-ProcAddress user32.dll GetAsyncKeyState
  - Get-ProcAddress user32.dll GetForegroundWindow
condition: 1 of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1218/T1218.md
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1056.001/src/Get-Keystrokes.ps1

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_keylogging.yml)
