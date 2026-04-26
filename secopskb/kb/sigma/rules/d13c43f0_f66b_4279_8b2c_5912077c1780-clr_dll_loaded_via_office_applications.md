---
sigma_id: "d13c43f0-f66b-4279-8b2c-5912077c1780"
title: "CLR DLL Loaded Via Office Applications"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_office_dotnet_clr_dll_load.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_office_dotnet_clr_dll_load.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "d13c43f0-f66b-4279-8b2c-5912077c1780"
  - "CLR DLL Loaded Via Office Applications"
attack_technique_ids:
  - "T1204.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# CLR DLL Loaded Via Office Applications

Detects CLR DLL being loaded by an Office Product

## Metadata

- Rule ID: d13c43f0-f66b-4279-8b2c-5912077c1780
- Status: test
- Level: medium
- Author: Antonlovesdnb
- Date: 2020-02-19
- Modified: 2023-03-29
- Source Path: rules/windows/image_load/image_load_office_dotnet_clr_dll_load.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1204-user_execution|T1204.002]]

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
  ImageLoaded|contains: \clr.dll
condition: selection
```

## False Positives

- Unknown

## References

- https://medium.com/threatpunter/detecting-adversary-tradecraft-with-image-load-event-logging-and-eql-8de93338c16

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_office_dotnet_clr_dll_load.yml)
