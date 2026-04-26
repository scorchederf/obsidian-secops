---
sigma_id: "8f3ab69a-aa22-4943-aa58-e0a52fdf6818"
title: "User Shell Folders Registry Modification via CommandLine"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_user_shell_folders_registry_modification.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_user_shell_folders_registry_modification.yml"
build_date: "2026-04-26 15:01:53"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "8f3ab69a-aa22-4943-aa58-e0a52fdf6818"
  - "User Shell Folders Registry Modification via CommandLine"
attack_technique_ids:
  - "T1547.001"
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# User Shell Folders Registry Modification via CommandLine

Detects modifications to User Shell Folders registry values via reg.exe or PowerShell, which could indicate persistence attempts.
Attackers may modify User Shell Folders registry values to point to malicious executables or scripts that will be executed during startup.
This technique is often used to maintain persistence on a compromised system by ensuring that malicious payloads are executed automatically.

## Metadata

- Rule ID: 8f3ab69a-aa22-4943-aa58-e0a52fdf6818
- Status: experimental
- Level: high
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2026-01-05
- Source Path: rules/windows/process_creation/proc_creation_win_user_shell_folders_registry_modification.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.001]]
- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \powershell.exe
  - \pwsh.exe
  - \reg.exe
- OriginalFileName:
  - powershell.exe
  - pwsh.dll
  - reg.exe
selection_cli_action:
  CommandLine|contains:
  - ' add '
  - New-ItemProperty
  - Set-ItemProperty
  - 'si '
selection_cli_paths_root:
  CommandLine|contains:
  - \Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders
  - \Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders
selection_cli_paths_suffix:
  CommandLine|contains: Startup
condition: all of selection_*
```

## False Positives

- Usage of reg.exe or PowerShell to modify User Shell Folders for legitimate purposes; but rare.

## Simulation

### Change Startup Folder - HKLM Modify User Shell Folders Common Startup Value

- Atomic Test: [[kb/atomic/tests/acfef903_7662_447e_a391_9c91c2f00f7b-change_startup_folder_hklm_modify_user_shell_folders_common_startup_value|acfef903-7662-447e-a391-9c91c2f00f7b]]
- atomic_guid: acfef903-7662-447e-a391-9c91c2f00f7b
- name: Change Startup Folder - HKLM Modify User Shell Folders Common Startup Value
- technique: T1547.001
- type: atomic-red-team

## References

- https://www.welivesecurity.com/en/eset-research/muddywater-snakes-riverbank/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_user_shell_folders_registry_modification.yml)
