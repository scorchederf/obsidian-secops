---
sigma_id: "78aa1347-1517-4454-9982-b338d6df8343"
title: "Powershell MsXml COM Object"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_msxml_com.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_msxml_com.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "78aa1347-1517-4454-9982-b338d6df8343"
  - "Powershell MsXml COM Object"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Powershell MsXml COM Object

Adversaries may abuse PowerShell commands and scripts for execution.
PowerShell is a powerful interactive command-line interface and scripting environment included in the Windows operating system. (Citation: TechNet PowerShell)
Adversaries can use PowerShell to perform a number of actions, including discovery of information and execution of code

## Metadata

- Rule ID: 78aa1347-1517-4454-9982-b338d6df8343
- Status: test
- Level: medium
- Author: frack113, MatilJ
- Date: 2022-01-19
- Modified: 2022-05-19
- Source Path: rules/windows/powershell/powershell_script/posh_ps_msxml_com.yml

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
  ScriptBlockText|contains|all:
  - New-Object
  - -ComObject
  - MsXml2.
  - XmlHttp
condition: selection
```

## False Positives

- Legitimate administrative script

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1059.001/T1059.001.md#atomic-test-7---powershell-msxml-com-object---with-prompt
- https://learn.microsoft.com/en-us/previous-versions/windows/desktop/ms766431(v=vs.85)
- https://www.trendmicro.com/en_id/research/22/e/uncovering-a-kingminer-botnet-attack-using-trend-micro-managed-x.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_msxml_com.yml)
