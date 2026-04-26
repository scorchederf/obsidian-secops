---
sigma_id: "1723e720-616d-4ddc-ab02-f7e3685a4713"
title: "Rundll32 Spawned Via Explorer.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rundll32_parent_explorer.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_parent_explorer.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "1723e720-616d-4ddc-ab02-f7e3685a4713"
  - "Rundll32 Spawned Via Explorer.EXE"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Rundll32 Spawned Via Explorer.EXE

Detects execution of "rundll32.exe" with a parent process of Explorer.exe. This has been observed by variants of Raspberry Robin, as first reported by Red Canary.

## Metadata

- Rule ID: 1723e720-616d-4ddc-ab02-f7e3685a4713
- Status: test
- Level: medium
- Author: CD_ROM_
- Date: 2022-05-21
- Modified: 2023-08-31
- Source Path: rules/windows/process_creation/proc_creation_win_rundll32_parent_explorer.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_parent:
  ParentImage|endswith: \explorer.exe
selection_img:
- Image|endswith: \rundll32.exe
- OriginalFileName: RUNDLL32.EXE
filter_main_generic:
- CommandLine|contains: ' C:\Windows\System32\'
- CommandLine|endswith: ' -localserver 22d8c27b-47a1-48d1-ad08-7da7abd79617'
condition: all of selection_* and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://redcanary.com/blog/raspberry-robin/
- https://thedfirreport.com/2022/09/26/bumblebee-round-two/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_parent_explorer.yml)
