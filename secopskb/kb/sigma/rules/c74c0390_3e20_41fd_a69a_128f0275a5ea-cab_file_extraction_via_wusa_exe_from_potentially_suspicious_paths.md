---
sigma_id: "c74c0390-3e20-41fd-a69a-128f0275a5ea"
title: "Cab File Extraction Via Wusa.EXE From Potentially Suspicious Paths"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wusa_cab_files_extraction_from_susp_paths.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wusa_cab_files_extraction_from_susp_paths.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "c74c0390-3e20-41fd-a69a-128f0275a5ea"
  - "Cab File Extraction Via Wusa.EXE From Potentially Suspicious Paths"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Cab File Extraction Via Wusa.EXE From Potentially Suspicious Paths

Detects the execution of the "wusa.exe" (Windows Update Standalone Installer) utility to extract ".cab" files using the "/extract" argument from potentially suspicious paths.

## Metadata

- Rule ID: c74c0390-3e20-41fd-a69a-128f0275a5ea
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-05
- Modified: 2023-11-28
- Source Path: rules/windows/process_creation/proc_creation_win_wusa_cab_files_extraction_from_susp_paths.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_root:
  Image|endswith: \wusa.exe
  CommandLine|contains: '/extract:'
selection_paths:
  CommandLine|contains:
  - :\PerfLogs\
  - :\Users\Public\
  - :\Windows\Temp\
  - \Appdata\Local\Temp\
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://web.archive.org/web/20180331144337/https://www.fireeye.com/blog/threat-research/2018/03/sanny-malware-delivery-method-updated-in-recently-observed-attacks.html
- https://www.echotrail.io/insights/search/wusa.exe/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wusa_cab_files_extraction_from_susp_paths.yml)
