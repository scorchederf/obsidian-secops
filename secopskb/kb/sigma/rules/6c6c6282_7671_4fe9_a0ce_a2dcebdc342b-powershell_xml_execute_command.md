---
sigma_id: "6c6c6282-7671-4fe9-a0ce-a2dcebdc342b"
title: "Powershell XML Execute Command"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_xml_iex.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_xml_iex.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "6c6c6282-7671-4fe9-a0ce-a2dcebdc342b"
  - "Powershell XML Execute Command"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Powershell XML Execute Command

Adversaries may abuse PowerShell commands and scripts for execution.
PowerShell is a powerful interactive command-line interface and scripting environment included in the Windows operating system. (Citation: TechNet PowerShell)
Adversaries can use PowerShell to perform a number of actions, including discovery of information and execution of code

## Metadata

- Rule ID: 6c6c6282-7671-4fe9-a0ce-a2dcebdc342b
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-01-19
- Modified: 2023-01-19
- Source Path: rules/windows/powershell/powershell_script/posh_ps_xml_iex.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection_xml:
  ScriptBlockText|contains|all:
  - New-Object
  - System.Xml.XmlDocument
  - .Load
selection_exec:
  ScriptBlockText|contains:
  - 'IEX '
  - 'Invoke-Expression '
  - 'Invoke-Command '
  - ICM -
condition: all of selection_*
```

## False Positives

- Legitimate administrative script

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1059.001/T1059.001.md#atomic-test-8---powershell-xml-requests

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_xml_iex.yml)
