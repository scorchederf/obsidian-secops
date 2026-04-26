---
sigma_id: "2158f96f-43c2-43cb-952a-ab4580f32382"
title: "Screen Capture Activity Via Psr.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_psr_capture_screenshots.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_psr_capture_screenshots.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "2158f96f-43c2-43cb-952a-ab4580f32382"
  - "Screen Capture Activity Via Psr.EXE"
attack_technique_ids:
  - "T1113"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Screen Capture Activity Via Psr.EXE

Detects execution of Windows Problem Steps Recorder (psr.exe), a utility used to record the user screen and clicks.

## Metadata

- Rule ID: 2158f96f-43c2-43cb-952a-ab4580f32382
- Status: test
- Level: medium
- Author: Beyu Denis, oscd.community
- Date: 2019-10-12
- Modified: 2024-01-04
- Source Path: rules/windows/process_creation/proc_creation_win_psr_capture_screenshots.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1113-screen_capture|T1113]]

## Detection

```yaml
selection:
  Image|endswith: \Psr.exe
  CommandLine|contains:
  - /start
  - -start
condition: selection
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Binaries/Psr/
- https://web.archive.org/web/20200229201156/https://www.sans.org/cyber-security-summit/archives/file/summit-archive-1493861893.pdf
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1560.001/T1560.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_psr_capture_screenshots.yml)
