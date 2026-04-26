---
sigma_id: "6ae53108-c3a0-4bee-8f45-c7591a2c337f"
title: "Deployment AppX Package Was Blocked By AppLocker"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/appxdeployment_server/win_appxdeployment_server_applocker_block.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/appxdeployment_server/win_appxdeployment_server_applocker_block.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "medium"
logsource: "windows / appxdeployment-server"
aliases:
  - "6ae53108-c3a0-4bee-8f45-c7591a2c337f"
  - "Deployment AppX Package Was Blocked By AppLocker"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Deployment AppX Package Was Blocked By AppLocker

Detects an appx package deployment that was blocked by AppLocker policy.

## Metadata

- Rule ID: 6ae53108-c3a0-4bee-8f45-c7591a2c337f
- Status: test
- Level: medium
- Author: frack113
- Date: 2023-01-11
- Source Path: rules/windows/builtin/appxdeployment_server/win_appxdeployment_server_applocker_block.yml

## Logsource

- product: windows
- service: appxdeployment-server

## Detection

```yaml
selection:
  EventID: 412
condition: selection
```

## False Positives

- Unlikely, since this event notifies about blocked application deployment. Tune your applocker rules to avoid blocking legitimate applications.

## References

- https://learn.microsoft.com/en-us/windows/win32/appxpkg/troubleshooting
- https://github.com/nasbench/EVTX-ETW-Resources/blob/7a806a148b3d9d381193d4a80356016e6e8b1ee8/ETWEventsList/CSV/Windows11/22H2/W11_22H2_Pro_20220920_22621.382/Providers/Microsoft-Windows-AppXDeployment-Server.csv

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/appxdeployment_server/win_appxdeployment_server_applocker_block.yml)
