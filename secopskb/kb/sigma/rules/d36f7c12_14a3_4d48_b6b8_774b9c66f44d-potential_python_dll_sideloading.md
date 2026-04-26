---
sigma_id: "d36f7c12-14a3-4d48-b6b8-774b9c66f44d"
title: "Potential Python DLL SideLoading"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_python.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_python.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "d36f7c12-14a3-4d48-b6b8-774b9c66f44d"
  - "Potential Python DLL SideLoading"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Python DLL SideLoading

Detects potential DLL sideloading of Python DLL files.

## Metadata

- Rule ID: d36f7c12-14a3-4d48-b6b8-774b9c66f44d
- Status: test
- Level: medium
- Author: Swachchhanda Shrawan Poudel
- Date: 2024-10-06
- Modified: 2025-08-18
- Source Path: rules/windows/image_load/image_load_side_load_python.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  ImageLoaded|endswith:
  - \python39.dll
  - \python310.dll
  - \python311.dll
  - \python312.dll
filter_main_default_install_paths:
- ImageLoaded|startswith:
  - C:\Program Files\Python3
  - C:\Program Files (x86)\Python3
- ImageLoaded|contains: \AppData\Local\Programs\Python\Python3
filter_optional_visual_studio:
  ImageLoaded|startswith: C:\Program Files\Microsoft Visual Studio\
filter_optional_anaconda:
  ImageLoaded|startswith: C:\ProgramData\Anaconda3\
filter_optional_cpython:
  ImageLoaded|contains:
  - \cpython\externals\
  - \cpython\PCbuild\
filter_optional_pyinstaller:
  ImageLoaded|startswith: C:\Users
  ImageLoaded|contains: \AppData\Local\Temp\_MEI
filter_main_legit_signature_details:
  Product: Python
  Signed: 'true'
  Description: Python
  Company: Python Software Foundation
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Legitimate software using Python DLLs

## References

- https://www.securonix.com/blog/seolurker-attack-campaign-uses-seo-poisoning-fake-google-ads-to-install-malware/
- https://thedfirreport.com/2024/09/30/nitrogen-campaign-drops-sliver-and-ends-with-blackcat-ransomware/
- https://github.com/wietze/HijackLibs/tree/dc9c9f2f94e6872051dab58fbafb043fdd8b4176/yml/3rd_party/python

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_python.yml)
