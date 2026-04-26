---
sigma_id: "cb7c4a03-2871-43c0-9bbb-18bbdb079896"
title: "Unmount Share Via Net.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_net_share_unmount.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_net_share_unmount.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "cb7c4a03-2871-43c0-9bbb-18bbdb079896"
  - "Unmount Share Via Net.EXE"
attack_technique_ids:
  - "T1070.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Unmount Share Via Net.EXE

Detects when when a mounted share is removed. Adversaries may remove share connections that are no longer useful in order to clean up traces of their operation

## Metadata

- Rule ID: cb7c4a03-2871-43c0-9bbb-18bbdb079896
- Status: test
- Level: low
- Author: oscd.community, @redcanary, Zach Stanford @svch0st
- Date: 2020-10-08
- Modified: 2023-02-21
- Source Path: rules/windows/process_creation/proc_creation_win_net_share_unmount.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070.005]]

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
  - share
  - /delete
condition: all of selection*
```

## False Positives

- Administrators or Power users may remove their shares via cmd line

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1070.005/T1070.005.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_net_share_unmount.yml)
