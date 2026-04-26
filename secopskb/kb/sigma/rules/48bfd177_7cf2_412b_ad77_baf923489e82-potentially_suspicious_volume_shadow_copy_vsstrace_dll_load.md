---
sigma_id: "48bfd177-7cf2-412b-ad77-baf923489e82"
title: "Potentially Suspicious Volume Shadow Copy Vsstrace.dll Load"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_dll_vsstrace_susp_load.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_dll_vsstrace_susp_load.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "48bfd177-7cf2-412b-ad77-baf923489e82"
  - "Potentially Suspicious Volume Shadow Copy Vsstrace.dll Load"
attack_technique_ids:
  - "T1490"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potentially Suspicious Volume Shadow Copy Vsstrace.dll Load

Detects the image load of VSS DLL by uncommon executables

## Metadata

- Rule ID: 48bfd177-7cf2-412b-ad77-baf923489e82
- Status: test
- Level: medium
- Author: frack113
- Date: 2023-02-17
- Modified: 2025-12-03
- Source Path: rules/windows/image_load/image_load_dll_vsstrace_susp_load.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1490-inhibit_system_recovery|T1490]]

## Detection

```yaml
selection:
  ImageLoaded|endswith: \vsstrace.dll
filter_main_windows:
- Image:
  - C:\Windows\explorer.exe
  - C:\Windows\ImmersiveControlPanel\SystemSettings.exe
- Image|startswith:
  - C:\Windows\System32\
  - C:\Windows\SysWOW64\
  - C:\Windows\Temp\{
  - C:\Windows\WinSxS\
  - C:\ProgramData\Package Cache\{
filter_main_program_files:
  Image|startswith:
  - C:\Program Files\
  - C:\Program Files (x86)\
filter_optional_recovery:
  Image|startswith: C:\$WinREAgent\Scratch\
filter_main_null_image:
  Image: null
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

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_dll_vsstrace_susp_load.yml)
