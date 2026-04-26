---
sigma_id: "e54279c7-4910-4e2c-902c-c56a25b549f6"
title: "Windows AppX Deployment Full Trust Package Installation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/appxdeployment_server/win_appxpackaging_server_full_trust_package_installation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/appxdeployment_server/win_appxpackaging_server_full_trust_package_installation.yml"
build_date: "2026-04-26 14:14:40"
status: "experimental"
level: "medium"
logsource: "windows / appxdeployment-server"
aliases:
  - "e54279c7-4910-4e2c-902c-c56a25b549f6"
  - "Windows AppX Deployment Full Trust Package Installation"
attack_technique_ids:
  - "T1204.002"
  - "T1553.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows AppX Deployment Full Trust Package Installation

Detects the installation of MSIX/AppX packages with full trust privileges which run with elevated privileges outside normal AppX container restrictions

## Metadata

- Rule ID: e54279c7-4910-4e2c-902c-c56a25b549f6
- Status: experimental
- Level: medium
- Author: Michael Haag, Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-11-03
- Source Path: rules/windows/builtin/appxdeployment_server/win_appxpackaging_server_full_trust_package_installation.yml

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
  EventID: 400
  HasFullTrust: true
filter_main_legitpath:
  PackageSourceUri|startswith:
  - file:///C:/Program%20Files/
  - file:///C:/Program%20Files%20(x86)/
filter_main_microsoft:
- PackageSourceUri|startswith: https://go.microsoft.com/fwlink/?linkid
- PackageSourceUri|contains:
  - .cdn.microsoft.com
  - .cdn.office.net/
filter_main_callerprocess:
  CallingProcess|startswith:
  - sysprep.exe
  - svchost.exe,AppReadiness
filter_optional_x_update:
  PackageSourceUri|startswith: x-windowsupdate://
filter_optional_microsoftclient:
  PackageFullName|startswith: MicrosoftWindows.Client.
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Some legitimate applications installation which have been missed from filtering can generate fps, thus baselining and tuning is recommended before deploying to production

## References

- https://www.splunk.com/en_us/blog/security/msix-weaponization-threat-detection-splunk.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/appxdeployment_server/win_appxpackaging_server_full_trust_package_installation.yml)
