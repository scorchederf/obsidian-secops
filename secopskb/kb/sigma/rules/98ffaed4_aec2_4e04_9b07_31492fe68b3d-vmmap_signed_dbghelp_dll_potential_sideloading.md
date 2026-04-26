---
sigma_id: "98ffaed4-aec2-4e04-9b07-31492fe68b3d"
title: "VMMap Signed Dbghelp.DLL Potential Sideloading"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_vmmap_dbghelp_signed.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_vmmap_dbghelp_signed.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "98ffaed4-aec2-4e04-9b07-31492fe68b3d"
  - "VMMap Signed Dbghelp.DLL Potential Sideloading"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# VMMap Signed Dbghelp.DLL Potential Sideloading

Detects potential DLL sideloading of a signed dbghelp.dll by the Sysinternals VMMap.

## Metadata

- Rule ID: 98ffaed4-aec2-4e04-9b07-31492fe68b3d
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-09-05
- Source Path: rules/windows/image_load/image_load_side_load_vmmap_dbghelp_signed.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  ImageLoaded|contains: C:\Debuggers\dbghelp.dll
  Image|endswith:
  - \vmmap.exe
  - \vmmap64.exe
  Signed: 'true'
condition: selection
```

## False Positives

- Unknown

## References

- https://techcommunity.microsoft.com/t5/sysinternals-blog/zoomit-v7-1-procdump-2-0-for-linux-process-explorer-v17-05/ba-p/3884766

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_vmmap_dbghelp_signed.yml)
