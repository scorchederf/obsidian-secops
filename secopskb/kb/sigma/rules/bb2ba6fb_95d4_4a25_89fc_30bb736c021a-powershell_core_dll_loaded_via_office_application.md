---
sigma_id: "bb2ba6fb-95d4-4a25-89fc-30bb736c021a"
title: "PowerShell Core DLL Loaded Via Office Application"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_office_powershell_dll_load.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_office_powershell_dll_load.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "bb2ba6fb-95d4-4a25-89fc-30bb736c021a"
  - "PowerShell Core DLL Loaded Via Office Application"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PowerShell Core DLL Loaded Via Office Application

Detects PowerShell core DLL being loaded by an Office Product

## Metadata

- Rule ID: bb2ba6fb-95d4-4a25-89fc-30bb736c021a
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-06-01
- Source Path: rules/windows/image_load/image_load_office_powershell_dll_load.yml

## Logsource

- category: image_load
- product: windows

## Detection

```yaml
selection:
  Image|endswith:
  - \excel.exe
  - \mspub.exe
  - \outlook.exe
  - \onenote.exe
  - \onenoteim.exe
  - \powerpnt.exe
  - \winword.exe
  ImageLoaded|contains:
  - \System.Management.Automation.Dll
  - \System.Management.Automation.ni.Dll
condition: selection
```

## False Positives

- Unknown

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_office_powershell_dll_load.yml)
