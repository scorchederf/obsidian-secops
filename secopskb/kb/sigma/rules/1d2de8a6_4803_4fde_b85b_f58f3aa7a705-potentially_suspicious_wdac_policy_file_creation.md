---
sigma_id: "1d2de8a6-4803-4fde-b85b-f58f3aa7a705"
title: "Potentially Suspicious WDAC Policy File Creation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_susp_wdac_policy_creation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_wdac_policy_creation.yml"
build_date: "2026-04-26 14:14:33"
status: "experimental"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "1d2de8a6-4803-4fde-b85b-f58f3aa7a705"
  - "Potentially Suspicious WDAC Policy File Creation"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potentially Suspicious WDAC Policy File Creation

Detects suspicious Windows Defender Application Control (WDAC) policy file creation from abnormal processes that could be abused by attacker to block EDR/AV components while allowing their own malicious code to run on the system.

## Metadata

- Rule ID: 1d2de8a6-4803-4fde-b85b-f58f3aa7a705
- Status: experimental
- Level: medium
- Author: X__Junior
- Date: 2025-02-07
- Modified: 2025-12-03
- Source Path: rules/windows/file/file_event/file_event_win_susp_wdac_policy_creation.yml

## Logsource

- category: file_event
- product: windows

## Detection

```yaml
selection_target:
  TargetFilename|contains: \Windows\System32\CodeIntegrity\
filter_main_images:
  Image|endswith:
  - \Microsoft.ConfigurationManagement.exe
  - \WDAC Wizard.exe
  - C:\Program Files\PowerShell\7-preview\pwsh.exe
  - C:\Program Files\PowerShell\7\pwsh.exe
  - C:\Windows\System32\dllhost.exe
  - C:\Windows\System32\WindowsPowerShell\v1.0\powershell_ise.exe
  - C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
  - C:\Windows\SysWOW64\dllhost.exe
  - C:\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell_ise.exe
  - C:\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell.exe
filter_main_cli:
- CommandLine|contains|all:
  - ConvertFrom-CIPolicy -XmlFilePath
  - '-BinaryFilePath '
- CommandLine|contains: CiTool --update-policy
- CommandLine|contains|all:
  - Copy-Item -Path
  - -Destination
filter_main_system:
  Image: System
filter_main_wuauclt:
  Image:
  - C:\Windows\System32\wuauclt.exe
  - C:\Windows\UUS\arm64\wuaucltcore.exe
condition: selection_target and not 1 of filter_main_*
```

## False Positives

- Administrators and security vendors could leverage WDAC, apply additional filters as needed.

## References

- https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/deployment/deploy-appcontrol-policies-using-group-policy
- https://beierle.win/2024-12-20-Weaponizing-WDAC-Killing-the-Dreams-of-EDR/
- https://github.com/logangoins/Krueger/tree/main
- https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/deployment/appcontrol-deployment-guide
- https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/deployment/deploy-appcontrol-policies-with-script
- https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/deployment/deploy-appcontrol-policies-with-memcm

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_wdac_policy_creation.yml)
