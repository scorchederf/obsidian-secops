---
sigma_id: "2b140a5c-dc02-4bb8-b6b1-8bdb45714cde"
title: "System Control Panel Item Loaded From Uncommon Location"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_cpl_from_non_system_location.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_cpl_from_non_system_location.yml"
build_date: "2026-04-26 15:01:52"
status: "test"
level: "high"
logsource: "windows / image_load"
aliases:
  - "2b140a5c-dc02-4bb8-b6b1-8bdb45714cde"
  - "System Control Panel Item Loaded From Uncommon Location"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# System Control Panel Item Loaded From Uncommon Location

Detects image load events of system control panel items (.cpl) from uncommon or non-system locations that may indicate DLL sideloading or other abuse techniques.

## Metadata

- Rule ID: 2b140a5c-dc02-4bb8-b6b1-8bdb45714cde
- Status: test
- Level: high
- Author: Anish Bogati
- Date: 2024-01-09
- Modified: 2026-02-17
- Source Path: rules/windows/image_load/image_load_side_load_cpl_from_non_system_location.yml

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
  - \appwiz.cpl
  - \bthprops.cpl
  - \hdwwiz.cpl
filter_main_legit_location:
  ImageLoaded|startswith:
  - C:\Windows\Prefetch\
  - C:\Windows\System32\
  - C:\Windows\SysWOW64\
  - C:\Windows\WinSxS\
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://www.hexacorn.com/blog/2024/01/06/1-little-known-secret-of-fondue-exe/
- https://www.hexacorn.com/blog/2024/01/01/1-little-known-secret-of-hdwwiz-exe/
- https://github.com/mhaskar/FsquirtCPLPoC
- https://securelist.com/sidewinder-apt/114089/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_cpl_from_non_system_location.yml)
