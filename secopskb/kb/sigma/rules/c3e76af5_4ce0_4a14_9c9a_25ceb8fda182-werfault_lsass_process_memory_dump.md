---
sigma_id: "c3e76af5-4ce0-4a14-9c9a-25ceb8fda182"
title: "WerFault LSASS Process Memory Dump"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_lsass_werfault_dump.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_lsass_werfault_dump.yml"
build_date: "2026-04-27 19:13:59"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "c3e76af5-4ce0-4a14-9c9a-25ceb8fda182"
  - "WerFault LSASS Process Memory Dump"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects WerFault creating a dump file with a name that indicates that the dump file could be an LSASS process memory, which contains user credentials

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]

## Detection

```yaml
selection:
  Image: C:\WINDOWS\system32\WerFault.exe
  TargetFilename|contains:
  - \lsass
  - lsass.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/helpsystems/nanodump

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_lsass_werfault_dump.yml)
