---
sigma_id: "c3d76afc-93df-461e-8e67-9b2bad3f2ac4"
title: "File Explorer Folder Opened Using Explorer Folder Shortcut Via Shell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_explorer_folder_shortcut_via_shell_binary.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_explorer_folder_shortcut_via_shell_binary.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "c3d76afc-93df-461e-8e67-9b2bad3f2ac4"
  - "File Explorer Folder Opened Using Explorer Folder Shortcut Via Shell"
attack_technique_ids:
  - "T1135"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# File Explorer Folder Opened Using Explorer Folder Shortcut Via Shell

Detects the initial execution of "cmd.exe" which spawns "explorer.exe" with the appropriate command line arguments for opening the "My Computer" folder.

## Metadata

- Rule ID: c3d76afc-93df-461e-8e67-9b2bad3f2ac4
- Status: test
- Level: high
- Author: @Kostastsale
- Date: 2022-12-22
- Modified: 2024-08-23
- Source Path: rules/windows/process_creation/proc_creation_win_explorer_folder_shortcut_via_shell_binary.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1135-network_share_discovery|T1135]]

## Detection

```yaml
selection:
  ParentImage|endswith:
  - \cmd.exe
  - \powershell.exe
  - \pwsh.exe
  Image|endswith: \explorer.exe
  CommandLine|contains: shell:mycomputerfolder
condition: selection
```

## False Positives

- Unknown

## References

- https://ss64.com/nt/shell.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_explorer_folder_shortcut_via_shell_binary.yml)
