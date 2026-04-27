---
sigma_id: "6e78b74f-c762-4800-82ad-f66787f10c8a"
title: "Potential Rcdll.DLL Sideloading"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_rcdll.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_rcdll.yml"
build_date: "2026-04-27 19:13:54"
status: "test"
level: "high"
logsource: "windows / image_load"
aliases:
  - "6e78b74f-c762-4800-82ad-f66787f10c8a"
  - "Potential Rcdll.DLL Sideloading"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects potential DLL sideloading of rcdll.dll

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow#^t1574001-dll|T1574.001: DLL]]

## Detection

```yaml
selection:
  ImageLoaded|endswith: \rcdll.dll
filter:
  ImageLoaded|startswith:
  - C:\Program Files (x86)\Microsoft Visual Studio\
  - C:\Program Files (x86)\Windows Kits\
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://www.trendmicro.com/en_us/research/23/c/iron-tiger-sysupdate-adds-linux-targeting.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_rcdll.yml)
