---
sigma_id: "90217a70-13fc-48e4-b3db-0d836c5824ac"
title: "GAC DLL Loaded Via Office Applications"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_office_dotnet_gac_dll_load.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_office_dotnet_gac_dll_load.yml"
build_date: "2026-04-26 15:01:44"
status: "test"
level: "high"
logsource: "windows / image_load"
aliases:
  - "90217a70-13fc-48e4-b3db-0d836c5824ac"
  - "GAC DLL Loaded Via Office Applications"
attack_technique_ids:
  - "T1204.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# GAC DLL Loaded Via Office Applications

Detects any GAC DLL being loaded by an Office Product

## Metadata

- Rule ID: 90217a70-13fc-48e4-b3db-0d836c5824ac
- Status: test
- Level: high
- Author: Antonlovesdnb
- Date: 2020-02-19
- Modified: 2023-02-10
- Source Path: rules/windows/image_load/image_load_office_dotnet_gac_dll_load.yml

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
  ImageLoaded|startswith: C:\Windows\Microsoft.NET\assembly\GAC_MSIL
condition: selection
```

## False Positives

- Legitimate macro usage. Add the appropriate filter according to your environment

## References

- https://medium.com/threatpunter/detecting-adversary-tradecraft-with-image-load-event-logging-and-eql-8de93338c16

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_office_dotnet_gac_dll_load.yml)
