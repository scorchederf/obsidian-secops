---
sigma_id: "40b6e656-4e11-4c0c-8772-c1cc6dae34ce"
title: "ScreenSaver Registry Key Set"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_scr_file_executed_by_rundll32.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_scr_file_executed_by_rundll32.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "40b6e656-4e11-4c0c-8772-c1cc6dae34ce"
  - "ScreenSaver Registry Key Set"
attack_technique_ids:
  - "T1218.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# ScreenSaver Registry Key Set

Detects registry key established after masqueraded .scr file execution using Rundll32 through desk.cpl

## Metadata

- Rule ID: 40b6e656-4e11-4c0c-8772-c1cc6dae34ce
- Status: test
- Level: medium
- Author: Jose Luis Sanchez Martinez (@Joseliyo_Jstnk)
- Date: 2022-05-04
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_scr_file_executed_by_rundll32.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

## Detection

```yaml
selection:
  Image|endswith: \rundll32.exe
registry:
  TargetObject|contains: \Control Panel\Desktop\SCRNSAVE.EXE
  Details|endswith: .scr
filter:
  Details|contains:
  - C:\Windows\System32\
  - C:\Windows\SysWOW64\
condition: selection and registry and not filter
```

## False Positives

- Legitimate use of screen saver

## References

- https://twitter.com/VakninHai/status/1517027824984547329
- https://twitter.com/pabraeken/status/998627081360695297
- https://jstnk9.github.io/jstnk9/research/InstallScreenSaver-SCR-files

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_scr_file_executed_by_rundll32.yml)
