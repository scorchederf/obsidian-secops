---
sigma_id: "f576a613-2392-4067-9d1a-9345fb58d8d1"
title: "Automated Collection Command Prompt"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_automated_collection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_automated_collection.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "f576a613-2392-4067-9d1a-9345fb58d8d1"
  - "Automated Collection Command Prompt"
attack_technique_ids:
  - "T1119"
  - "T1552.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Automated Collection Command Prompt

Once established within a system or network, an adversary may use automated techniques for collecting internal data.

## Metadata

- Rule ID: f576a613-2392-4067-9d1a-9345fb58d8d1
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-07-28
- Modified: 2022-11-11
- Source Path: rules/windows/process_creation/proc_creation_win_susp_automated_collection.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1119-automated_collection|T1119]]
- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.001]]

## Detection

```yaml
selection_ext:
  CommandLine|contains:
  - .doc
  - .docx
  - .xls
  - .xlsx
  - .ppt
  - .pptx
  - .rtf
  - .pdf
  - .txt
selection_other_dir:
  CommandLine|contains|all:
  - 'dir '
  - ' /b '
  - ' /s '
selection_other_findstr:
  OriginalFileName: FINDSTR.EXE
  CommandLine|contains:
  - ' /e '
  - ' /si '
condition: selection_ext and 1 of selection_other_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1119/T1119.md
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1552.001/T1552.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_automated_collection.yml)
