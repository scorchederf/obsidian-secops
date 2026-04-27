---
sigma_id: "52753ea4-b3a0-4365-910d-36cff487b789"
title: "Hijack Legit RDP Session to Move Laterally"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_tsclient_filewrite_startup.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_tsclient_filewrite_startup.yml"
build_date: "2026-04-27 19:13:52"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the usage of tsclient share to place a backdoor on the RDP source machine's startup folder

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1219-remote_access_tools#^t1219002-remote-desktop-software|T1219.002: Remote Desktop Software]]

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
