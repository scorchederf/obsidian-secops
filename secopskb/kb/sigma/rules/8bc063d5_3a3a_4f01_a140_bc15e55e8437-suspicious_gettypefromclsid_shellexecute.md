---
sigma_id: "8bc063d5-3a3a-4f01-a140-bc15e55e8437"
title: "Suspicious GetTypeFromCLSID ShellExecute"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_gettypefromclsid.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_gettypefromclsid.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "8bc063d5-3a3a-4f01-a140-bc15e55e8437"
  - "Suspicious GetTypeFromCLSID ShellExecute"
attack_technique_ids:
  - "T1546.015"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious GetTypeFromCLSID ShellExecute

Detects suspicious Powershell code that execute COM Objects

## Metadata

- Rule ID: 8bc063d5-3a3a-4f01-a140-bc15e55e8437
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-04-02
- Source Path: rules/windows/powershell/powershell_script/posh_ps_susp_gettypefromclsid.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.015]]

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - ::GetTypeFromCLSID(
  - .ShellExecute(
condition: selection
```

## False Positives

- Legitimate PowerShell scripts

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1546.015/T1546.015.md#atomic-test-2---powershell-execute-com-object

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_gettypefromclsid.yml)
