---
sigma_id: "44143844-0631-49ab-97a0-96387d6b2d7c"
title: "File Download Using Notepad++ GUP Utility"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_gup_download.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_gup_download.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "44143844-0631-49ab-97a0-96387d6b2d7c"
  - "File Download Using Notepad++ GUP Utility"
attack_technique_ids:
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# File Download Using Notepad++ GUP Utility

Detects execution of the Notepad++ updater (gup) from a process other than Notepad++ to download files.

## Metadata

- Rule ID: 44143844-0631-49ab-97a0-96387d6b2d7c
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-06-10
- Modified: 2023-03-02
- Source Path: rules/windows/process_creation/proc_creation_win_gup_download.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detection

```yaml
selection_img:
- Image|endswith: \GUP.exe
- OriginalFileName: gup.exe
selection_cli:
  CommandLine|contains|all:
  - ' -unzipTo '
  - http
filter:
  ParentImage|endswith: \notepad++.exe
condition: all of selection* and not filter
```

## False Positives

- Other parent processes other than notepad++ using GUP that are not currently identified

## References

- https://twitter.com/nas_bench/status/1535322182863179776

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_gup_download.yml)
