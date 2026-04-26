---
sigma_id: "a5ea83a7-05a5-44c1-be2e-addccbbd8c03"
title: "UAC Bypass With Fake DLL"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_uac_bypass_via_dism.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_uac_bypass_via_dism.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / image_load"
aliases:
  - "a5ea83a7-05a5-44c1-be2e-addccbbd8c03"
  - "UAC Bypass With Fake DLL"
attack_technique_ids:
  - "T1548.002"
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# UAC Bypass With Fake DLL

Attempts to load dismcore.dll after dropping it

## Metadata

- Rule ID: a5ea83a7-05a5-44c1-be2e-addccbbd8c03
- Status: test
- Level: high
- Author: oscd.community, Dmitry Uchakin
- Date: 2020-10-06
- Modified: 2022-12-25
- Source Path: rules/windows/image_load/image_load_uac_bypass_via_dism.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]
- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  Image|endswith: \dism.exe
  ImageLoaded|endswith: \dismcore.dll
filter:
  ImageLoaded: C:\Windows\System32\Dism\dismcore.dll
condition: selection and not filter
```

## False Positives

- Actions of a legitimate telnet client

## References

- https://steemit.com/utopian-io/@ah101/uac-bypassing-utility

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_uac_bypass_via_dism.yml)
