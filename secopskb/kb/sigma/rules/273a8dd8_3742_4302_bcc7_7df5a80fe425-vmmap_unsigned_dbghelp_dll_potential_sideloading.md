---
sigma_id: "273a8dd8-3742-4302-bcc7-7df5a80fe425"
title: "VMMap Unsigned Dbghelp.DLL Potential Sideloading"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_vmmap_dbghelp_unsigned.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_vmmap_dbghelp_unsigned.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / image_load"
aliases:
  - "273a8dd8-3742-4302-bcc7-7df5a80fe425"
  - "VMMap Unsigned Dbghelp.DLL Potential Sideloading"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# VMMap Unsigned Dbghelp.DLL Potential Sideloading

Detects potential DLL sideloading of an unsigned dbghelp.dll by the Sysinternals VMMap.

## Metadata

- Rule ID: 273a8dd8-3742-4302-bcc7-7df5a80fe425
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-07-28
- Modified: 2023-09-05
- Source Path: rules/windows/image_load/image_load_side_load_vmmap_dbghelp_unsigned.yml

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
filter_main_signed:
  Signed: 'true'
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://techcommunity.microsoft.com/t5/sysinternals-blog/zoomit-v7-1-procdump-2-0-for-linux-process-explorer-v17-05/ba-p/3884766

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_vmmap_dbghelp_unsigned.yml)
