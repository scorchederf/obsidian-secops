---
sigma_id: "c977cb50-3dff-4a9f-b873-9290f56132f1"
title: "AppX Located in Uncommon Directory Added to Deployment Pipeline"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/appxdeployment_server/win_appxdeployment_server_uncommon_package_locations.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/appxdeployment_server/win_appxdeployment_server_uncommon_package_locations.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / appxdeployment-server"
aliases:
  - "c977cb50-3dff-4a9f-b873-9290f56132f1"
  - "AppX Located in Uncommon Directory Added to Deployment Pipeline"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AppX Located in Uncommon Directory Added to Deployment Pipeline

Detects an appx package that was added to the pipeline of the "to be processed" packages that is located in uncommon locations.

## Metadata

- Rule ID: c977cb50-3dff-4a9f-b873-9290f56132f1
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-01-11
- Modified: 2025-12-03
- Source Path: rules/windows/builtin/appxdeployment_server/win_appxdeployment_server_uncommon_package_locations.yml

## Logsource

- product: windows
- service: appxdeployment-server

## Detection

```yaml
selection:
  EventID: 854
filter_main_generic:
  Path|contains:
  - :/Program%20Files
  - :/Windows/System32/
  - :\Program Files (x86)\
  - :\Program Files\
  - :\Windows\ImmersiveControlPanel\
  - :\Windows\PrintDialog\
  - :\Windows\SystemApps\
  - AppData/Local/Temp/WinGet/Microsoft.Winget.Source
  - x-windowsupdate://
filter_main_specific:
  Path|contains:
  - https://installer.teams.static.microsoft/
  - https://res.cdn.office.net
  - https://statics.teams.cdn.live.net/
  - https://statics.teams.cdn.office.net/
  - microsoft.com
filter_optional_onedrive:
  Path|contains: AppData\Local\Microsoft\OneDrive\
filter_optional_winget:
  Path|contains:
  - AppData/Local/Temp/WinGet/Microsoft.Winget.Source
  - AppData\Local\Temp\WinGet\Microsoft.Winget.Source
filter_optional_x_windowsupdate:
  Path|contains: x-windowsupdate://
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- Internal Research
- https://www.sentinelone.com/labs/inside-malicious-windows-apps-for-malware-deployment/
- https://learn.microsoft.com/en-us/windows/win32/appxpkg/troubleshooting
- https://news.sophos.com/en-us/2021/11/11/bazarloader-call-me-back-attack-abuses-windows-10-apps-mechanism/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/appxdeployment_server/win_appxdeployment_server_uncommon_package_locations.yml)
