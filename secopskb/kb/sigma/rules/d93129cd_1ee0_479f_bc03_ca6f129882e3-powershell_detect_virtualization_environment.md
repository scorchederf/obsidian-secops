---
sigma_id: "d93129cd-1ee0-479f-bc03-ca6f129882e3"
title: "Powershell Detect Virtualization Environment"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_detect_vm_env.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_detect_vm_env.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "d93129cd-1ee0-479f-bc03-ca6f129882e3"
  - "Powershell Detect Virtualization Environment"
attack_technique_ids:
  - "T1497.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Powershell Detect Virtualization Environment

Adversaries may employ various system checks to detect and avoid virtualization and analysis environments.
This may include changing behaviors based on the results of checks for the presence of artifacts indicative of a virtual machine environment (VME) or sandbox

## Metadata

- Rule ID: d93129cd-1ee0-479f-bc03-ca6f129882e3
- Status: test
- Level: medium
- Author: frack113, Duc.Le-GTSC
- Date: 2021-08-03
- Modified: 2022-03-03
- Source Path: rules/windows/powershell/powershell_script/posh_ps_detect_vm_env.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1497-virtualization_sandbox_evasion|T1497.001]]

## Detection

```yaml
selection_action:
  ScriptBlockText|contains:
  - Get-WmiObject
  - gwmi
selection_module:
  ScriptBlockText|contains:
  - MSAcpi_ThermalZoneTemperature
  - Win32_ComputerSystem
condition: all of selection*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1497.001/T1497.001.md
- https://techgenix.com/malicious-powershell-scripts-evade-detection/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_detect_vm_env.yml)
