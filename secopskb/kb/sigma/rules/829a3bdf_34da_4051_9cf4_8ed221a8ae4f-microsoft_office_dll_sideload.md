---
sigma_id: "829a3bdf-34da-4051-9cf4-8ed221a8ae4f"
title: "Microsoft Office DLL Sideload"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_office_dlls.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_office_dlls.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / image_load"
aliases:
  - "829a3bdf-34da-4051-9cf4-8ed221a8ae4f"
  - "Microsoft Office DLL Sideload"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Microsoft Office DLL Sideload

Detects DLL sideloading of DLLs that are part of Microsoft Office from non standard location

## Metadata

- Rule ID: 829a3bdf-34da-4051-9cf4-8ed221a8ae4f
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems), Wietze Beukema (project and research)
- Date: 2022-08-17
- Modified: 2023-03-15
- Source Path: rules/windows/image_load/image_load_side_load_office_dlls.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  ImageLoaded|endswith: \outllib.dll
filter:
  ImageLoaded|startswith:
  - C:\Program Files\Microsoft Office\OFFICE
  - C:\Program Files (x86)\Microsoft Office\OFFICE
  - C:\Program Files\Microsoft Office\Root\OFFICE
  - C:\Program Files (x86)\Microsoft Office\Root\OFFICE
condition: selection and not filter
```

## False Positives

- Unlikely

## References

- https://hijacklibs.net/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_office_dlls.yml)
