---
sigma_id: "1e53dd56-8d83-4eb4-a43e-b790a05510aa"
title: "Always Install Elevated MSI Spawned Cmd And Powershell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_elavated_msi_spawned_shell.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_elavated_msi_spawned_shell.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "1e53dd56-8d83-4eb4-a43e-b790a05510aa"
  - "Always Install Elevated MSI Spawned Cmd And Powershell"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Always Install Elevated MSI Spawned Cmd And Powershell

Detects Windows Installer service (msiexec.exe) spawning "cmd" or "powershell"

## Metadata

- Rule ID: 1e53dd56-8d83-4eb4-a43e-b790a05510aa
- Status: test
- Level: medium
- Author: Teymur Kheirkhabarov (idea), Mangatas Tondang (rule), oscd.community
- Date: 2020-10-13
- Modified: 2022-10-20
- Source Path: rules/windows/process_creation/proc_creation_win_susp_elavated_msi_spawned_shell.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \cmd.exe
  - \powershell.exe
  - \pwsh.exe
- OriginalFileName:
  - Cmd.Exe
  - PowerShell.EXE
  - pwsh.dll
selection_parent:
  ParentImage|contains|all:
  - \Windows\Installer\
  - msi
  ParentImage|endswith: tmp
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://image.slidesharecdn.com/kheirkhabarovoffzonefinal-181117201458/95/hunting-for-privilege-escalation-in-windows-environment-50-638.jpg

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_elavated_msi_spawned_shell.yml)
