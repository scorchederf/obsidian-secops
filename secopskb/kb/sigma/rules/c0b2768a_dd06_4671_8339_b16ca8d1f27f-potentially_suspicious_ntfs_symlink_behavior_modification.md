---
sigma_id: "c0b2768a-dd06-4671-8339-b16ca8d1f27f"
title: "Potentially Suspicious NTFS Symlink Behavior Modification"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_fsutil_symlinkevaluation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_fsutil_symlinkevaluation.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "c0b2768a-dd06-4671-8339-b16ca8d1f27f"
  - "Potentially Suspicious NTFS Symlink Behavior Modification"
attack_technique_ids:
  - "T1059"
  - "T1222.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potentially Suspicious NTFS Symlink Behavior Modification

Detects the modification of NTFS symbolic link behavior using fsutil, which could be used to enable remote to local or remote to remote symlinks for potential attacks.

## Metadata

- Rule ID: c0b2768a-dd06-4671-8339-b16ca8d1f27f
- Status: test
- Level: medium
- Author: frack113, The DFIR Report
- Date: 2022-03-02
- Modified: 2025-11-13
- Source Path: rules/windows/process_creation/proc_creation_win_fsutil_symlinkevaluation.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]
- [[kb/attack/techniques/T1222-file_and_directory_permissions_modification|T1222.001]]

## Detection

```yaml
selection_img_proxy:
- Image|endswith:
  - \cmd.exe
  - \powershell.exe
  - \pwsh.exe
- OriginalFileName:
  - Cmd.Exe
  - PowerShell.EXE
  - pwsh.dll
selection_fsutil_cli:
  CommandLine|contains|all:
  - fsutil
  - behavior
  - set
  - SymlinkEvaluation
selection_symlink_params:
  CommandLine|contains:
  - R2L:1
  - R2R:1
  - L2L:1
condition: all of selection_*
```

## False Positives

- Legitimate usage, investigate the parent process and context to determine if benign.

## References

- https://www.cybereason.com/blog/cybereason-vs.-blackcat-ransomware
- https://learn.microsoft.com/fr-fr/windows-server/administration/windows-commands/fsutil-behavior
- https://thedfirreport.com/2025/06/30/hide-your-rdp-password-spray-leads-to-ransomhub-deployment/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_fsutil_symlinkevaluation.yml)
