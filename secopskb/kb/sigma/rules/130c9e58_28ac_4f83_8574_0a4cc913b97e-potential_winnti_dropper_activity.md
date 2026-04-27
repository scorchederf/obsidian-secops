---
sigma_id: "130c9e58-28ac-4f83-8574-0a4cc913b97e"
title: "Potential Winnti Dropper Activity"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_redmimicry_winnti_filedrop.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_redmimicry_winnti_filedrop.yml"
build_date: "2026-04-27 19:13:54"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "130c9e58-28ac-4f83-8574-0a4cc913b97e"
  - "Potential Winnti Dropper Activity"
attack_technique_ids:
  - "T1027"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects files dropped by Winnti as described in RedMimicry Winnti playbook

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027: Obfuscated Files or Information]]

## Detection

```yaml
selection:
  TargetFilename|endswith:
  - \gthread-3.6.dll
  - \sigcmm-2.4.dll
  - \Windows\Temp\tmp.bat
condition: selection
```

## False Positives

- Unknown

## References

- https://redmimicry.com/posts/redmimicry-winnti/#dropper

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_redmimicry_winnti_filedrop.yml)
