---
sigma_id: "ec19ebab-72dc-40e1-9728-4c0b805d722c"
title: "Tamper Windows Defender - PSClassic"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_classic/posh_pc_tamper_windows_defender_set_mp.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_classic/posh_pc_tamper_windows_defender_set_mp.yml"
build_date: "2026-04-26 15:01:53"
status: "test"
level: "high"
logsource: "windows / ps_classic_provider_start"
aliases:
  - "ec19ebab-72dc-40e1-9728-4c0b805d722c"
  - "Tamper Windows Defender - PSClassic"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Tamper Windows Defender - PSClassic

Attempting to disable scheduled scanning and other parts of Windows Defender ATP or set default actions to allow.

## Metadata

- Rule ID: ec19ebab-72dc-40e1-9728-4c0b805d722c
- Status: test
- Level: high
- Author: frack113, Nasreddine Bencherchali (Nextron Systems)
- Date: 2021-06-07
- Modified: 2024-01-02
- Source Path: rules/windows/powershell/powershell_classic/posh_pc_tamper_windows_defender_set_mp.yml

## Logsource

- category: ps_classic_provider_start
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection_set_mppreference:
  Data|contains: Set-MpPreference
selection_options_bool_allow:
  Data|contains:
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
selection_options_actions_func:
  Data|contains:
  - HighThreatDefaultAction Allow
  - htdefac Allow
  - LowThreatDefaultAction Allow
  - ltdefac Allow
  - ModerateThreatDefaultAction Allow
  - mtdefac Allow
  - SevereThreatDefaultAction Allow
  - stdefac Allow
condition: selection_set_mppreference and 1 of selection_options_*
```

## False Positives

- Legitimate PowerShell scripts that disable Windows Defender for troubleshooting purposes. Must be investigated.

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1562.001/T1562.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_classic/posh_pc_tamper_windows_defender_set_mp.yml)
