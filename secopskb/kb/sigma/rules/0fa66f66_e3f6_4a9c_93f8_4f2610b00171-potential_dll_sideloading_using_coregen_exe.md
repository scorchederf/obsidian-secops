---
sigma_id: "0fa66f66-e3f6-4a9c-93f8-4f2610b00171"
title: "Potential DLL Sideloading Using Coregen.exe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_coregen.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_coregen.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "0fa66f66-e3f6-4a9c-93f8-4f2610b00171"
  - "Potential DLL Sideloading Using Coregen.exe"
attack_technique_ids:
  - "T1218"
  - "T1055"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential DLL Sideloading Using Coregen.exe

Detect usage of the "coregen.exe" (Microsoft CoreCLR Native Image Generator) binary to sideload arbitrary DLLs.

## Metadata

- Rule ID: 0fa66f66-e3f6-4a9c-93f8-4f2610b00171
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-12-31
- Source Path: rules/windows/image_load/image_load_side_load_coregen.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]
- [[kb/attack/techniques/T1055-process_injection|T1055]]

## Detection

```yaml
selection:
  Image|endswith: \coregen.exe
filter_main_legit_paths:
  ImageLoaded|startswith:
  - C:\Program Files (x86)\Microsoft Silverlight\
  - C:\Program Files\Microsoft Silverlight\
  - C:\Windows\System32\
  - C:\Windows\SysWOW64\
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/OtherMSBinaries/Coregen/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_coregen.yml)
