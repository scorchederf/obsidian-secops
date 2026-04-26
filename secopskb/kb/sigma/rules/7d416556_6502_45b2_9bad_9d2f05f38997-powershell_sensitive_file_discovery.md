---
sigma_id: "7d416556-6502-45b2-9bad-9d2f05f38997"
title: "Powershell Sensitive File Discovery"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_sensitive_file_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_sensitive_file_discovery.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "7d416556-6502-45b2-9bad-9d2f05f38997"
  - "Powershell Sensitive File Discovery"
attack_technique_ids:
  - "T1083"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Powershell Sensitive File Discovery

Detect adversaries enumerate sensitive files

## Metadata

- Rule ID: 7d416556-6502-45b2-9bad-9d2f05f38997
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-09-16
- Source Path: rules/windows/powershell/powershell_script/posh_ps_sensitive_file_discovery.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1083-file_and_directory_discovery|T1083]]

## Detection

```yaml
selection_action:
  ScriptBlockText|contains:
  - ls
  - get-childitem
  - gci
selection_recurse:
  ScriptBlockText|contains: -recurse
selection_file:
  ScriptBlockText|contains:
  - .pass
  - .kdbx
  - .kdb
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://twitter.com/malmoeb/status/1570814999370801158

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_sensitive_file_discovery.yml)
