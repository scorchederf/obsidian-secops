---
sigma_id: "452bce90-6fb0-43cc-97a5-affc283139b3"
title: "Suspicious Windows Defender Registry Key Tampering Via Reg.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_reg_windows_defender_tamper.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_windows_defender_tamper.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "452bce90-6fb0-43cc-97a5-affc283139b3"
  - "Suspicious Windows Defender Registry Key Tampering Via Reg.EXE"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious Windows Defender Registry Key Tampering Via Reg.EXE

Detects the usage of "reg.exe" to tamper with different Windows Defender registry keys in order to disable some important features related to protection and detection

## Metadata

- Rule ID: 452bce90-6fb0-43cc-97a5-affc283139b3
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Swachchhanda Shrawan Poudel, Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-03-22
- Modified: 2025-06-04
- Source Path: rules/windows/process_creation/proc_creation_win_reg_windows_defender_tamper.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection_root_img:
- Image|endswith: \reg.exe
- OriginalFileName: reg.exe
selection_root_path:
  CommandLine|contains:
  - SOFTWARE\Microsoft\Windows Defender\
  - SOFTWARE\Policies\Microsoft\Windows Defender Security Center
  - SOFTWARE\Policies\Microsoft\Windows Defender\
selection_dword_0:
  CommandLine|contains|all:
  - ' add '
  - d 0
  CommandLine|contains:
  - DisallowExploitProtectionOverride
  - EnableControlledFolderAccess
  - MpEnablePus
  - PUAProtection
  - SpynetReporting
  - SubmitSamplesConsent
  - TamperProtection
selection_dword_1:
  CommandLine|contains|all:
  - ' add '
  - d 1
  CommandLine|contains:
  - DisableAccess
  - DisableAntiSpyware
  - DisableAntiSpywareRealtimeProtection
  - DisableAntiVirus
  - DisableAntiVirusSignatures
  - DisableArchiveScanning
  - DisableBehaviorMonitoring
  - DisableBlockAtFirstSeen
  - DisableCloudProtection
  - DisableConfig
  - DisableEnhancedNotifications
  - DisableIntrusionPreventionSystem
  - DisableIOAVProtection
  - DisableNetworkProtection
  - DisableOnAccessProtection
  - DisablePrivacyMode
  - DisableRealtimeMonitoring
  - DisableRoutinelyTakingAction
  - DisableScanOnRealtimeEnable
  - DisableScriptScanning
  - DisableSecurityCenter
  - Notification_Suppress
  - SignatureDisableUpdateOnStartupWithoutEngine
condition: all of selection_root_* and 1 of selection_dword_*
```

## False Positives

- Rare legitimate use by administrators to test software (should always be investigated)

## References

- https://thedfirreport.com/2022/03/21/apt35-automates-initial-access-using-proxyshell/
- https://github.com/swagkarna/Defeat-Defender-V1.2.0/tree/ae4059c4276da6f6303b8f53cdff085ecae88a91
- https://www.elevenforum.com/t/video-guide-how-to-completely-disable-microsoft-defender-antivirus.14608/page-2
- https://tria.ge/241231-j9yatstqbm/behavioral1

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_windows_defender_tamper.yml)
