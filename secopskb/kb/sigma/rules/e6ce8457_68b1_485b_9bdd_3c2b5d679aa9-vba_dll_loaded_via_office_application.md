---
sigma_id: "e6ce8457-68b1-485b-9bdd-3c2b5d679aa9"
title: "VBA DLL Loaded Via Office Application"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_office_vbadll_load.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_office_vbadll_load.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "high"
logsource: "windows / image_load"
aliases:
  - "e6ce8457-68b1-485b-9bdd-3c2b5d679aa9"
  - "VBA DLL Loaded Via Office Application"
attack_technique_ids:
  - "T1204.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# VBA DLL Loaded Via Office Application

Detects VB DLL's loaded by an office application. Which could indicate the presence of VBA Macros.

## Metadata

- Rule ID: e6ce8457-68b1-485b-9bdd-3c2b5d679aa9
- Status: test
- Level: high
- Author: Antonlovesdnb
- Date: 2020-02-19
- Modified: 2023-02-10
- Source Path: rules/windows/image_load/image_load_office_vbadll_load.yml

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
  ImageLoaded|endswith:
  - \VBE7.DLL
  - \VBEUI.DLL
  - \VBE7INTL.DLL
condition: selection
```

## False Positives

- Legitimate macro usage. Add the appropriate filter according to your environment

## References

- https://medium.com/threatpunter/detecting-adversary-tradecraft-with-image-load-event-logging-and-eql-8de93338c16

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_office_vbadll_load.yml)
