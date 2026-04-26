---
sigma_id: "9e9a9002-56c4-40fd-9eff-e4b09bfa5f6c"
title: "DLL Load By System Process From Suspicious Locations"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_susp_dll_load_system_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_susp_dll_load_system_process.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "9e9a9002-56c4-40fd-9eff-e4b09bfa5f6c"
  - "DLL Load By System Process From Suspicious Locations"
attack_technique_ids:
  - "T1070"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# DLL Load By System Process From Suspicious Locations

Detects when a system process (i.e. located in system32, syswow64, etc.) loads a DLL from a suspicious location or a location with permissive permissions such as "C:\Users\Public"

## Metadata

- Rule ID: 9e9a9002-56c4-40fd-9eff-e4b09bfa5f6c
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-17
- Modified: 2023-09-18
- Source Path: rules/windows/image_load/image_load_susp_dll_load_system_process.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070]]

## Detection

```yaml
selection:
  Image|startswith: C:\Windows\
  ImageLoaded|startswith:
  - C:\Users\Public\
  - C:\PerfLogs\
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/hackerhouse-opensource/iscsicpl_bypassUAC (Idea)

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_susp_dll_load_system_process.yml)
