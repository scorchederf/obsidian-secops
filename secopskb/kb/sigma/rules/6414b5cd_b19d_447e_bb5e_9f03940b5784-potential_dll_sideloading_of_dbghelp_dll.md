---
sigma_id: "6414b5cd-b19d-447e-bb5e-9f03940b5784"
title: "Potential DLL Sideloading Of DBGHELP.DLL"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_dbghelp.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_dbghelp.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "6414b5cd-b19d-447e-bb5e-9f03940b5784"
  - "Potential DLL Sideloading Of DBGHELP.DLL"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential DLL Sideloading Of DBGHELP.DLL

Detects potential DLL sideloading of "dbghelp.dll"

## Metadata

- Rule ID: 6414b5cd-b19d-447e-bb5e-9f03940b5784
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), Wietze Beukema (project and research)
- Date: 2022-10-25
- Modified: 2025-10-07
- Source Path: rules/windows/image_load/image_load_side_load_dbghelp.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  ImageLoaded|endswith: \dbghelp.dll
filter_main_generic:
  ImageLoaded|startswith:
  - C:\Program Files (x86)\
  - C:\Program Files\
  - C:\Windows\SoftwareDistribution\
  - C:\Windows\System32\
  - C:\Windows\SystemTemp\
  - C:\Windows\SysWOW64\
  - C:\Windows\WinSxS\
filter_optional_anaconda:
  ImageLoaded|endswith:
  - \Anaconda3\Lib\site-packages\vtrace\platforms\windll\amd64\dbghelp.dll
  - \Anaconda3\Lib\site-packages\vtrace\platforms\windll\i386\dbghelp.dll
filter_optional_epicgames:
  ImageLoaded|endswith:
  - \Epic Games\Launcher\Engine\Binaries\ThirdParty\DbgHelp\dbghelp.dll
  - \Epic Games\MagicLegends\x86\dbghelp.dll
filter_optional_opera:
  ImageLoaded|contains: opera\Opera Installer Temp\opera_package
  ImageLoaded|endswith: \assistant\dbghelp.dll
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Legitimate applications loading their own versions of the DLL mentioned in this rule

## References

- https://hijacklibs.net/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_dbghelp.yml)
