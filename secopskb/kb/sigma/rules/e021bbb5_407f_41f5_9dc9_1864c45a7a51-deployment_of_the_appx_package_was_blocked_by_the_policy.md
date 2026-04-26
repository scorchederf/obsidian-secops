---
sigma_id: "e021bbb5-407f-41f5-9dc9-1864c45a7a51"
title: "Deployment Of The AppX Package Was Blocked By The Policy"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/appxdeployment_server/win_appxdeployment_server_policy_block.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/appxdeployment_server/win_appxdeployment_server_policy_block.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "medium"
logsource: "windows / appxdeployment-server"
aliases:
  - "e021bbb5-407f-41f5-9dc9-1864c45a7a51"
  - "Deployment Of The AppX Package Was Blocked By The Policy"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Deployment Of The AppX Package Was Blocked By The Policy

Detects an appx package deployment that was blocked by the local computer policy.
The following events indicate that an AppX package deployment was blocked by a policy:
- Event ID 441: The package deployment operation is blocked by the "Allow deployment operations in special profiles" policy
- Event ID 442: Deployments to non-system volumes are blocked by the "Disable deployment of Windows Store apps to non-system volumes" policy."
- Event ID 453: Package blocked by a platform policy.
- Event ID 454: Package blocked by a platform policy.

## Metadata

- Rule ID: e021bbb5-407f-41f5-9dc9-1864c45a7a51
- Status: test
- Level: medium
- Author: frack113
- Date: 2023-01-11
- Source Path: rules/windows/builtin/appxdeployment_server/win_appxdeployment_server_policy_block.yml

## Logsource

- product: windows
- service: appxdeployment-server

## Detection

```yaml
selection:
  EventID:
  - 441
  - 442
  - 453
  - 454
condition: selection
```

## False Positives

- Unlikely, since this event notifies about blocked application deployment. Tune your applocker rules to avoid blocking legitimate applications.

## References

- https://learn.microsoft.com/en-us/windows/win32/appxpkg/troubleshooting
- https://github.com/nasbench/EVTX-ETW-Resources/blob/7a806a148b3d9d381193d4a80356016e6e8b1ee8/ETWEventsList/CSV/Windows11/22H2/W11_22H2_Pro_20220920_22621.382/Providers/Microsoft-Windows-AppXDeployment-Server.csv

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/appxdeployment_server/win_appxdeployment_server_policy_block.yml)
