---
sigma_id: "828af599-4c53-4ed2-ba4a-a9f835c434ea"
title: "Fax Service DLL Search Order Hijack"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_ualapi.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_ualapi.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / image_load"
aliases:
  - "828af599-4c53-4ed2-ba4a-a9f835c434ea"
  - "Fax Service DLL Search Order Hijack"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Fax Service DLL Search Order Hijack

The Fax service attempts to load ualapi.dll, which is non-existent. An attacker can then (side)load their own malicious DLL using this service.

## Metadata

- Rule ID: 828af599-4c53-4ed2-ba4a-a9f835c434ea
- Status: test
- Level: high
- Author: NVISO
- Date: 2020-05-04
- Modified: 2022-06-02
- Source Path: rules/windows/image_load/image_load_side_load_ualapi.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  Image|endswith: \fxssvc.exe
  ImageLoaded|endswith: ualapi.dll
filter:
  ImageLoaded|startswith: C:\Windows\WinSxS\
condition: selection and not filter
```

## False Positives

- Unlikely

## References

- https://windows-internals.com/faxing-your-way-to-system/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_ualapi.yml)
