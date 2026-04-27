---
sigma_id: "6ea858a8-ba71-4a12-b2cc-5d83312404c7"
title: "HackTool - Typical HiveNightmare SAM File Export"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_hktl_hivenightmare_file_exports.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_hktl_hivenightmare_file_exports.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "6ea858a8-ba71-4a12-b2cc-5d83312404c7"
  - "HackTool - Typical HiveNightmare SAM File Export"
attack_technique_ids:
  - "T1552.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects files written by the different tools that exploit HiveNightmare

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1552-unsecured_credentials#^t1552001-credentials-in-files|T1552.001: Credentials In Files]]

## Detection

```yaml
selection:
- TargetFilename|contains:
  - \hive_sam_
  - \SAM-2021-
  - \SAM-2022-
  - \SAM-2023-
  - \SAM-haxx
  - \Sam.save
- TargetFilename: C:\windows\temp\sam
condition: selection
```

## False Positives

- Files that accidentally contain these strings

## References

- https://github.com/GossiTheDog/HiveNightmare
- https://github.com/FireFart/hivenightmare/
- https://github.com/WiredPulse/Invoke-HiveNightmare
- https://twitter.com/cube0x0/status/1418920190759378944

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_hktl_hivenightmare_file_exports.yml)
