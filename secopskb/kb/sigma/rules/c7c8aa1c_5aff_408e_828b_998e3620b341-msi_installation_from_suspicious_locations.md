---
sigma_id: "c7c8aa1c-5aff-408e-828b-998e3620b341"
title: "MSI Installation From Suspicious Locations"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/application/msiinstaller/win_msi_install_from_susp_locations.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/msiinstaller/win_msi_install_from_susp_locations.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "medium"
logsource: "windows / application"
aliases:
  - "c7c8aa1c-5aff-408e-828b-998e3620b341"
  - "MSI Installation From Suspicious Locations"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# MSI Installation From Suspicious Locations

Detects MSI package installation from suspicious locations

## Metadata

- Rule ID: c7c8aa1c-5aff-408e-828b-998e3620b341
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-31
- Modified: 2023-10-23
- Source Path: rules/windows/builtin/application/msiinstaller/win_msi_install_from_susp_locations.yml

## Logsource

- product: windows
- service: application

## Detection

```yaml
selection:
  Provider_Name: MsiInstaller
  EventID:
  - 1040
  - 1042
  Data|contains:
  - :\Windows\TEMP\
  - \\\\
  - \Desktop\
  - \PerfLogs\
  - \Users\Public\
filter_winget:
  Data|contains: \AppData\Local\Temp\WinGet\
filter_updhealthtools:
  Data|contains: C:\Windows\TEMP\UpdHealthTools.msi
condition: selection and not 1 of filter_*
```

## False Positives

- False positives may occur if you allow installation from folders such as the desktop, the public folder or remote shares. A baseline is required before production use.

## References

- https://www.trendmicro.com/en_us/research/22/h/ransomware-actor-abuses-genshin-impact-anti-cheat-driver-to-kill-antivirus.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/msiinstaller/win_msi_install_from_susp_locations.yml)
