---
sigma_id: "14c71865-6cd3-44ae-adaa-1db923fae5f2"
title: "Tamper Windows Defender - ScriptBlockLogging"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_tamper_windows_defender_set_mp.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_tamper_windows_defender_set_mp.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "14c71865-6cd3-44ae-adaa-1db923fae5f2"
  - "Tamper Windows Defender - ScriptBlockLogging"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Tamper Windows Defender - ScriptBlockLogging

Detects PowerShell scripts attempting to disable scheduled scanning and other parts of Windows Defender ATP or set default actions to allow.

## Metadata

- Rule ID: 14c71865-6cd3-44ae-adaa-1db923fae5f2
- Status: test
- Level: high
- Author: frack113, elhoim, Tim Shelton (fps, alias support), Swachchhanda Shrawan Poudel, Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-01-16
- Modified: 2024-01-02
- Source Path: rules/windows/powershell/powershell_script/posh_ps_tamper_windows_defender_set_mp.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection_options_disabling_preference:
  ScriptBlockText|contains: Set-MpPreference
selection_options_disabling_function:
  ScriptBlockText|contains:
  - -dbaf $true
  - -dbaf 1
  - -dbm $true
  - -dbm 1
  - -dips $true
  - -dips 1
  - -DisableArchiveScanning $true
  - -DisableArchiveScanning 1
  - -DisableBehaviorMonitoring $true
  - -DisableBehaviorMonitoring 1
  - -DisableBlockAtFirstSeen $true
  - -DisableBlockAtFirstSeen 1
  - -DisableCatchupFullScan $true
  - -DisableCatchupFullScan 1
  - -DisableCatchupQuickScan $true
  - -DisableCatchupQuickScan 1
  - -DisableIntrusionPreventionSystem $true
  - -DisableIntrusionPreventionSystem 1
  - -DisableIOAVProtection $true
  - -DisableIOAVProtection 1
  - -DisableRealtimeMonitoring $true
  - -DisableRealtimeMonitoring 1
  - -DisableRemovableDriveScanning $true
  - -DisableRemovableDriveScanning 1
  - -DisableScanningMappedNetworkDrivesForFullScan $true
  - -DisableScanningMappedNetworkDrivesForFullScan 1
  - -DisableScanningNetworkFiles $true
  - -DisableScanningNetworkFiles 1
  - -DisableScriptScanning $true
  - -DisableScriptScanning 1
  - -MAPSReporting $false
  - -MAPSReporting 0
  - -drdsc $true
  - -drdsc 1
  - -drtm $true
  - -drtm 1
  - -dscrptsc $true
  - -dscrptsc 1
  - -dsmndf $true
  - -dsmndf 1
  - -dsnf $true
  - -dsnf 1
  - -dss $true
  - -dss 1
selection_other_default_actions_allow:
  ScriptBlockText|contains: Set-MpPreference
selection_other_default_actions_func:
  ScriptBlockText|contains:
  - HighThreatDefaultAction Allow
  - htdefac Allow
  - LowThreatDefaultAction Allow
  - ltdefac Allow
  - ModerateThreatDefaultAction Allow
  - mtdefac Allow
  - SevereThreatDefaultAction Allow
  - stdefac Allow
condition: all of selection_options_disabling_* or all of selection_other_default_actions_*
```

## False Positives

- Legitimate PowerShell scripts that disable Windows Defender for troubleshooting purposes. Must be investigated.

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1562.001/T1562.001.md
- https://learn.microsoft.com/en-us/powershell/module/defender/set-mppreference?view=windowsserver2022-ps
- https://bidouillesecurity.com/disable-windows-defender-in-powershell/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_tamper_windows_defender_set_mp.yml)
