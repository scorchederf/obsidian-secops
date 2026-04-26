---
sigma_id: "ddcd88cb-7f62-4ce5-86f9-1704190feb0a"
title: "Potential In-Memory Execution Using Reflection.Assembly"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_dotnet_assembly_from_file.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_dotnet_assembly_from_file.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "ddcd88cb-7f62-4ce5-86f9-1704190feb0a"
  - "Potential In-Memory Execution Using Reflection.Assembly"
attack_technique_ids:
  - "T1620"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential In-Memory Execution Using Reflection.Assembly

Detects usage of "Reflection.Assembly" load functions to dynamically load assemblies in memory

## Metadata

- Rule ID: ddcd88cb-7f62-4ce5-86f9-1704190feb0a
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-12-25
- Source Path: rules/windows/powershell/powershell_script/posh_ps_dotnet_assembly_from_file.yml

## Logsource

- category: ps_script
- definition: Script Block Logging must be enable
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1620-reflective_code_loading|T1620]]

## Detection

```yaml
selection:
  ScriptBlockText|contains: '[Reflection.Assembly]::load'
condition: selection
```

## False Positives

- Legitimate use of the library

## References

- https://speakerdeck.com/heirhabarov/hunting-for-powershell-abuse?slide=50

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_dotnet_assembly_from_file.yml)
