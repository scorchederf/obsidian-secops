---
sigma_id: "5947497f-1aa4-41dd-9693-c9848d58727d"
title: "Suspicious Unblock-File"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_unblock_file.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_unblock_file.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "5947497f-1aa4-41dd-9693-c9848d58727d"
  - "Suspicious Unblock-File"
attack_technique_ids:
  - "T1553.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Unblock-File

Remove the Zone.Identifier alternate data stream which identifies the file as downloaded from the internet.

## Metadata

- Rule ID: 5947497f-1aa4-41dd-9693-c9848d58727d
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-02-01
- Source Path: rules/windows/powershell/powershell_script/posh_ps_susp_unblock_file.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1553-subvert_trust_controls|T1553.005]]

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - 'Unblock-File '
  - '-Path '
condition: selection
```

## False Positives

- Legitimate PowerShell scripts

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1553.005/T1553.005.md#atomic-test-3---remove-the-zoneidentifier-alternate-data-stream
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/unblock-file?view=powershell-7.2

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_unblock_file.yml)
