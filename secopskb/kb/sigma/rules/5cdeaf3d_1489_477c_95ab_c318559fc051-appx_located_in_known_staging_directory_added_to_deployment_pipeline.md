---
sigma_id: "5cdeaf3d-1489-477c-95ab-c318559fc051"
title: "AppX Located in Known Staging Directory Added to Deployment Pipeline"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/appxdeployment_server/win_appxdeployment_server_appx_package_in_staging_directory.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/appxdeployment_server/win_appxdeployment_server_appx_package_in_staging_directory.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "high"
logsource: "windows / appxdeployment-server"
aliases:
  - "5cdeaf3d-1489-477c-95ab-c318559fc051"
  - "AppX Located in Known Staging Directory Added to Deployment Pipeline"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects an appx package that was added to the pipeline of the "to be processed" packages that is located in a known folder often used as a staging directory.

## Logsource

- product: windows
- service: appxdeployment-server

## Detection

```yaml
selection_eid:
  EventID: 854
selection_paths_forward:
  Path|contains:
  - :/Perflogs/
  - :/Users/Public/
  - :/Windows/Temp/
  - /AppdData/Local/Temp/
  - /Desktop/
  - /Downloads/
selection_paths_back:
  Path|contains:
  - :\PerfLogs\
  - :\Users\Public\
  - :\Windows\Temp\
  - \AppdData\Local\Temp\
  - \Desktop\
  - \Downloads\
condition: selection_eid and 1 of selection_paths_*
```

## False Positives

- Unknown

## References

- https://www.sentinelone.com/labs/inside-malicious-windows-apps-for-malware-deployment/
- https://learn.microsoft.com/en-us/windows/win32/appxpkg/troubleshooting
- https://news.sophos.com/en-us/2021/11/11/bazarloader-call-me-back-attack-abuses-windows-10-apps-mechanism/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/appxdeployment_server/win_appxdeployment_server_appx_package_in_staging_directory.yml)
