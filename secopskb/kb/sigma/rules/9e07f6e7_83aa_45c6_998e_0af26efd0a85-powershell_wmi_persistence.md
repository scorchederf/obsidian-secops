---
sigma_id: "9e07f6e7-83aa-45c6-998e-0af26efd0a85"
title: "Powershell WMI Persistence"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_wmi_persistence.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_wmi_persistence.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "9e07f6e7-83aa-45c6-998e-0af26efd0a85"
  - "Powershell WMI Persistence"
attack_technique_ids:
  - "T1546.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Powershell WMI Persistence

Adversaries may establish persistence and elevate privileges by executing malicious content triggered by a Windows Management Instrumentation (WMI) event subscription.

## Metadata

- Rule ID: 9e07f6e7-83aa-45c6-998e-0af26efd0a85
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-08-19
- Modified: 2022-12-25
- Source Path: rules/windows/powershell/powershell_script/posh_ps_wmi_persistence.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.003]]

## Detection

```yaml
selection_ioc:
- ScriptBlockText|contains|all:
  - 'New-CimInstance '
  - '-Namespace root/subscription '
  - '-ClassName __EventFilter '
  - '-Property '
- ScriptBlockText|contains|all:
  - 'New-CimInstance '
  - '-Namespace root/subscription '
  - '-ClassName CommandLineEventConsumer '
  - '-Property '
condition: selection_ioc
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1546.003/T1546.003.md
- https://github.com/EmpireProject/Empire/blob/08cbd274bef78243d7a8ed6443b8364acd1fc48b/data/module_source/persistence/Persistence.psm1#L545

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_wmi_persistence.yml)
