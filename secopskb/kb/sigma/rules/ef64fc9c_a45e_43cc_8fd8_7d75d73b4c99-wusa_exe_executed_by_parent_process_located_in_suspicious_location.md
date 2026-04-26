---
sigma_id: "ef64fc9c-a45e-43cc-8fd8-7d75d73b4c99"
title: "Wusa.EXE Executed By Parent Process Located In Suspicious Location"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wusa_susp_parent_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wusa_susp_parent_execution.yml"
build_date: "2026-04-26 17:03:24"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "ef64fc9c-a45e-43cc-8fd8-7d75d73b4c99"
  - "Wusa.EXE Executed By Parent Process Located In Suspicious Location"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Wusa.EXE Executed By Parent Process Located In Suspicious Location

Detects execution of the "wusa.exe" (Windows Update Standalone Installer) utility by a parent process that is located in a suspicious location.
Attackers could instantiate an instance of "wusa.exe" in order to bypass User Account Control (UAC). They can duplicate the access token from "wusa.exe" to gain elevated privileges.

## Metadata

- Rule ID: ef64fc9c-a45e-43cc-8fd8-7d75d73b4c99
- Status: test
- Level: high
- Author: X__Junior (Nextron Systems)
- Date: 2023-11-26
- Modified: 2024-08-15
- Source Path: rules/windows/process_creation/proc_creation_win_wusa_susp_parent_execution.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_img:
  Image|endswith: \wusa.exe
selection_paths_1:
  ParentImage|contains:
  - :\Perflogs\
  - :\Users\Public\
  - :\Windows\Temp\
  - \Appdata\Local\Temp\
  - \Temporary Internet
selection_paths_2:
- ParentImage|contains|all:
  - :\Users\
  - \Favorites\
- ParentImage|contains|all:
  - :\Users\
  - \Favourites\
- ParentImage|contains|all:
  - :\Users\
  - \Contacts\
- ParentImage|contains|all:
  - :\Users\
  - \Pictures\
filter_main_msu:
  CommandLine|contains: .msu
condition: selection_img and 1 of selection_paths_* and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://www.fortinet.com/blog/threat-research/konni-campaign-distributed-via-malicious-document

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wusa_susp_parent_execution.yml)
