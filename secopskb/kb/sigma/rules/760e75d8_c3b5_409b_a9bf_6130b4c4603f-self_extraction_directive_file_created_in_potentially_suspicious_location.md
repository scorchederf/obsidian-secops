---
sigma_id: "760e75d8-c3b5-409b-a9bf-6130b4c4603f"
title: "Self Extraction Directive File Created In Potentially Suspicious Location"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_sed_file_creation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_sed_file_creation.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "760e75d8-c3b5-409b-a9bf-6130b4c4603f"
  - "Self Extraction Directive File Created In Potentially Suspicious Location"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Self Extraction Directive File Created In Potentially Suspicious Location

Detects the creation of Self Extraction Directive files (.sed) in a potentially suspicious location.
These files are used by the "iexpress.exe" utility in order to create self extracting packages.
Attackers were seen abusing this utility and creating PE files with embedded ".sed" entries.

## Metadata

- Rule ID: 760e75d8-c3b5-409b-a9bf-6130b4c4603f
- Status: test
- Level: medium
- Author: Joseliyo Sanchez, @Joseliyo_Jstnk
- Date: 2024-02-05
- Source Path: rules/windows/file/file_event/file_event_win_sed_file_creation.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  TargetFilename|contains:
  - :\ProgramData\
  - :\Temp\
  - :\Windows\System32\Tasks\
  - :\Windows\Tasks\
  - :\Windows\Temp\
  - \AppData\Local\Temp\
  TargetFilename|endswith: .sed
condition: selection
```

## False Positives

- Unknown

## References

- https://strontic.github.io/xcyclopedia/library/iexpress.exe-D594B2A33EFAFD0EABF09E3FDC05FCEA.html
- https://en.wikipedia.org/wiki/IExpress
- https://www.virustotal.com/gui/file/602f4ae507fa8de57ada079adff25a6c2a899bd25cd092d0af7e62cdb619c93c/behavior

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_sed_file_creation.yml)
