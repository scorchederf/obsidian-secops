---
sigma_id: "ab90dab8-c7da-4010-9193-563528cfa347"
title: "Potentially Suspicious Self Extraction Directive File Created"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_executable_detected/file_executable_detected_win_susp_embeded_sed_file.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_executable_detected/file_executable_detected_win_susp_embeded_sed_file.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / file_executable_detected"
aliases:
  - "ab90dab8-c7da-4010-9193-563528cfa347"
  - "Potentially Suspicious Self Extraction Directive File Created"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potentially Suspicious Self Extraction Directive File Created

Detects the creation of a binary file with the ".sed" extension. The ".sed" extension stand for Self Extraction Directive files.
These files are used by the "iexpress.exe" utility in order to create self extracting packages.
Attackers were seen abusing this utility and creating PE files with embedded ".sed" entries.
Usually ".sed" files are simple ini files and not PE binaries.

## Metadata

- Rule ID: ab90dab8-c7da-4010-9193-563528cfa347
- Status: test
- Level: medium
- Author: Joseliyo Sanchez, @Joseliyo_Jstnk
- Date: 2024-02-05
- Source Path: rules/windows/file/file_executable_detected/file_executable_detected_win_susp_embeded_sed_file.yml

## Logsource

- category: file_executable_detected
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
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

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_executable_detected/file_executable_detected_win_susp_embeded_sed_file.yml)
