---
sigma_id: "602f5669-6927-4688-84db-0d4b7afb2150"
title: "Disable Powershell Command History"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_disable_psreadline_command_history.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_disable_psreadline_command_history.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "602f5669-6927-4688-84db-0d4b7afb2150"
  - "Disable Powershell Command History"
attack_technique_ids:
  - "T1070.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects scripts or commands that disabled the Powershell command history by removing psreadline module

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal#^t1070003-clear-command-history|T1070.003: Clear Command History]]

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - Remove-Module
  - psreadline
condition: selection
```

## False Positives

- Legitimate script that disables the command history

## References

- https://twitter.com/DissectMalware/status/1062879286749773824

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_disable_psreadline_command_history.yml)
