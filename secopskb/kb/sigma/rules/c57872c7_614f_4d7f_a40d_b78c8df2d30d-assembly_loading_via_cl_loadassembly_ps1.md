---
sigma_id: "c57872c7-614f-4d7f-a40d-b78c8df2d30d"
title: "Assembly Loading Via CL_LoadAssembly.ps1"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_cl_loadassembly.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_cl_loadassembly.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "c57872c7-614f-4d7f-a40d-b78c8df2d30d"
  - "Assembly Loading Via CL_LoadAssembly.ps1"
attack_technique_ids:
  - "T1216"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Assembly Loading Via CL_LoadAssembly.ps1

Detects calls to "LoadAssemblyFromPath" or "LoadAssemblyFromNS" that are part of the "CL_LoadAssembly.ps1" script. This can be abused to load different assemblies and bypass App locker controls.

## Metadata

- Rule ID: c57872c7-614f-4d7f-a40d-b78c8df2d30d
- Status: test
- Level: medium
- Author: frack113, Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-05-21
- Modified: 2023-08-17
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_cl_loadassembly.yml

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
  - 'LoadAssemblyFromPath '
  - 'LoadAssemblyFromNS '
condition: selection
```

## False Positives

- Unknown

## References

- https://bohops.com/2018/01/07/executing-commands-and-bypassing-applocker-with-powershell-diagnostic-scripts/
- https://lolbas-project.github.io/lolbas/Scripts/CL_LoadAssembly/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_cl_loadassembly.yml)
