---
sigma_id: "b6188d2f-b3c4-4d2c-a17d-9706e0851af0"
title: "Potential Goopdate.DLL Sideloading"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_goopdate.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_goopdate.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "b6188d2f-b3c4-4d2c-a17d-9706e0851af0"
  - "Potential Goopdate.DLL Sideloading"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Goopdate.DLL Sideloading

Detects potential DLL sideloading of "goopdate.dll", a DLL used by googleupdate.exe

## Metadata

- Rule ID: b6188d2f-b3c4-4d2c-a17d-9706e0851af0
- Status: test
- Level: medium
- Author: X__Junior (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-05-15
- Modified: 2025-10-07
- Source Path: rules/windows/image_load/image_load_side_load_goopdate.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  ImageLoaded|endswith: \goopdate.dll
filter_main_generic:
  ImageLoaded|startswith:
  - C:\Program Files (x86)\
  - C:\Program Files\
filter_optional_dropbox_installer_temp:
  Image|contains|all:
  - \AppData\Local\Temp\GUM
  - .tmp\Dropbox
  ImageLoaded|contains|all:
  - \AppData\Local\Temp\GUM
  - .tmp\goopdate.dll
filter_optional_googleupdate_temp:
  Image|contains:
  - \AppData\Local\Temp\GUM
  - :\Windows\SystemTemp\GUM
  Image|endswith: .tmp\GoogleUpdate.exe
  ImageLoaded|contains:
  - \AppData\Local\Temp\GUM
  - :\Windows\SystemTemp\GUM
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- False positives are expected from Google Chrome installations running from user locations (AppData) and other custom locations. Apply additional filters accordingly.
- Other third party chromium browsers located in AppData

## References

- https://www.ncsc.gov.uk/static-assets/documents/malware-analysis-reports/goofy-guineapig/NCSC-MAR-Goofy-Guineapig.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_goopdate.yml)
