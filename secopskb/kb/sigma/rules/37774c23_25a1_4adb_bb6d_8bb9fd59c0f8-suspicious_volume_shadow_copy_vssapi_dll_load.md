---
sigma_id: "37774c23-25a1-4adb-bb6d-8bb9fd59c0f8"
title: "Suspicious Volume Shadow Copy Vssapi.dll Load"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_dll_vssapi_susp_load.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_dll_vssapi_susp_load.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / image_load"
aliases:
  - "37774c23-25a1-4adb-bb6d-8bb9fd59c0f8"
  - "Suspicious Volume Shadow Copy Vssapi.dll Load"
attack_technique_ids:
  - "T1490"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Volume Shadow Copy Vssapi.dll Load

Detects the image load of VSS DLL by uncommon executables

## Metadata

- Rule ID: 37774c23-25a1-4adb-bb6d-8bb9fd59c0f8
- Status: test
- Level: high
- Author: frack113
- Date: 2022-10-31
- Modified: 2025-10-17
- Source Path: rules/windows/image_load/image_load_dll_vssapi_susp_load.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1490-inhibit_system_recovery|T1490]]

## Detection

```yaml
selection:
  ImageLoaded|endswith: \vssapi.dll
filter_main_windows:
- Image:
  - C:\Windows\explorer.exe
  - C:\Windows\ImmersiveControlPanel\SystemSettings.exe
- Image|startswith:
  - C:\Windows\System32\
  - C:\Windows\SysWOW64\
  - C:\Windows\Temp\{
  - C:\Windows\WinSxS\
filter_main_program_files:
  Image|startswith:
  - C:\Program Files\
  - C:\Program Files (x86)\
filter_main_null_image:
  Image: null
filter_optional_programdata_packagecache:
  Image|startswith: C:\ProgramData\Package Cache\
filter_optional_avira:
  Image|contains|all:
  - \temp\is-
  - \avira_system_speedup.tmp
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- https://github.com/ORCx41/DeleteShadowCopies

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_dll_vssapi_susp_load.yml)
