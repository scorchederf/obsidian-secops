---
sigma_id: "f208d6d8-d83a-4c2c-960d-877c37da84e5"
title: "Process Launched Without Image Name"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_no_image_name.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_no_image_name.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "f208d6d8-d83a-4c2c-960d-877c37da84e5"
  - "Process Launched Without Image Name"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Process Launched Without Image Name

Detect the use of processes with no name (".exe"), which can be used to evade Image-based detections.

## Metadata

- Rule ID: f208d6d8-d83a-4c2c-960d-877c37da84e5
- Status: test
- Level: medium
- Author: Matt Anderson (Huntress)
- Date: 2024-07-23
- Source Path: rules/windows/process_creation/proc_creation_win_susp_no_image_name.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
  Image|endswith: \.exe
condition: selection
```

## False Positives

- Rare legitimate software.

## References

- https://www.huntress.com/blog/fake-browser-updates-lead-to-boinc-volunteer-computing-software

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_no_image_name.yml)
