---
sigma_id: "84b1ecf9-6eff-4004-bafb-bae5c0e251b2"
title: "Potentially Suspicious GoogleUpdate Child Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_googleupdate_susp_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_googleupdate_susp_child_process.yml"
build_date: "2026-04-26 15:01:49"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "84b1ecf9-6eff-4004-bafb-bae5c0e251b2"
  - "Potentially Suspicious GoogleUpdate Child Process"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potentially Suspicious GoogleUpdate Child Process

Detects potentially suspicious child processes of "GoogleUpdate.exe"

## Metadata

- Rule ID: 84b1ecf9-6eff-4004-bafb-bae5c0e251b2
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-05-15
- Modified: 2023-05-22
- Source Path: rules/windows/process_creation/proc_creation_win_googleupdate_susp_child_process.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
  ParentImage|endswith: \GoogleUpdate.exe
filter_main_known_legit:
- Image|contains: \Google
- Image|endswith:
  - \setup.exe
  - chrome_updater.exe
  - chrome_installer.exe
filter_main_image_null:
  Image: null
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://www.ncsc.gov.uk/static-assets/documents/malware-analysis-reports/goofy-guineapig/NCSC-MAR-Goofy-Guineapig.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_googleupdate_susp_child_process.yml)
