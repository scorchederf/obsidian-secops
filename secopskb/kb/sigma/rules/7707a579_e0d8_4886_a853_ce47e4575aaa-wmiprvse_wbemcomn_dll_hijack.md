---
sigma_id: "7707a579-e0d8-4886-a853-ce47e4575aaa"
title: "Wmiprvse Wbemcomn DLL Hijack"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_wmiprvse_wbemcomn_dll_hijack.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_wmiprvse_wbemcomn_dll_hijack.yml"
build_date: "2026-04-26 17:03:24"
status: "test"
level: "high"
logsource: "windows / image_load"
aliases:
  - "7707a579-e0d8-4886-a853-ce47e4575aaa"
  - "Wmiprvse Wbemcomn DLL Hijack"
attack_technique_ids:
  - "T1047"
  - "T1021.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Wmiprvse Wbemcomn DLL Hijack

Detects a threat actor creating a file named `wbemcomn.dll` in the `C:\Windows\System32\wbem\` directory over the network and loading it for a WMI DLL Hijack scenario.

## Metadata

- Rule ID: 7707a579-e0d8-4886-a853-ce47e4575aaa
- Status: test
- Level: high
- Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research)
- Date: 2020-10-12
- Modified: 2022-10-09
- Source Path: rules/windows/image_load/image_load_wmiprvse_wbemcomn_dll_hijack.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]
- [[kb/attack/techniques/T1021-remote_services|T1021.002]]

## Detection

```yaml
selection:
  Image|endswith: \wmiprvse.exe
  ImageLoaded|endswith: \wbem\wbemcomn.dll
condition: selection
```

## False Positives

- Unknown

## References

- https://threathunterplaybook.com/hunts/windows/201009-RemoteWMIWbemcomnDLLHijack/notebook.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_wmiprvse_wbemcomn_dll_hijack.yml)
