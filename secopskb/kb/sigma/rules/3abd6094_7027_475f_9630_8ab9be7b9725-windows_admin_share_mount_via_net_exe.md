---
sigma_id: "3abd6094-7027-475f-9630-8ab9be7b9725"
title: "Windows Admin Share Mount Via Net.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_net_use_mount_admin_share.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_net_use_mount_admin_share.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "3abd6094-7027-475f-9630-8ab9be7b9725"
  - "Windows Admin Share Mount Via Net.EXE"
attack_technique_ids:
  - "T1021.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows Admin Share Mount Via Net.EXE

Detects when an admin share is mounted using net.exe

## Metadata

- Rule ID: 3abd6094-7027-475f-9630-8ab9be7b9725
- Status: test
- Level: medium
- Author: oscd.community, Teymur Kheirkhabarov @HeirhabarovT, Zach Stanford @svch0st, wagga
- Date: 2020-10-05
- Modified: 2023-02-21
- Source Path: rules/windows/process_creation/proc_creation_win_net_use_mount_admin_share.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.002]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \net.exe
  - \net1.exe
- OriginalFileName:
  - net.exe
  - net1.exe
selection_cli:
  CommandLine|contains|all:
  - ' use '
  - ' \\\\*\\*$'
condition: all of selection_*
```

## False Positives

- Administrators

## References

- https://drive.google.com/file/d/1lKya3_mLnR3UQuCoiYruO3qgu052_iS_/view

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_net_use_mount_admin_share.yml)
