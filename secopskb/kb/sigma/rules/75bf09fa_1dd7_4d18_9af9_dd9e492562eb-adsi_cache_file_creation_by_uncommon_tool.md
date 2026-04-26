---
sigma_id: "75bf09fa-1dd7-4d18-9af9-dd9e492562eb"
title: "ADSI-Cache File Creation By Uncommon Tool"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_adsi_cache_creation_by_uncommon_tool.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_adsi_cache_creation_by_uncommon_tool.yml"
build_date: "2026-04-26 14:14:19"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "75bf09fa-1dd7-4d18-9af9-dd9e492562eb"
  - "ADSI-Cache File Creation By Uncommon Tool"
attack_technique_ids:
  - "T1001.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# ADSI-Cache File Creation By Uncommon Tool

Detects the creation of an "Active Directory Schema Cache File" (.sch) file by an uncommon tool.

## Metadata

- Rule ID: 75bf09fa-1dd7-4d18-9af9-dd9e492562eb
- Status: test
- Level: medium
- Author: xknow @xknow_infosec, Tim Shelton
- Date: 2019-03-24
- Modified: 2023-10-18
- Source Path: rules/windows/file/file_event/file_event_win_adsi_cache_creation_by_uncommon_tool.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1001-data_obfuscation|T1001.003]]

## Detection

```yaml
selection:
  TargetFilename|contains: \Local\Microsoft\Windows\SchCache\
  TargetFilename|endswith: .sch
filter_main_generic:
- Image|endswith:
  - :\Program Files\Cylance\Desktop\CylanceSvc.exe
  - :\Windows\CCM\CcmExec.exe
  - :\windows\system32\dllhost.exe
  - :\Windows\system32\dsac.exe
  - :\Windows\system32\efsui.exe
  - :\windows\system32\mmc.exe
  - :\windows\system32\svchost.exe
  - :\Windows\System32\wbem\WmiPrvSE.exe
  - :\windows\system32\WindowsPowerShell\v1.0\powershell.exe
- Image|contains:
  - :\Windows\ccmsetup\autoupgrade\ccmsetup
  - :\Program Files\SentinelOne\Sentinel Agent
filter_main_office:
  Image|contains|all:
  - :\Program Files\
  - \Microsoft Office
  Image|endswith: \OUTLOOK.EXE
filter_optional_ldapwhoami:
  Image|endswith: \LANDesk\LDCLient\ldapwhoami.exe
filter_optional_citrix:
  Image|endswith: :\Program Files\Citrix\Receiver StoreFront\Services\DefaultDomainServices\Citrix.DeliveryServices.DomainServices.ServiceHost.exe
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Other legimate tools, which do ADSI (LDAP) operations, e.g. any remoting activity by MMC, Powershell, Windows etc.

## References

- https://medium.com/@ivecodoe/detecting-ldapfragger-a-newly-released-cobalt-strike-beacon-using-ldap-for-c2-communication-c274a7f00961
- https://blog.fox-it.com/2020/03/19/ldapfragger-command-and-control-over-ldap-attributes/
- https://github.com/fox-it/LDAPFragger

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_adsi_cache_creation_by_uncommon_tool.yml)
