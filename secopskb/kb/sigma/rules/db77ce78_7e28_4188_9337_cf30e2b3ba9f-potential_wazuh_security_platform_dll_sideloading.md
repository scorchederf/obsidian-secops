---
sigma_id: "db77ce78-7e28-4188-9337-cf30e2b3ba9f"
title: "Potential Wazuh Security Platform DLL Sideloading"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_wazuh.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_wazuh.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "db77ce78-7e28-4188-9337-cf30e2b3ba9f"
  - "Potential Wazuh Security Platform DLL Sideloading"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Wazuh Security Platform DLL Sideloading

Detects potential DLL side loading of DLLs that are part of the Wazuh security platform

## Metadata

- Rule ID: db77ce78-7e28-4188-9337-cf30e2b3ba9f
- Status: test
- Level: medium
- Author: X__Junior (Nextron Systems)
- Date: 2023-03-13
- Modified: 2023-05-12
- Source Path: rules/windows/image_load/image_load_side_load_wazuh.yml

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
  - \libwazuhshared.dll
  - \libwinpthread-1.dll
filter_main_generic:
  ImageLoaded|startswith:
  - C:\Program Files\
  - C:\Program Files (x86)\
filter_optional_mingw64:
  ImageLoaded|contains:
  - \AppData\Local\
  - \ProgramData\
  ImageLoaded|endswith: \mingw64\bin\libwinpthread-1.dll
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Many legitimate applications leverage this DLL. (Visual Studio, JetBrains, Ruby, Anaconda, GithubDesktop, etc.)

## References

- https://www.trendmicro.com/en_us/research/23/c/iron-tiger-sysupdate-adds-linux-targeting.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_wazuh.yml)
