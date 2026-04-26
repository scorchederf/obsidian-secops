---
sigma_id: "162ab1e4-6874-4564-853c-53ec3ab8be01"
title: "TeamViewer Remote Session"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_susp_teamviewer_remote_session.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_teamviewer_remote_session.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "162ab1e4-6874-4564-853c-53ec3ab8be01"
  - "TeamViewer Remote Session"
attack_technique_ids:
  - "T1219.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# TeamViewer Remote Session

Detects the creation of log files during a TeamViewer remote session

## Metadata

- Rule ID: 162ab1e4-6874-4564-853c-53ec3ab8be01
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2022-01-30
- Source Path: rules/windows/file/file_event/file_event_win_susp_teamviewer_remote_session.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1219-remote_access_tools|T1219.002]]

## Detection

```yaml
selection1:
  TargetFilename|endswith:
  - \TeamViewer\RemotePrinting\tvprint.db
  - \TeamViewer\TVNetwork.log
selection2:
  TargetFilename|contains|all:
  - \TeamViewer
  - _Logfile.log
condition: 1 of selection*
```

## False Positives

- Legitimate uses of TeamViewer in an organisation

## References

- https://www.teamviewer.com/en-us/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_teamviewer_remote_session.yml)
