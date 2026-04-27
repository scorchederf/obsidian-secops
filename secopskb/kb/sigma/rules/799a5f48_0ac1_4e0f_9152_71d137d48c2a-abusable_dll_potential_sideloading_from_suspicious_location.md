---
sigma_id: "799a5f48-0ac1-4e0f-9152-71d137d48c2a"
title: "Abusable DLL Potential Sideloading From Suspicious Location"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_abused_dlls_susp_paths.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_abused_dlls_susp_paths.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / image_load"
aliases:
  - "799a5f48-0ac1-4e0f-9152-71d137d48c2a"
  - "Abusable DLL Potential Sideloading From Suspicious Location"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Abusable DLL Potential Sideloading From Suspicious Location

Detects potential DLL sideloading of DLLs that are known to be abused from suspicious locations

## Metadata

- Rule ID: 799a5f48-0ac1-4e0f-9152-71d137d48c2a
- Status: test
- Level: high
- Author: X__Junior (Nextron Systems)
- Date: 2023-07-11
- Source Path: rules/windows/image_load/image_load_side_load_abused_dlls_susp_paths.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection_dll:
  ImageLoaded|endswith:
  - \coreclr.dll
  - \facesdk.dll
  - \HPCustPartUI.dll
  - \libcef.dll
  - \ZIPDLL.dll
selection_folders_1:
  ImageLoaded|contains:
  - :\Perflogs\
  - :\Users\Public\
  - \Temporary Internet
  - \Windows\Temp\
selection_folders_2:
- ImageLoaded|contains|all:
  - :\Users\
  - \Favorites\
- ImageLoaded|contains|all:
  - :\Users\
  - \Favourites\
- ImageLoaded|contains|all:
  - :\Users\
  - \Contacts\
- ImageLoaded|contains|all:
  - :\Users\
  - \Pictures\
condition: selection_dll and 1 of selection_folders_*
```

## False Positives

- Unknown

## References

- https://www.trendmicro.com/en_us/research/23/f/behind-the-scenes-unveiling-the-hidden-workings-of-earth-preta.html
- https://research.checkpoint.com/2023/beyond-the-horizon-traveling-the-world-on-camaro-dragons-usb-flash-drives/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_abused_dlls_susp_paths.yml)
