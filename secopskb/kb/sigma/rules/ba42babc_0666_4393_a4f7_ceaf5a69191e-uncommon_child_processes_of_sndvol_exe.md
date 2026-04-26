---
sigma_id: "ba42babc-0666-4393-a4f7-ceaf5a69191e"
title: "Uncommon Child Processes Of SndVol.exe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sndvol_susp_child_processes.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sndvol_susp_child_processes.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "ba42babc-0666-4393-a4f7-ceaf5a69191e"
  - "Uncommon Child Processes Of SndVol.exe"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Uncommon Child Processes Of SndVol.exe

Detects potentially uncommon child processes of SndVol.exe (the Windows volume mixer)

## Metadata

- Rule ID: ba42babc-0666-4393-a4f7-ceaf5a69191e
- Status: test
- Level: medium
- Author: X__Junior (Nextron Systems)
- Date: 2023-06-09
- Source Path: rules/windows/process_creation/proc_creation_win_sndvol_susp_child_processes.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
  ParentImage|endswith: \SndVol.exe
filter_main_rundll32:
  Image|endswith: \rundll32.exe
  CommandLine|contains: ' shell32.dll,Control_RunDLL '
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://twitter.com/Max_Mal_/status/1661322732456353792

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sndvol_susp_child_processes.yml)
