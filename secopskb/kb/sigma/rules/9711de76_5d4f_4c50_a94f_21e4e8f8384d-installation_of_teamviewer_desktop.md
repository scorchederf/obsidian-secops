---
sigma_id: "9711de76-5d4f-4c50-a94f-21e4e8f8384d"
title: "Installation of TeamViewer Desktop"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_install_teamviewer_desktop.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_install_teamviewer_desktop.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "9711de76-5d4f-4c50-a94f-21e4e8f8384d"
  - "Installation of TeamViewer Desktop"
attack_technique_ids:
  - "T1219.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Installation of TeamViewer Desktop

TeamViewer_Desktop.exe is create during install

## Metadata

- Rule ID: 9711de76-5d4f-4c50-a94f-21e4e8f8384d
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-01-28
- Source Path: rules/windows/file/file_event/file_event_win_install_teamviewer_desktop.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1219-remote_access_tools|T1219.002]]

## Detection

```yaml
selection:
  TargetFilename|endswith: \TeamViewer_Desktop.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1219/T1219.md#atomic-test-1---teamviewer-files-detected-test-on-windows

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_install_teamviewer_desktop.yml)
