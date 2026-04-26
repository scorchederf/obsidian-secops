---
sigma_id: "145095eb-e273-443b-83d0-f9b519b7867b"
title: "PDF File Created By RegEdit.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_regedit_print_as_pdf.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_regedit_print_as_pdf.yml"
build_date: "2026-04-26 15:01:47"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "145095eb-e273-443b-83d0-f9b519b7867b"
  - "PDF File Created By RegEdit.EXE"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# PDF File Created By RegEdit.EXE

Detects the creation of a file with the ".pdf" extension by the "RegEdit.exe" process.
This indicates that a user is trying to print/save a registry key as a PDF in order to potentially extract sensitive information and bypass defenses.

## Metadata

- Rule ID: 145095eb-e273-443b-83d0-f9b519b7867b
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2024-07-08
- Source Path: rules/windows/file/file_event/file_event_win_regedit_print_as_pdf.yml

## Logsource

- category: file_event
- product: windows

## Detection

```yaml
selection:
  Image|endswith: \regedit.exe
  TargetFilename|endswith: .pdf
condition: selection
```

## False Positives

- Unlikely

## References

- https://sensepost.com/blog/2024/dumping-lsa-secrets-a-story-about-task-decorrelation/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_regedit_print_as_pdf.yml)
