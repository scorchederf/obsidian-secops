---
sigma_id: "898d5fc9-fbc3-43de-93ad-38e97237c344"
title: "AppX Package Deployment Failed Due to Signing Requirements"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/appxdeployment_server/win_appxdeployment_server_appx_package_deployment_failed_signing_requirements.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/appxdeployment_server/win_appxdeployment_server_appx_package_deployment_failed_signing_requirements.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / appxdeployment-server"
aliases:
  - "898d5fc9-fbc3-43de-93ad-38e97237c344"
  - "AppX Package Deployment Failed Due to Signing Requirements"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AppX Package Deployment Failed Due to Signing Requirements

Detects an appx package deployment / installation with the error code "0x80073cff" which indicates that the package didn't meet the signing requirements.

## Metadata

- Rule ID: 898d5fc9-fbc3-43de-93ad-38e97237c344
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-01-11
- Modified: 2025-12-03
- Source Path: rules/windows/builtin/appxdeployment_server/win_appxdeployment_server_appx_package_deployment_failed_signing_requirements.yml

## Logsource

- product: windows
- service: appxdeployment-server

## Detection

```yaml
selection:
  EventID: 401
  ErrorCode: '0x80073cff'
condition: selection
```

## False Positives

- Legitimate AppX packages not signed by MS used part of an enterprise.

## References

- https://www.sentinelone.com/labs/inside-malicious-windows-apps-for-malware-deployment/
- https://learn.microsoft.com/en-us/windows/win32/appxpkg/troubleshooting
- https://news.sophos.com/en-us/2021/11/11/bazarloader-call-me-back-attack-abuses-windows-10-apps-mechanism/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/appxdeployment_server/win_appxdeployment_server_appx_package_deployment_failed_signing_requirements.yml)
