---
sigma_id: "9ed5959a-c43c-4c59-84e3-d28628429456"
title: "UAC Bypass Using Iscsicpl - ImageLoad"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_uac_bypass_iscsicpl.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_uac_bypass_iscsicpl.yml"
build_date: "2026-04-27 19:13:58"
status: "test"
level: "high"
logsource: "windows / image_load"
aliases:
  - "9ed5959a-c43c-4c59-84e3-d28628429456"
  - "UAC Bypass Using Iscsicpl - ImageLoad"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the "iscsicpl.exe" UAC bypass technique that leverages a DLL Search Order hijacking technique to load a custom DLL's from temp or a any user controlled location in the users %PATH%

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism#^t1548002-bypass-user-account-control|T1548.002: Bypass User Account Control]]

## Detection

```yaml
selection:
  Image: C:\Windows\SysWOW64\iscsicpl.exe
  ImageLoaded|endswith: \iscsiexe.dll
filter:
  ImageLoaded|contains|all:
  - C:\Windows\
  - iscsiexe.dll
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://github.com/hackerhouse-opensource/iscsicpl_bypassUAC
- https://twitter.com/wdormann/status/1547583317410607110

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_uac_bypass_iscsicpl.yml)
