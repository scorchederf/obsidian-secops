---
sigma_id: "857c8db3-c89b-42fb-882b-f681c7cf4da2"
title: "Unsigned Image Loaded Into LSASS Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_lsass_unsigned_image_load.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_lsass_unsigned_image_load.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "857c8db3-c89b-42fb-882b-f681c7cf4da2"
  - "Unsigned Image Loaded Into LSASS Process"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Unsigned Image Loaded Into LSASS Process

Loading unsigned image (DLL, EXE) into LSASS process

## Metadata

- Rule ID: 857c8db3-c89b-42fb-882b-f681c7cf4da2
- Status: test
- Level: medium
- Author: Teymur Kheirkhabarov, oscd.community
- Date: 2019-10-22
- Modified: 2021-11-27
- Source Path: rules/windows/image_load/image_load_lsass_unsigned_image_load.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Detection

```yaml
selection:
  Image|endswith: \lsass.exe
  Signed: 'false'
condition: selection
```

## False Positives

- Valid user connecting using RDP

## References

- https://www.slideshare.net/heirhabarov/hunting-for-credentials-dumping-in-windows-environment

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_lsass_unsigned_image_load.yml)
