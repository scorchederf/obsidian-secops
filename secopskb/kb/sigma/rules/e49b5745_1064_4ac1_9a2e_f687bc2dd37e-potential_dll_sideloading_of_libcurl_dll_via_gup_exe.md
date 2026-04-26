---
sigma_id: "e49b5745-1064-4ac1-9a2e-f687bc2dd37e"
title: "Potential DLL Sideloading Of Libcurl.DLL Via GUP.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_gup_libcurl.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_gup_libcurl.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "e49b5745-1064-4ac1-9a2e-f687bc2dd37e"
  - "Potential DLL Sideloading Of Libcurl.DLL Via GUP.EXE"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential DLL Sideloading Of Libcurl.DLL Via GUP.EXE

Detects potential DLL sideloading of "libcurl.dll" by the "gup.exe" process from an uncommon location

## Metadata

- Rule ID: e49b5745-1064-4ac1-9a2e-f687bc2dd37e
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-05-05
- Source Path: rules/windows/image_load/image_load_side_load_gup_libcurl.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  Image|endswith: \gup.exe
  ImageLoaded|endswith: \libcurl.dll
filter_main_notepad_plusplus:
  Image|endswith: \Notepad++\updater\GUP.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://labs.withsecure.com/publications/fin7-target-veeam-servers

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_gup_libcurl.yml)
