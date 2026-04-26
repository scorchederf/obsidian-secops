---
sigma_id: "570ae5ec-33dc-427c-b815-db86228ad43e"
title: "Application Uninstalled"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/application/msiinstaller/win_builtin_remove_application.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/msiinstaller/win_builtin_remove_application.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "low"
logsource: "windows / application"
aliases:
  - "570ae5ec-33dc-427c-b815-db86228ad43e"
  - "Application Uninstalled"
attack_technique_ids:
  - "T1489"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Application Uninstalled

An application has been removed. Check if it is critical.

## Metadata

- Rule ID: 570ae5ec-33dc-427c-b815-db86228ad43e
- Status: test
- Level: low
- Author: frack113
- Date: 2022-01-28
- Modified: 2022-09-17
- Source Path: rules/windows/builtin/application/msiinstaller/win_builtin_remove_application.yml

## Logsource

- product: windows
- service: application

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1489-service_stop|T1489]]

## Detection

```yaml
selection:
  Provider_Name: MsiInstaller
  EventID:
  - 1034
  - 11724
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/nasbench/EVTX-ETW-Resources/blob/f1b010ce0ee1b71e3024180de1a3e67f99701fe4/ETWProvidersManifests/Windows11/22H2/W11_22H2_Pro_20221220_22621.963/WEPExplorer/Microsoft-Windows-MsiServer.xml
- https://learn.microsoft.com/en-us/windows/win32/msi/event-logging

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/msiinstaller/win_builtin_remove_application.yml)
