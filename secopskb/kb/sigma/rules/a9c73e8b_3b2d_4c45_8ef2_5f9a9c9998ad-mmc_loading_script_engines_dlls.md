---
sigma_id: "a9c73e8b-3b2d-4c45-8ef2-5f9a9c9998ad"
title: "MMC Loading Script Engines DLLs"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_win_mmc_loads_script_engine_dll.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_win_mmc_loads_script_engine_dll.yml"
build_date: "2026-04-26 14:14:28"
status: "experimental"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "a9c73e8b-3b2d-4c45-8ef2-5f9a9c9998ad"
  - "MMC Loading Script Engines DLLs"
attack_technique_ids:
  - "T1059.005"
  - "T1218.014"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# MMC Loading Script Engines DLLs

Detects when the Microsoft Management Console (MMC) loads the DLL libraries like vbscript, jscript etc which might indicate an attempt
to execute malicious scripts within a trusted system process for bypassing application whitelisting or defense evasion.

## Metadata

- Rule ID: a9c73e8b-3b2d-4c45-8ef2-5f9a9c9998ad
- Status: experimental
- Level: medium
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-02-05
- Source Path: rules/windows/image_load/image_load_win_mmc_loads_script_engine_dll.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.005]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.014]]

## Detection

```yaml
selection:
  Image|endswith: \mmc.exe
  ImageLoaded|endswith:
  - \vbscript.dll
  - \jscript.dll
  - \jscript9.dll
condition: selection
```

## False Positives

- Legitimate MMC operations or extensions loading these libraries

## References

- https://tria.ge/241015-l98snsyeje/behavioral2
- https://www.elastic.co/security-labs/grimresource

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_win_mmc_loads_script_engine_dll.yml)
