---
sigma_id: "30d07da2-83ab-45d8-ae75-ec7c0edcaffc"
title: "Renamed BOINC Client Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_renamed_boinc.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_boinc.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "30d07da2-83ab-45d8-ae75-ec7c0edcaffc"
  - "Renamed BOINC Client Execution"
attack_technique_ids:
  - "T1553"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Renamed BOINC Client Execution

Detects the execution of a renamed BOINC binary.

## Metadata

- Rule ID: 30d07da2-83ab-45d8-ae75-ec7c0edcaffc
- Status: test
- Level: medium
- Author: Matt Anderson (Huntress)
- Date: 2024-07-23
- Source Path: rules/windows/process_creation/proc_creation_win_renamed_boinc.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1553-subvert_trust_controls|T1553]]

## Detection

```yaml
selection:
  OriginalFileName: BOINC.exe
filter_main_legit_name:
  Image|endswith: \BOINC.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://boinc.berkeley.edu/
- https://www.virustotal.com/gui/file/91e405e8a527023fb8696624e70498ae83660fe6757cef4871ce9bcc659264d3/details
- https://www.huntress.com/blog/fake-browser-updates-lead-to-boinc-volunteer-computing-software

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_boinc.yml)
