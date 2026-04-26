---
sigma_id: "72ca7c75-bf85-45cd-aca7-255d360e423c"
title: "Potential Chrome Frame Helper DLL Sideloading"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_chrome_frame_helper.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_chrome_frame_helper.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "72ca7c75-bf85-45cd-aca7-255d360e423c"
  - "Potential Chrome Frame Helper DLL Sideloading"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Chrome Frame Helper DLL Sideloading

Detects potential DLL sideloading of "chrome_frame_helper.dll"

## Metadata

- Rule ID: 72ca7c75-bf85-45cd-aca7-255d360e423c
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), Wietze Beukema (project and research)
- Date: 2022-08-17
- Modified: 2023-05-15
- Source Path: rules/windows/image_load/image_load_side_load_chrome_frame_helper.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  ImageLoaded|endswith: \chrome_frame_helper.dll
filter_main_path:
  ImageLoaded|startswith:
  - C:\Program Files\Google\Chrome\Application\
  - C:\Program Files (x86)\Google\Chrome\Application\
filter_optional_user_path:
  ImageLoaded|contains: \AppData\local\Google\Chrome\Application\
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- https://hijacklibs.net/entries/3rd_party/google/chrome_frame_helper.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_chrome_frame_helper.yml)
