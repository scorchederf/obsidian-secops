---
sigma_id: "0eb46774-f1ab-4a74-8238-1155855f2263"
title: "Disable Windows Defender Functionalities Via Registry Keys"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_windows_defender_tamper.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_windows_defender_tamper.yml"
build_date: "2026-04-26 15:01:44"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "0eb46774-f1ab-4a74-8238-1155855f2263"
  - "Disable Windows Defender Functionalities Via Registry Keys"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Disable Windows Defender Functionalities Via Registry Keys

Detects when attackers or tools disable Windows Defender functionalities via the Windows registry

## Metadata

- Rule ID: 0eb46774-f1ab-4a74-8238-1155855f2263
- Status: test
- Level: high
- Author: AlertIQ, Ján Trenčanský, frack113, Nasreddine Bencherchali, Swachchhanda Shrawan Poudel
- Date: 2022-08-01
- Modified: 2024-10-07
- Source Path: rules/windows/registry/registry_set/registry_set_windows_defender_tamper.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection_main:
  TargetObject|contains:
  - \SOFTWARE\Microsoft\Windows Defender\
  - \SOFTWARE\Policies\Microsoft\Windows Defender Security Center\
  - \SOFTWARE\Policies\Microsoft\Windows Defender\
selection_dword_1:
  TargetObject|endswith:
  - \DisableAntiSpyware
  - \DisableAntiVirus
  - \DisableBehaviorMonitoring
  - \DisableBlockAtFirstSeen
  - \DisableEnhancedNotifications
  - \DisableIntrusionPreventionSystem
  - \DisableIOAVProtection
  - \DisableOnAccessProtection
  - \DisableRealtimeMonitoring
  - \DisableScanOnRealtimeEnable
  - \DisableScriptScanning
  Details: DWORD (0x00000001)
selection_dword_0:
  TargetObject|endswith:
  - \DisallowExploitProtectionOverride
  - \Features\TamperProtection
  - \MpEngine\MpEnablePus
  - \PUAProtection
  - \Signature Update\ForceUpdateFromMU
  - \SpyNet\SpynetReporting
  - \SpyNet\SubmitSamplesConsent
  - \Windows Defender Exploit Guard\Controlled Folder Access\EnableControlledFolderAccess
  Details: DWORD (0x00000000)
filter_optional_symantec:
  Image|startswith: C:\Program Files\Symantec\Symantec Endpoint Protection\
  Image|endswith: \sepWscSvc64.exe
condition: selection_main and 1 of selection_dword_* and not 1 of filter_optional_*
```

## False Positives

- Administrator actions via the Windows Defender interface
- Third party Antivirus

## References

- https://thedfirreport.com/2021/10/18/icedid-to-xinglocker-ransomware-in-24-hours/
- https://gist.github.com/anadr/7465a9fde63d41341136949f14c21105
- https://admx.help/?Category=Windows_7_2008R2&Policy=Microsoft.Policies.WindowsDefender::SpyNetReporting
- https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/ransomware-hive-conti-avoslocker
- https://www.tenforums.com/tutorials/32236-enable-disable-microsoft-defender-pua-protection-windows-10-a.html
- https://www.tenforums.com/tutorials/105533-enable-disable-windows-defender-exploit-protection-settings.html
- https://www.tenforums.com/tutorials/123792-turn-off-tamper-protection-microsoft-defender-antivirus.html
- https://securelist.com/key-group-ransomware-samples-and-telegram-schemes/114025/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_windows_defender_tamper.yml)
