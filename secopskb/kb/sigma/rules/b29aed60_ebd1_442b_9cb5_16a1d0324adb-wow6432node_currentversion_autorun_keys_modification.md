---
sigma_id: "b29aed60-ebd1-442b-9cb5-16a1d0324adb"
title: "Wow6432Node CurrentVersion Autorun Keys Modification"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_wow6432node.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_wow6432node.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "b29aed60-ebd1-442b-9cb5-16a1d0324adb"
  - "Wow6432Node CurrentVersion Autorun Keys Modification"
attack_technique_ids:
  - "T1547.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Wow6432Node CurrentVersion Autorun Keys Modification

Detects modification of autostart extensibility point (ASEP) in registry.

## Metadata

- Rule ID: b29aed60-ebd1-442b-9cb5-16a1d0324adb
- Status: test
- Level: medium
- Author: Victor Sergeev, Daniil Yugoslavskiy, Gleb Sukhodolskiy, Timur Zinniatullin, oscd.community, Tim Shelton, frack113 (split)
- Date: 2019-10-25
- Modified: 2025-12-08
- Source Path: rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_wow6432node.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.001]]

## Detection

```yaml
selection_wow_current_version_base:
  TargetObject|contains: \SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion
selection_wow_current_version_keys:
  TargetObject|contains:
  - \ShellServiceObjectDelayLoad
  - \Run\
  - \RunOnce\
  - \RunOnceEx\
  - \RunServices\
  - \RunServicesOnce\
  - \Explorer\ShellServiceObjects
  - \Explorer\ShellIconOverlayIdentifiers
  - \Explorer\ShellExecuteHooks
  - \Explorer\SharedTaskScheduler
  - \Explorer\Browser Helper Objects
filter_main_empty:
  Details: (Empty)
filter_main_null:
  Details: null
filter_main_ms_win_desktop_runtime:
  Details|startswith: '"C:\ProgramData\Package Cache\{d21a4f20-968a-4b0c-bf04-a38da5f06e41}\windowsdesktop-runtime-'
filter_main_vcredist:
  Image|endswith: \VC_redist.x64.exe
  Details|endswith: '}\VC_redist.x64.exe" /burn.runonce'
filter_main_upgrades:
  Image|startswith:
  - C:\ProgramData\Package Cache
  - C:\Windows\Temp\
  Image|contains:
  - \winsdksetup.exe
  - \windowsdesktop-runtime-
  - \AspNetCoreSharedFrameworkBundle-
  Details|endswith: ' /burn.runonce'
filter_main_uninstallers:
  Image|startswith: C:\Windows\Installer\MSI
  TargetObject|contains: \Explorer\Browser Helper Objects
filter_main_msiexec:
  Image: C:\WINDOWS\system32\msiexec.exe
  TargetObject|contains: \SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Run\
filter_main_edge:
  Image|contains|all:
  - C:\Program Files (x86)\Microsoft\EdgeUpdate\Install\{
  - \setup.exe
filter_optional_msoffice1:
  Image: C:\Program Files\Common Files\Microsoft Shared\ClickToRun\OfficeClickToRun.exe
  TargetObject|contains: \Office\ClickToRun\REGISTRY\MACHINE\Software\Wow6432Node\
filter_optional_msoffice2:
  Image:
  - C:\Program Files\Microsoft Office\root\integration\integrator.exe
  - C:\Program Files (x86)\Microsoft Office\root\integration\integrator.exe
  TargetObject|contains: \Explorer\Browser Helper Objects\{31D09BA0-12F5-4CCE-BE8A-2923E76605DA}\
filter_optional_dropbox:
- Details|endswith: -A251-47B7-93E1-CDD82E34AF8B}
- Details: grpconv -o
- Details|contains|all:
  - C:\Program Files
  - \Dropbox\Client\Dropbox.exe
  - ' /systemstartup'
filter_optional_evernote:
  TargetObject|endswith: \Explorer\Browser Helper Objects\{92EF2EAD-A7CE-4424-B0DB-499CF856608E}\NoExplorer
filter_optional_dotnet:
  Image|contains: \windowsdesktop-runtime-
  TargetObject|endswith:
  - \WOW6432Node\Microsoft\Windows\CurrentVersion\RunOnce\{e2d1ae32-dd1d-4ad7-a298-10e42e7840fc}
  - \WOW6432Node\Microsoft\Windows\CurrentVersion\RunOnce\{7037b699-7382-448c-89a7-4765961d2537}
  Details|startswith: '"C:\ProgramData\Package Cache\'
  Details|endswith: .exe" /burn.runonce
filter_optional_office:
  Image|startswith:
  - C:\Program Files\Common Files\Microsoft Shared\ClickToRun\
  - C:\Program Files\Common Files\Microsoft Shared\ClickToRun\Updates\
  Image|endswith: \OfficeClickToRun.exe
filter_optional_discord:
  TargetObject|endswith: \SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Run\Discord
  Details|endswith: Discord.exe --checkInstall
filter_optional_avira:
  Details|endswith: \Avira.OE.Setup.Bundle.exe" /burn.runonce
  Image|endswith: \Avira.OE.Setup.Bundle.exe
filter_optional_avg_1:
  Image|endswith: \instup.exe
  TargetObject|endswith: \SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\RunOnce\AvRepair
  Details|endswith: instup.exe" /instop:repair /wait
filter_optional_avg_2:
  Image|endswith: \instup.exe
  TargetObject|endswith:
  - \SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Explorer\ShellIconOverlayIdentifiers\00avg\(Default)
  - \SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Explorer\ShellIconOverlayIdentifiers\00asw\(Default)
  Details:
  - '{472083B1-C522-11CF-8763-00608CC02F24}'
  - '{472083B0-C522-11CF-8763-00608CC02F24}'
condition: all of selection_* and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Legitimate software automatically (mostly, during installation) sets up autorun keys for legitimate reason
- Legitimate administrator sets up autorun keys for legitimate reason

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1547.001/T1547.001.md
- https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns
- https://gist.github.com/GlebSukhodolskiy/0fc5fa5f482903064b448890db1eaf9d
- https://oddvar.moe/2018/03/21/persistence-using-runonceex-hidden-from-autoruns-exe/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_wow6432node.yml)
