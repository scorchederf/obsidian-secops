---
sigma_id: "6ec86d9e-912e-4726-91a2-209359b999b9"
title: "Amsi.DLL Loaded Via LOLBIN Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_dll_amsi_suspicious_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_dll_amsi_suspicious_process.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "6ec86d9e-912e-4726-91a2-209359b999b9"
  - "Amsi.DLL Loaded Via LOLBIN Process"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Amsi.DLL Loaded Via LOLBIN Process

Detects loading of "Amsi.dll" by a living of the land process. This could be an indication of a "PowerShell without PowerShell" attack

## Metadata

- Rule ID: 6ec86d9e-912e-4726-91a2-209359b999b9
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-06-01
- Modified: 2025-10-07
- Source Path: rules/windows/image_load/image_load_dll_amsi_suspicious_process.yml

## Logsource

- category: image_load
- product: windows

## Detection

```yaml
selection:
  ImageLoaded|endswith: \amsi.dll
  Image|endswith:
  - \ExtExport.exe
  - \odbcconf.exe
  - \rundll32.exe
condition: selection
```

## False Positives

- Unknown

## References

- Internal Research
- https://www.paloaltonetworks.com/blog/security-operations/stopping-powershell-without-powershell/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_dll_amsi_suspicious_process.yml)
