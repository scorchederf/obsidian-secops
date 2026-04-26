---
sigma_id: "3d0ed417-3d94-4963-a562-4a92c940656a"
title: "Creation of a Diagcab"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_susp_diagcab.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_diagcab.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "3d0ed417-3d94-4963-a562-4a92c940656a"
  - "Creation of a Diagcab"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Creation of a Diagcab

Detects the creation of diagcab file, which could be caused by some legitimate installer or is a sign of exploitation (review the filename and its location)

## Metadata

- Rule ID: 3d0ed417-3d94-4963-a562-4a92c940656a
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-06-08
- Source Path: rules/windows/file/file_event/file_event_win_susp_diagcab.yml

## Logsource

- category: file_event
- product: windows

## Detection

```yaml
selection:
  TargetFilename|endswith: .diagcab
condition: selection
```

## False Positives

- Legitimate microsoft diagcab

## References

- https://threadreaderapp.com/thread/1533879688141086720.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_diagcab.yml)
