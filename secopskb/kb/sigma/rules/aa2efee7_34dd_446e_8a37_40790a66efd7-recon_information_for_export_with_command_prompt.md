---
sigma_id: "aa2efee7-34dd-446e-8a37-40790a66efd7"
title: "Recon Information for Export with Command Prompt"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_recon.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_recon.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "aa2efee7-34dd-446e-8a37-40790a66efd7"
  - "Recon Information for Export with Command Prompt"
attack_technique_ids:
  - "T1119"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Recon Information for Export with Command Prompt

Once established within a system or network, an adversary may use automated techniques for collecting internal data.

## Metadata

- Rule ID: aa2efee7-34dd-446e-8a37-40790a66efd7
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-07-30
- Modified: 2022-09-13
- Source Path: rules/windows/process_creation/proc_creation_win_susp_recon.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1119-automated_collection|T1119]]

## Detection

```yaml
selection_image:
- Image|endswith:
  - \tree.com
  - \WMIC.exe
  - \doskey.exe
  - \sc.exe
- OriginalFileName:
  - wmic.exe
  - DOSKEY.EXE
  - sc.exe
selection_redirect:
  ParentCommandLine|contains:
  - ' > %TEMP%\'
  - ' > %TMP%\'
condition: all of selection*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1119/T1119.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_recon.yml)
