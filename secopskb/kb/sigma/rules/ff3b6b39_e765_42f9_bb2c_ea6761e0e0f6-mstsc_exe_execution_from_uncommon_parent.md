---
sigma_id: "ff3b6b39-e765-42f9-bb2c-ea6761e0e0f6"
title: "Mstsc.EXE Execution From Uncommon Parent"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_mstsc_run_local_rpd_file_susp_parent.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mstsc_run_local_rpd_file_susp_parent.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "ff3b6b39-e765-42f9-bb2c-ea6761e0e0f6"
  - "Mstsc.EXE Execution From Uncommon Parent"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Mstsc.EXE Execution From Uncommon Parent

Detects potential RDP connection via Mstsc using a local ".rdp" file located in suspicious locations.

## Metadata

- Rule ID: ff3b6b39-e765-42f9-bb2c-ea6761e0e0f6
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-04-18
- Source Path: rules/windows/process_creation/proc_creation_win_mstsc_run_local_rpd_file_susp_parent.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_parent:
  ParentImage|endswith:
  - \brave.exe
  - \CCleanerBrowser.exe
  - \chrome.exe
  - \chromium.exe
  - \firefox.exe
  - \iexplore.exe
  - \microsoftedge.exe
  - \msedge.exe
  - \opera.exe
  - \vivaldi.exe
  - \whale.exe
  - \outlook.exe
selection_img:
- Image|endswith: \mstsc.exe
- OriginalFileName: mstsc.exe
condition: all of selection_*
```

## False Positives

- Unlikely

## References

- https://www.blackhillsinfosec.com/rogue-rdp-revisiting-initial-access-methods/
- https://web.archive.org/web/20230726144748/https://blog.thickmints.dev/mintsights/detecting-rogue-rdp/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mstsc_run_local_rpd_file_susp_parent.yml)
