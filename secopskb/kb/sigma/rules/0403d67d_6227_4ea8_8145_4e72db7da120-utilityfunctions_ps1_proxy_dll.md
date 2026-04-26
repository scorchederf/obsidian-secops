---
sigma_id: "0403d67d-6227-4ea8-8145-4e72db7da120"
title: "UtilityFunctions.ps1 Proxy Dll"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_utilityfunctions.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_utilityfunctions.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "0403d67d-6227-4ea8-8145-4e72db7da120"
  - "UtilityFunctions.ps1 Proxy Dll"
attack_technique_ids:
  - "T1216"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# UtilityFunctions.ps1 Proxy Dll

Detects the use of a Microsoft signed script executing a managed DLL with PowerShell.

## Metadata

- Rule ID: 0403d67d-6227-4ea8-8145-4e72db7da120
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-05-28
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_utilityfunctions.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1216-system_script_proxy_execution|T1216]]

## Detection

```yaml
selection:
  CommandLine|contains:
  - UtilityFunctions.ps1
  - 'RegSnapin '
condition: selection
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Scripts/UtilityFunctions/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_utilityfunctions.yml)
