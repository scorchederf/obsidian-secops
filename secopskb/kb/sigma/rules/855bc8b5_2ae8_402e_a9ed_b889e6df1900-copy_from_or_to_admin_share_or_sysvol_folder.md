---
sigma_id: "855bc8b5-2ae8-402e-a9ed-b889e6df1900"
title: "Copy From Or To Admin Share Or Sysvol Folder"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_copy_lateral_movement.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_copy_lateral_movement.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "855bc8b5-2ae8-402e-a9ed-b889e6df1900"
  - "Copy From Or To Admin Share Or Sysvol Folder"
attack_technique_ids:
  - "T1039"
  - "T1048"
  - "T1021.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Copy From Or To Admin Share Or Sysvol Folder

Detects a copy command or a copy utility execution to or from an Admin share or remote

## Metadata

- Rule ID: 855bc8b5-2ae8-402e-a9ed-b889e6df1900
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems), oscd.community, Teymur Kheirkhabarov @HeirhabarovT, Zach Stanford @svch0st, Nasreddine Bencherchali
- Date: 2019-12-30
- Modified: 2025-10-22
- Source Path: rules/windows/process_creation/proc_creation_win_susp_copy_lateral_movement.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1039-data_from_network_shared_drive|T1039]]
- [[kb/attack/techniques/T1048-exfiltration_over_alternative_protocol|T1048]]
- [[kb/attack/techniques/T1021-remote_services|T1021.002]]

## Detection

```yaml
selection_target:
  CommandLine|contains:
  - \\\\*\\*$
  - \Sysvol\
selection_other_tools:
- Image|endswith:
  - \robocopy.exe
  - \xcopy.exe
- OriginalFileName:
  - robocopy.exe
  - XCOPY.EXE
selection_cmd_img:
- Image|endswith: \cmd.exe
- OriginalFileName: Cmd.Exe
selection_cmd_cli:
  CommandLine|contains: copy
selection_pwsh_img:
- Image|contains:
  - \powershell_ise.exe
  - \powershell.exe
  - \pwsh.exe
- OriginalFileName:
  - powershell_ise.exe
  - PowerShell.EXE
  - pwsh.dll
selection_pwsh_cli:
  CommandLine|contains:
  - copy-item
  - 'copy '
  - 'cpi '
  - ' cp '
  - 'move '
  - ' move-item'
  - ' mi '
  - ' mv '
condition: selection_target and (selection_other_tools or all of selection_cmd_* or
  all of selection_pwsh_*)
```

## False Positives

- Administrative scripts

## References

- https://twitter.com/SBousseaden/status/1211636381086339073
- https://drive.google.com/file/d/1lKya3_mLnR3UQuCoiYruO3qgu052_iS_/view
- https://www.elastic.co/guide/en/security/current/remote-file-copy-to-a-hidden-share.html
- https://www.microsoft.com/en-us/security/blog/2022/10/18/defenders-beware-a-case-for-post-ransomware-investigations/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_copy_lateral_movement.yml)
