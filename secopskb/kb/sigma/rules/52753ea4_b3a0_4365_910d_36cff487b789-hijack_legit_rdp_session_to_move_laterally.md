---
sigma_id: "52753ea4-b3a0-4365-910d-36cff487b789"
title: "Hijack Legit RDP Session to Move Laterally"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_tsclient_filewrite_startup.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_tsclient_filewrite_startup.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "52753ea4-b3a0-4365-910d-36cff487b789"
  - "Hijack Legit RDP Session to Move Laterally"
attack_technique_ids:
  - "T1219.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Hijack Legit RDP Session to Move Laterally

Detects the usage of tsclient share to place a backdoor on the RDP source machine's startup folder

## Metadata

- Rule ID: 52753ea4-b3a0-4365-910d-36cff487b789
- Status: test
- Level: high
- Author: Samir Bousseaden
- Date: 2019-02-21
- Modified: 2021-11-27
- Source Path: rules/windows/file/file_event/file_event_win_tsclient_filewrite_startup.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1219-remote_access_tools|T1219.002]]

## Detection

```yaml
selection:
  Image|endswith: \mstsc.exe
  TargetFilename|contains: \Microsoft\Windows\Start Menu\Programs\Startup\
condition: selection
```

## False Positives

- Unlikely

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_tsclient_filewrite_startup.yml)
