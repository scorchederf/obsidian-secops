---
sigma_id: "4d7f1827-1637-4def-8d8a-fd254f9454df"
title: "Sysmon Application Crashed"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/application_popup/win_system_application_sysmon_crash.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/application_popup/win_system_application_sysmon_crash.yml"
build_date: "2026-04-26 15:01:52"
status: "test"
level: "high"
logsource: "windows / system"
aliases:
  - "4d7f1827-1637-4def-8d8a-fd254f9454df"
  - "Sysmon Application Crashed"
attack_technique_ids:
  - "T1562"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Sysmon Application Crashed

Detects application popup reporting a failure of the Sysmon service

## Metadata

- Rule ID: 4d7f1827-1637-4def-8d8a-fd254f9454df
- Status: test
- Level: high
- Author: Tim Shelton
- Date: 2022-04-26
- Modified: 2024-01-17
- Source Path: rules/windows/builtin/system/application_popup/win_system_application_sysmon_crash.yml

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562]]

## Detection

```yaml
selection:
  Provider_Name: Application Popup
  EventID: 26
  Caption:
  - sysmon64.exe - Application Error
  - sysmon.exe - Application Error
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/nasbench/EVTX-ETW-Resources/blob/f1b010ce0ee1b71e3024180de1a3e67f99701fe4/ETWProvidersManifests/Windows10/1803/W10_1803_Pro_19700101_17134.1/WEPExplorer/Application%20Popup.xml#L36

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/application_popup/win_system_application_sysmon_crash.yml)
