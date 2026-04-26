---
sigma_id: "f117933c-980c-4f78-b384-e3d838111165"
title: "Windows Share Mount Via Net.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_net_use_mount_share.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_net_use_mount_share.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "f117933c-980c-4f78-b384-e3d838111165"
  - "Windows Share Mount Via Net.EXE"
attack_technique_ids:
  - "T1021.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows Share Mount Via Net.EXE

Detects when a share is mounted using the "net.exe" utility

## Metadata

- Rule ID: f117933c-980c-4f78-b384-e3d838111165
- Status: test
- Level: low
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-02-02
- Modified: 2023-02-21
- Source Path: rules/windows/process_creation/proc_creation_win_net_use_mount_share.yml

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
  CommandLine|contains:
  - ' use '
  - ' \\\\'
condition: all of selection_*
```

## False Positives

- Legitimate activity by administrators and scripts

## References

- https://drive.google.com/file/d/1lKya3_mLnR3UQuCoiYruO3qgu052_iS_/view

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_net_use_mount_share.yml)
