---
sigma_id: "ff0f2b05-09db-4095-b96d-1b75ca24894a"
title: "DotNET Assembly DLL Loaded Via Office Application"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_office_dotnet_assembly_dll_load.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_office_dotnet_assembly_dll_load.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "ff0f2b05-09db-4095-b96d-1b75ca24894a"
  - "DotNET Assembly DLL Loaded Via Office Application"
attack_technique_ids:
  - "T1204.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# DotNET Assembly DLL Loaded Via Office Application

Detects any assembly DLL being loaded by an Office Product

## Metadata

- Rule ID: ff0f2b05-09db-4095-b96d-1b75ca24894a
- Status: test
- Level: medium
- Author: Antonlovesdnb
- Date: 2020-02-19
- Modified: 2023-03-29
- Source Path: rules/windows/image_load/image_load_office_dotnet_assembly_dll_load.yml

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
  - \onenote.exe
  - \onenoteim.exe
  - \outlook.exe
  - \powerpnt.exe
  - \winword.exe
  ImageLoaded|startswith: C:\Windows\assembly\
condition: selection
```

## False Positives

- Unknown

## References

- https://medium.com/threatpunter/detecting-adversary-tradecraft-with-image-load-event-logging-and-eql-8de93338c16

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_office_dotnet_assembly_dll_load.yml)
