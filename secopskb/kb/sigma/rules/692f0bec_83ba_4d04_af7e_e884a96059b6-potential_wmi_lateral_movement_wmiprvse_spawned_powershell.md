---
sigma_id: "692f0bec-83ba-4d04-af7e-e884a96059b6"
title: "Potential WMI Lateral Movement WmiPrvSE Spawned PowerShell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wmiprvse_spawns_powershell.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmiprvse_spawns_powershell.yml"
build_date: "2026-04-26 14:14:33"
status: "stable"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "692f0bec-83ba-4d04-af7e-e884a96059b6"
  - "Potential WMI Lateral Movement WmiPrvSE Spawned PowerShell"
attack_technique_ids:
  - "T1047"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential WMI Lateral Movement WmiPrvSE Spawned PowerShell

Detects Powershell as a child of the WmiPrvSE process. Which could be a sign of lateral movement via WMI.

## Metadata

- Rule ID: 692f0bec-83ba-4d04-af7e-e884a96059b6
- Status: stable
- Level: medium
- Author: Markus Neis @Karneades
- Date: 2019-04-03
- Modified: 2023-03-29
- Source Path: rules/windows/process_creation/proc_creation_win_wmiprvse_spawns_powershell.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection_parent:
  ParentImage|endswith: \WmiPrvSE.exe
selection_img:
- Image|endswith:
  - \powershell.exe
  - \pwsh.exe
- OriginalFileName:
  - PowerShell.EXE
  - pwsh.dll
condition: all of selection_*
```

## False Positives

- AppvClient
- CCM
- WinRM

## References

- https://any.run/report/68bc255f9b0db6a0d30a8f2dadfbee3256acfe12497bf93943bc1eab0735e45e/a2385d6f-34f7-403c-90d3-b1f9d2a90a5e

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmiprvse_spawns_powershell.yml)
