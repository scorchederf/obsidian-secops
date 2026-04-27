---
sigma_id: "b2b048b0-7857-4380-b0fb-d3f0ab820b71"
title: "Self Extracting Package Creation Via Iexpress.EXE From Potentially Suspicious Location"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_iexpress_susp_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_iexpress_susp_execution.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "b2b048b0-7857-4380-b0fb-d3f0ab820b71"
  - "Self Extracting Package Creation Via Iexpress.EXE From Potentially Suspicious Location"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Self Extracting Package Creation Via Iexpress.EXE From Potentially Suspicious Location

Detects the use of iexpress.exe to create binaries via Self Extraction Directive (SED) files located in potentially suspicious locations.
This behavior has been observed in-the-wild by different threat actors.

## Metadata

- Rule ID: b2b048b0-7857-4380-b0fb-d3f0ab820b71
- Status: test
- Level: high
- Author: Joseliyo Sanchez, @Joseliyo_Jstnk, Nasreddine Bencherchali (Nextron Systems)
- Date: 2024-02-05
- Modified: 2024-06-04
- Source Path: rules/windows/process_creation/proc_creation_win_iexpress_susp_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_img:
- Image|endswith: \iexpress.exe
- OriginalFileName: IEXPRESS.exe
selection_cli:
  CommandLine|contains|windash: ' /n '
selection_paths:
  CommandLine|contains:
  - :\ProgramData\
  - :\Temp\
  - :\Windows\System32\Tasks\
  - :\Windows\Tasks\
  - :\Windows\Temp\
  - \AppData\Local\Temp\
condition: all of selection_*
```

## False Positives

- Administrators building packages using iexpress.exe

## References

- https://strontic.github.io/xcyclopedia/library/iexpress.exe-D594B2A33EFAFD0EABF09E3FDC05FCEA.html
- https://en.wikipedia.org/wiki/IExpress
- https://decoded.avast.io/janvojtesek/raspberry-robins-roshtyak-a-little-lesson-in-trickery/
- https://www.virustotal.com/gui/file/602f4ae507fa8de57ada079adff25a6c2a899bd25cd092d0af7e62cdb619c93c/behavior

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_iexpress_susp_execution.yml)
