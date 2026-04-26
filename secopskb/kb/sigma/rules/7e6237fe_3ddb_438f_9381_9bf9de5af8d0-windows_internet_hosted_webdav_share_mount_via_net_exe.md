---
sigma_id: "7e6237fe-3ddb-438f-9381-9bf9de5af8d0"
title: "Windows Internet Hosted WebDav Share Mount Via Net.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_net_use_mount_internet_share.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_net_use_mount_internet_share.yml"
build_date: "2026-04-26 15:01:55"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "7e6237fe-3ddb-438f-9381-9bf9de5af8d0"
  - "Windows Internet Hosted WebDav Share Mount Via Net.EXE"
attack_technique_ids:
  - "T1021.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Windows Internet Hosted WebDav Share Mount Via Net.EXE

Detects when an internet hosted webdav share is mounted using the "net.exe" utility

## Metadata

- Rule ID: 7e6237fe-3ddb-438f-9381-9bf9de5af8d0
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-02-21
- Modified: 2023-07-25
- Source Path: rules/windows/process_creation/proc_creation_win_net_use_mount_internet_share.yml

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
  - ' http'
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://drive.google.com/file/d/1lKya3_mLnR3UQuCoiYruO3qgu052_iS_/view

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_net_use_mount_internet_share.yml)
