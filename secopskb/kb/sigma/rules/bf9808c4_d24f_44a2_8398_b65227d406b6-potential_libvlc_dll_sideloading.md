---
sigma_id: "bf9808c4-d24f-44a2-8398-b65227d406b6"
title: "Potential Libvlc.DLL Sideloading"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_libvlc.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_libvlc.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "bf9808c4-d24f-44a2-8398-b65227d406b6"
  - "Potential Libvlc.DLL Sideloading"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Libvlc.DLL Sideloading

Detects potential DLL sideloading of "libvlc.dll", a DLL that is legitimately used by "VLC.exe"

## Metadata

- Rule ID: bf9808c4-d24f-44a2-8398-b65227d406b6
- Status: test
- Level: medium
- Author: X__Junior
- Date: 2023-04-17
- Source Path: rules/windows/image_load/image_load_side_load_libvlc.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  ImageLoaded|endswith: \libvlc.dll
filter_main_vlc:
  ImageLoaded|startswith:
  - C:\Program Files (x86)\VideoLAN\VLC\
  - C:\Program Files\VideoLAN\VLC\
condition: selection and not 1 of filter_main_*
```

## False Positives

- False positives are expected if VLC is installed in non-default locations

## References

- https://www.trendmicro.com/en_us/research/23/c/earth-preta-updated-stealthy-strategies.html
- https://hijacklibs.net/entries/3rd_party/vlc/libvlc.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_libvlc.yml)
