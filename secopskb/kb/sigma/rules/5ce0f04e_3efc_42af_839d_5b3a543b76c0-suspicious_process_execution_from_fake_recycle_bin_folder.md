---
sigma_id: "5ce0f04e-3efc-42af-839d-5b3a543b76c0"
title: "Suspicious Process Execution From Fake Recycle.Bin Folder"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_recycle_bin_fake_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_recycle_bin_fake_execution.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "5ce0f04e-3efc-42af-839d-5b3a543b76c0"
  - "Suspicious Process Execution From Fake Recycle.Bin Folder"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Process Execution From Fake Recycle.Bin Folder

Detects process execution from a fake recycle bin folder, often used to avoid security solution.

## Metadata

- Rule ID: 5ce0f04e-3efc-42af-839d-5b3a543b76c0
- Status: test
- Level: high
- Author: X__Junior (Nextron Systems)
- Date: 2023-07-12
- Modified: 2023-12-11
- Source Path: rules/windows/process_creation/proc_creation_win_susp_recycle_bin_fake_execution.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
  Image|contains:
  - RECYCLERS.BIN\
  - RECYCLER.BIN\
condition: selection
```

## False Positives

- Unlikely

## References

- https://www.mandiant.com/resources/blog/infected-usb-steal-secrets
- https://unit42.paloaltonetworks.com/cloaked-ursa-phishing/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_recycle_bin_fake_execution.yml)
