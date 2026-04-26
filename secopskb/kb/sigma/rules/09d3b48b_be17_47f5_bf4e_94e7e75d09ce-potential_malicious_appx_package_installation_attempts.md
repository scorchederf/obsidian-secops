---
sigma_id: "09d3b48b-be17-47f5-bf4e-94e7e75d09ce"
title: "Potential Malicious AppX Package Installation Attempts"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/appxdeployment_server/win_appxdeployment_server_mal_appx_names.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/appxdeployment_server/win_appxdeployment_server_mal_appx_names.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / appxdeployment-server"
aliases:
  - "09d3b48b-be17-47f5-bf4e-94e7e75d09ce"
  - "Potential Malicious AppX Package Installation Attempts"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Malicious AppX Package Installation Attempts

Detects potential installation or installation attempts of known malicious appx packages

## Metadata

- Rule ID: 09d3b48b-be17-47f5-bf4e-94e7e75d09ce
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-01-11
- Modified: 2023-01-12
- Source Path: rules/windows/builtin/appxdeployment_server/win_appxdeployment_server_mal_appx_names.yml

## Logsource

- product: windows
- service: appxdeployment-server

## Detection

```yaml
selection:
  EventID:
  - 400
  - 401
  PackageFullName|contains: 3669e262-ec02-4e9d-bcb4-3d008b4afac9
condition: selection
```

## False Positives

- Rare occasions where a malicious package uses the exact same name and version as a legitimate application.

## References

- https://www.sentinelone.com/labs/inside-malicious-windows-apps-for-malware-deployment/
- https://news.sophos.com/en-us/2021/11/11/bazarloader-call-me-back-attack-abuses-windows-10-apps-mechanism/
- https://forensicitguy.github.io/analyzing-magnitude-magniber-appx/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/appxdeployment_server/win_appxdeployment_server_mal_appx_names.yml)
