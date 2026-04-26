---
sigma_id: "70e8e9b4-6a93-4cb7-8cde-da69502e7aff"
title: "VMGuestLib DLL Sideload"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_vmguestlib.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_vmguestlib.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "70e8e9b4-6a93-4cb7-8cde-da69502e7aff"
  - "VMGuestLib DLL Sideload"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# VMGuestLib DLL Sideload

Detects DLL sideloading of VMGuestLib.dll by the WmiApSrv service.

## Metadata

- Rule ID: 70e8e9b4-6a93-4cb7-8cde-da69502e7aff
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-12-01
- Source Path: rules/windows/image_load/image_load_side_load_vmguestlib.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  ImageLoaded|contains|all:
  - \VMware\VMware Tools\vmStatsProvider\win32
  - \vmGuestLib.dll
  Image|endswith: \Windows\System32\wbem\WmiApSrv.exe
filter:
  Signed: 'true'
condition: selection and not filter
```

## False Positives

- FP could occur if the legitimate version of vmGuestLib already exists on the system

## References

- https://decoded.avast.io/martinchlumecky/png-steganography/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_vmguestlib.yml)
