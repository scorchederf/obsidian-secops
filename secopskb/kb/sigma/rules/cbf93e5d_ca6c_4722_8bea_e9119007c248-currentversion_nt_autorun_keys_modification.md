---
sigma_id: "cbf93e5d-ca6c-4722-8bea-e9119007c248"
title: "CurrentVersion NT Autorun Keys Modification"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_currentversion_nt.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_currentversion_nt.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "cbf93e5d-ca6c-4722-8bea-e9119007c248"
  - "CurrentVersion NT Autorun Keys Modification"
attack_technique_ids:
  - "T1547.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# CurrentVersion NT Autorun Keys Modification

Detects modification of autostart extensibility point (ASEP) in registry.

## Metadata

- Rule ID: cbf93e5d-ca6c-4722-8bea-e9119007c248
- Status: test
- Level: medium
- Author: Victor Sergeev, Daniil Yugoslavskiy, Gleb Sukhodolskiy, Timur Zinniatullin, oscd.community, Tim Shelton, frack113 (split)
- Date: 2019-10-25
- Modified: 2025-10-22
- Source Path: rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_currentversion_nt.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.001]]

## Detection

```yaml
selection_nt_current_version_base:
  TargetObject|contains: \SOFTWARE\Microsoft\Windows NT\CurrentVersion
selection_nt_current_version:
  TargetObject|contains:
  - \Winlogon\VmApplet
  - \Winlogon\Userinit
  - \Winlogon\Taskman
  - \Winlogon\Shell
  - \Winlogon\GpExtensions
  - \Winlogon\AppSetup
  - \Winlogon\AlternateShells\AvailableShells
  - \Windows\IconServiceLib
  - \Windows\Appinit_Dlls
  - \Image File Execution Options
  - \Font Drivers
  - \Drivers32
  - \Windows\Run
  - \Windows\Load
filter_main_empty:
  Details: (Empty)
filter_main_null:
  Details: null
filter_main_poqexec:
  Image: C:\Windows\System32\poqexec.exe
filter_main_legitimate_subkey:
  TargetObject|contains: \Image File Execution Options\
  TargetObject|endswith:
  - \DisableExceptionChainValidation
  - \MitigationOptions
filter_main_security_extension_dc:
  Image: C:\Windows\system32\svchost.exe
  TargetObject|contains:
  - \Winlogon\GPExtensions\{827D319E-6EAC-11D2-A4EA-00C04F79F83A}\PreviousPolicyAreas
  - \Winlogon\GPExtensions\{827D319E-6EAC-11D2-A4EA-00C04F79F83A}\MaxNoGPOListChangesInterval
  Details:
  - DWORD (0x00000001)
  - DWORD (0x00000009)
  - DWORD (0x000003c0)
filter_main_runtimebroker:
  Image: C:\Windows\System32\RuntimeBroker.exe
  TargetObject|contains: \runtimebroker.exe\Microsoft.Windows.ShellExperienceHost
filter_optional_edge:
  Image|startswith: C:\Program Files (x86)\Microsoft\Temp\
  Image|endswith: \MicrosoftEdgeUpdate.exe
filter_optional_avguard:
  Image|startswith:
  - C:\Program Files (x86)\Avira\Antivirus\avguard.exe
  - C:\Program Files\Avira\Antivirus\avguard.exe
  TargetObject|contains: SOFTWARE\WOW6432Node\Avira\Antivirus\Overwrite_Keys\HKEY_LOCAL_MACHINE\Software\Microsoft\Windows
    NT\CurrentVersion\Winlogon\
  TargetObject|endswith:
  - \userinit\UseAsDefault
  - \shell\UseAsDefault
  Details:
  - explorer.exe
  - C:\Windows\system32\userinit.exe,
filter_optional_msoffice:
- TargetObject|contains:
  - \ClickToRunStore\HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\
  - \ClickToRun\REGISTRY\MACHINE\Software\Microsoft\Windows NT\CurrentVersion\
- Image:
  - C:\Program Files\Microsoft Office\root\integration\integrator.exe
  - C:\Program Files (x86)\Microsoft Office\root\integration\integrator.exe
filter_optional_officeclicktorun:
  Image|startswith:
  - C:\Program Files\Common Files\Microsoft Shared\ClickToRun\
  - C:\Program Files\Common Files\Microsoft Shared\ClickToRun\Updates\
  Image|endswith: \OfficeClickToRun.exe
filter_optional_ngen:
  Image|startswith: C:\Windows\Microsoft.NET\Framework
  Image|endswith: \ngen.exe
filter_optional_onedrive:
  Image|endswith: \AppData\Local\Microsoft\OneDrive\StandaloneUpdater\OneDriveSetup.exe
  TargetObject|endswith: \Microsoft\Windows\CurrentVersion\RunOnce\Delete Cached Update
    Binary
  Details|startswith: C:\Windows\system32\cmd.exe /q /c del /q "C:\Users\
  Details|endswith: \AppData\Local\Microsoft\OneDrive\Update\OneDriveSetup.exe"
condition: all of selection_* and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Legitimate software automatically (mostly, during installation) sets up autorun keys for legitimate reason
- Legitimate administrator sets up autorun keys for legitimate reason

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1547.001/T1547.001.md
- https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns
- https://gist.github.com/GlebSukhodolskiy/0fc5fa5f482903064b448890db1eaf9d

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_currentversion_nt.yml)
