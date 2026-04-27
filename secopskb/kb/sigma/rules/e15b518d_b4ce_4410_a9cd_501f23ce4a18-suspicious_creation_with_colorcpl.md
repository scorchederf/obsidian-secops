---
sigma_id: "e15b518d-b4ce-4410-a9cd-501f23ce4a18"
title: "Suspicious Creation with Colorcpl"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_susp_colorcpl.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_colorcpl.yml"
build_date: "2026-04-27 19:13:56"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "e15b518d-b4ce-4410-a9cd-501f23ce4a18"
  - "Suspicious Creation with Colorcpl"
attack_technique_ids:
  - "T1564"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Once executed, colorcpl.exe will copy the arbitrary file to c:\windows\system32\spool\drivers\color\

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1564-hide_artifacts|T1564: Hide Artifacts]]

## Detection

```yaml
selection:
  Image|endswith: \colorcpl.exe
filter_ext:
  TargetFilename|endswith:
  - .icm
  - .gmmp
  - .cdmp
  - .camp
condition: selection and not 1 of filter_*
```

## False Positives

- Unknown

## References

- https://twitter.com/eral4m/status/1480468728324231172?s=20

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_colorcpl.yml)
