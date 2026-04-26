---
sigma_id: "ad1f4bb9-8dfb-4765-adb6-2a7cfb6c0f94"
title: "Suspicious WSMAN Provider Image Loads"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_wsman_provider_image_load.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_wsman_provider_image_load.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "ad1f4bb9-8dfb-4765-adb6-2a7cfb6c0f94"
  - "Suspicious WSMAN Provider Image Loads"
attack_technique_ids:
  - "T1059.001"
  - "T1021.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious WSMAN Provider Image Loads

Detects signs of potential use of the WSMAN provider from uncommon processes locally and remote execution.

## Metadata

- Rule ID: ad1f4bb9-8dfb-4765-adb6-2a7cfb6c0f94
- Status: test
- Level: medium
- Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research)
- Date: 2020-06-24
- Modified: 2025-10-17
- Source Path: rules/windows/image_load/image_load_wsman_provider_image_load.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]
- [[kb/attack/techniques/T1021-remote_services|T1021.003]]

## Detection

```yaml
request_client:
- ImageLoaded|endswith:
  - \WsmSvc.dll
  - \WsmAuto.dll
  - \Microsoft.WSMan.Management.ni.dll
- OriginalFileName:
  - WsmSvc.dll
  - WSMANAUTOMATION.DLL
  - Microsoft.WSMan.Management.dll
respond_server:
  Image|endswith: \svchost.exe
  OriginalFileName: WsmWmiPl.dll
filter_general:
  Image:
  - C:\Program Files (x86)\PowerShell\6\pwsh.exe
  - C:\Program Files (x86)\PowerShell\7\pwsh.exe
  - C:\Program Files\PowerShell\6\pwsh.exe
  - C:\Program Files\PowerShell\7\pwsh.exe
  - C:\Windows\System32\sdiagnhost.exe
  - C:\Windows\System32\services.exe
  - C:\Windows\System32\WindowsPowerShell\v1.0\powershell_ise.exe
  - C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
filter_svchost:
  CommandLine|contains:
  - svchost.exe -k netsvcs -p -s BITS
  - svchost.exe -k GraphicsPerfSvcGroup -s GraphicsPerfSvc
  - svchost.exe -k NetworkService -p -s Wecsvc
  - svchost.exe -k netsvcs
filter_mscorsvw:
  Image|startswith:
  - C:\Windows\Microsoft.NET\Framework64\v
  - C:\Windows\Microsoft.NET\Framework\v
  - C:\Windows\Microsoft.NET\FrameworkArm\v
  - C:\Windows\Microsoft.NET\FrameworkArm64\v
  Image|endswith: \mscorsvw.exe
filter_svr_2019:
  Image:
  - C:\Windows\System32\Configure-SMRemoting.exe
  - C:\Windows\System32\ServerManager.exe
filter_nextron:
  Image|startswith: C:\Windows\Temp\asgard2-agent\
filter_citrix:
  Image|startswith: C:\Program Files\Citrix\
filter_upgrade:
  Image|startswith: C:\$WINDOWS.~BT\Sources\
filter_mmc:
  Image|endswith: \mmc.exe
svchost:
  Image|endswith: \svchost.exe
commandline_null:
  CommandLine: null
condition: ( request_client or respond_server ) and not 1 of filter* and not ( svchost
  and commandline_null )
```

## False Positives

- Unknown

## References

- https://twitter.com/chadtilbury/status/1275851297770610688
- https://bohops.com/2020/05/12/ws-management-com-another-approach-for-winrm-lateral-movement/
- https://learn.microsoft.com/en-us/windows/win32/winrm/windows-remote-management-architecture
- https://github.com/bohops/WSMan-WinRM

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_wsman_provider_image_load.yml)
