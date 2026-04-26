---
sigma_id: "9a025188-6f2d-42f8-bb2f-d3a83d24a5af"
title: "Windows AppX Deployment Unsigned Package Installation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/appxdeployment_server/win_appxpackaging_server_unsigned_package_installation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/appxdeployment_server/win_appxpackaging_server_unsigned_package_installation.yml"
build_date: "2026-04-26 14:14:40"
status: "experimental"
level: "medium"
logsource: "windows / appxdeployment-server"
aliases:
  - "9a025188-6f2d-42f8-bb2f-d3a83d24a5af"
  - "Windows AppX Deployment Unsigned Package Installation"
attack_technique_ids:
  - "T1204.002"
  - "T1553.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows AppX Deployment Unsigned Package Installation

Detects attempts to install unsigned MSIX/AppX packages using the -AllowUnsigned parameter via AppXDeployment-Server events

## Metadata

- Rule ID: 9a025188-6f2d-42f8-bb2f-d3a83d24a5af
- Status: experimental
- Level: medium
- Author: Michael Haag, Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-11-03
- Source Path: rules/windows/builtin/appxdeployment_server/win_appxpackaging_server_unsigned_package_installation.yml

## Logsource

- product: windows
- service: appxdeployment-server

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1204-user_execution|T1204.002]]
- [[kb/attack/techniques/T1553-subvert_trust_controls|T1553.005]]

## Detection

```yaml
selection:
  EventID: 603
  Flags: '8388608'
condition: selection
```

## False Positives

- Legitimate installation of unsigned packages for legitimate purposes such as development or testing

## References

- https://docs.microsoft.com/en-us/powershell/module/appx/add-appxpackage
- https://www.splunk.com/en_us/blog/security/msix-weaponization-threat-detection-splunk.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/appxdeployment_server/win_appxpackaging_server_unsigned_package_installation.yml)
