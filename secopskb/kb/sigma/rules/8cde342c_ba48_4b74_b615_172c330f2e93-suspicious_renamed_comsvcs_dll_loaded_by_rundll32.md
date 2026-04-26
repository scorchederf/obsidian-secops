---
sigma_id: "8cde342c-ba48-4b74-b615-172c330f2e93"
title: "Suspicious Renamed Comsvcs DLL Loaded By Rundll32"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_dll_comsvcs_load_renamed_version_by_rundll32.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_dll_comsvcs_load_renamed_version_by_rundll32.yml"
build_date: "2026-04-26 15:01:52"
status: "test"
level: "high"
logsource: "windows / image_load"
aliases:
  - "8cde342c-ba48-4b74-b615-172c330f2e93"
  - "Suspicious Renamed Comsvcs DLL Loaded By Rundll32"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Renamed Comsvcs DLL Loaded By Rundll32

Detects rundll32 loading a renamed comsvcs.dll to dump process memory

## Metadata

- Rule ID: 8cde342c-ba48-4b74-b615-172c330f2e93
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-14
- Modified: 2023-02-17
- Source Path: rules/windows/image_load/image_load_dll_comsvcs_load_renamed_version_by_rundll32.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Detection

```yaml
selection:
  Image|endswith: \rundll32.exe
  Hashes|contains:
  - IMPHASH=eed93054cb555f3de70eaa9787f32ebb
  - IMPHASH=5e0dbdec1fce52daae251a110b4f309d
  - IMPHASH=eadbccbb324829acb5f2bbe87e5549a8
  - IMPHASH=407ca0f7b523319d758a40d7c0193699
  - IMPHASH=281d618f4e6271e527e6386ea6f748de
filter:
  ImageLoaded|endswith: \comsvcs.dll
condition: selection and not filter
```

## False Positives

- Unlikely

## References

- https://twitter.com/sbousseaden/status/1555200155351228419

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_dll_comsvcs_load_renamed_version_by_rundll32.yml)
