---
sigma_id: "2f78da12-f7c7-430b-8b19-a28f269b77a3"
title: "Disable Windows Event Logging Via Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_disable_winevt_logging.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_disable_winevt_logging.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "2f78da12-f7c7-430b-8b19-a28f269b77a3"
  - "Disable Windows Event Logging Via Registry"
attack_technique_ids:
  - "T1562.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Disable Windows Event Logging Via Registry

Detects tampering with the "Enabled" registry key in order to disable Windows logging of a Windows event channel

## Metadata

- Rule ID: 2f78da12-f7c7-430b-8b19-a28f269b77a3
- Status: test
- Level: high
- Author: frack113, Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-04
- Modified: 2024-03-25
- Source Path: rules/windows/registry/registry_set/registry_set_disable_winevt_logging.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.002]]

## Detection

```yaml
selection:
  TargetObject|contains: \Microsoft\Windows\CurrentVersion\WINEVT\Channels\
  TargetObject|endswith: \Enabled
  Details: DWORD (0x00000000)
filter_main_wevutil:
  Image: C:\Windows\system32\wevtutil.exe
filter_main_iis:
  Image|startswith: C:\Windows\winsxs\
  Image|endswith: \TiWorker.exe
filter_main_svchost:
  Image: C:\Windows\System32\svchost.exe
  TargetObject|contains:
  - \Microsoft\Windows\CurrentVersion\WINEVT\Channels\Microsoft-Windows-FileInfoMinifilter
  - \Microsoft\Windows\CurrentVersion\WINEVT\Channels\Microsoft-Windows-ASN1\
  - \Microsoft\Windows\CurrentVersion\WINEVT\Channels\Microsoft-Windows-Kernel-AppCompat\
  - \Microsoft\Windows\CurrentVersion\WINEVT\Channels\Microsoft-Windows-Runtime\Error\
  - \Microsoft\Windows\CurrentVersion\WINEVT\Channels\Microsoft-Windows-CAPI2/Operational\
filter_main_trusted_installer:
  Image: C:\Windows\servicing\TrustedInstaller.exe
  TargetObject|contains: \Microsoft\Windows\CurrentVersion\WINEVT\Channels\Microsoft-Windows-Compat-Appraiser
filter_optional_empty:
  Image: ''
filter_optional_null:
  Image: null
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Rare falsepositives may occur from legitimate administrators disabling specific event log for troubleshooting

## References

- https://twitter.com/WhichbufferArda/status/1543900539280293889
- https://github.com/DebugPrivilege/CPP/blob/c39d365617dbfbcb01fffad200d52b6239b2918c/Windows%20Defender/RestoreDefenderConfig.cpp

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_disable_winevt_logging.yml)
