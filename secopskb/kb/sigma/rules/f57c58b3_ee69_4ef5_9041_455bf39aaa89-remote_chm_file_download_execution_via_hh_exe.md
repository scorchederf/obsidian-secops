---
sigma_id: "f57c58b3-ee69-4ef5-9041-455bf39aaa89"
title: "Remote CHM File Download/Execution Via HH.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hh_chm_remote_download_or_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hh_chm_remote_download_or_execution.yml"
build_date: "2026-04-26 15:01:50"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "f57c58b3-ee69-4ef5-9041-455bf39aaa89"
  - "Remote CHM File Download/Execution Via HH.EXE"
attack_technique_ids:
  - "T1218.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Remote CHM File Download/Execution Via HH.EXE

Detects the usage of "hh.exe" to execute/download remotely hosted ".chm" files.

## Metadata

- Rule ID: f57c58b3-ee69-4ef5-9041-455bf39aaa89
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-09-29
- Modified: 2024-01-31
- Source Path: rules/windows/process_creation/proc_creation_win_hh_chm_remote_download_or_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.001]]

## Detection

```yaml
selection_img:
- OriginalFileName: HH.exe
- Image|endswith: \hh.exe
selection_cli:
  CommandLine|contains:
  - http://
  - https://
  - \\\\
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://www.splunk.com/en_us/blog/security/follina-for-protocol-handlers.html
- https://github.com/redcanaryco/atomic-red-team/blob/1cf4dd51f83dcb0ebe6ade902d6157ad2dbc6ac8/atomics/T1218.001/T1218.001.md
- https://www.zscaler.com/blogs/security-research/unintentional-leak-glimpse-attack-vectors-apt37

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hh_chm_remote_download_or_execution.yml)
