---
sigma_id: "ec8c4047-fad9-416a-8c81-0f479353d7f6"
title: "Diagnostic Library Sdiageng.DLL Loaded By Msdt.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_dll_sdiageng_load_by_msdt.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_dll_sdiageng_load_by_msdt.yml"
build_date: "2026-04-26 15:01:44"
status: "test"
level: "high"
logsource: "windows / image_load"
aliases:
  - "ec8c4047-fad9-416a-8c81-0f479353d7f6"
  - "Diagnostic Library Sdiageng.DLL Loaded By Msdt.EXE"
attack_technique_ids:
  - "T1202"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Diagnostic Library Sdiageng.DLL Loaded By Msdt.EXE

Detects both of CVE-2022-30190 (Follina) and DogWalk vulnerabilities exploiting msdt.exe binary to load the "sdiageng.dll" library

## Metadata

- Rule ID: ec8c4047-fad9-416a-8c81-0f479353d7f6
- Status: test
- Level: high
- Author: Greg (rule)
- Date: 2022-06-17
- Modified: 2023-02-17
- Source Path: rules/windows/image_load/image_load_dll_sdiageng_load_by_msdt.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Detection

```yaml
selection:
  Image|endswith: \msdt.exe
  ImageLoaded|endswith: \sdiageng.dll
condition: selection
```

## False Positives

- Unknown

## References

- https://www.securonix.com/blog/detecting-microsoft-msdt-dogwalk/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_dll_sdiageng_load_by_msdt.yml)
