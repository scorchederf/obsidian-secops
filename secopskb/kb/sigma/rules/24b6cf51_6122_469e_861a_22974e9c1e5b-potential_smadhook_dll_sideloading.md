---
sigma_id: "24b6cf51-6122-469e-861a-22974e9c1e5b"
title: "Potential SmadHook.DLL Sideloading"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_smadhook.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_smadhook.yml"
build_date: "2026-04-26 15:01:49"
status: "test"
level: "high"
logsource: "windows / image_load"
aliases:
  - "24b6cf51-6122-469e-861a-22974e9c1e5b"
  - "Potential SmadHook.DLL Sideloading"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential SmadHook.DLL Sideloading

Detects potential DLL sideloading of "SmadHook.dll", a DLL used by SmadAV antivirus

## Metadata

- Rule ID: 24b6cf51-6122-469e-861a-22974e9c1e5b
- Status: test
- Level: high
- Author: X__Junior (Nextron Systems)
- Date: 2023-06-01
- Source Path: rules/windows/image_load/image_load_side_load_smadhook.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  ImageLoaded|endswith:
  - \SmadHook32c.dll
  - \SmadHook64c.dll
filter_main_legit_path:
  Image:
  - C:\Program Files (x86)\SMADAV\SmadavProtect32.exe
  - C:\Program Files (x86)\SMADAV\SmadavProtect64.exe
  - C:\Program Files\SMADAV\SmadavProtect32.exe
  - C:\Program Files\SMADAV\SmadavProtect64.exe
  ImageLoaded|startswith:
  - C:\Program Files (x86)\SMADAV\
  - C:\Program Files\SMADAV\
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unlikely

## References

- https://research.checkpoint.com/2023/malware-spotlight-camaro-dragons-tinynote-backdoor/
- https://www.qurium.org/alerts/targeted-malware-against-crph/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_smadhook.yml)
