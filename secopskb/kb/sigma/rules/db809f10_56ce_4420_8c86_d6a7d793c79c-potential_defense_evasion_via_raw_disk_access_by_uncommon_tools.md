---
sigma_id: "db809f10-56ce-4420-8c86-d6a7d793c79c"
title: "Potential Defense Evasion Via Raw Disk Access By Uncommon Tools"
framework: "sigma"
generated: "true"
source_path: "rules/windows/raw_access_thread/raw_access_thread_susp_disk_access_using_uncommon_tools.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/raw_access_thread/raw_access_thread_susp_disk_access_using_uncommon_tools.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "low"
logsource: "windows / raw_access_thread"
aliases:
  - "db809f10-56ce-4420-8c86-d6a7d793c79c"
  - "Potential Defense Evasion Via Raw Disk Access By Uncommon Tools"
attack_technique_ids:
  - "T1006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Defense Evasion Via Raw Disk Access By Uncommon Tools

Detects raw disk access using uncommon tools or tools that are located in suspicious locations (heavy filtering is required), which could indicate possible defense evasion attempts

## Metadata

- Rule ID: db809f10-56ce-4420-8c86-d6a7d793c79c
- Status: test
- Level: low
- Author: Teymur Kheirkhabarov, oscd.community
- Date: 2019-10-22
- Modified: 2025-12-03
- Source Path: rules/windows/raw_access_thread/raw_access_thread_susp_disk_access_using_uncommon_tools.yml

## Logsource

- category: raw_access_thread
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1006-direct_volume_access|T1006]]

## Detection

```yaml
filter_main_floppy:
  Device|contains: floppy
filter_main_generic:
  Image|startswith:
  - C:\$WINDOWS.~BT\
  - C:\Program Files (x86)\
  - C:\Program Files\
  - C:\Windows\CCM\
  - C:\Windows\explorer.exe
  - C:\Windows\servicing\
  - C:\Windows\SoftwareDistribution\
  - C:\Windows\System32\
  - C:\Windows\SystemApps\
  - C:\Windows\SysWOW64\
  - C:\Windows\uus\
  - C:\Windows\WinSxS\
filter_main_system_images:
  Image:
  - Registry
  - System
filter_main_windefender:
  Image|startswith: C:\ProgramData\Microsoft\Windows Defender\Platform\
  Image|endswith:
  - \MsMpEng.exe
  - \MpDefenderCoreService.exe
filter_main_microsoft_appdata:
  Image|startswith: C:\Users\
  Image|contains|all:
  - \AppData\
  - \Microsoft\
filter_main_ssd_nvme:
  Image|startswith: C:\Windows\Temp\
  Image|endswith:
  - \Executables\SSDUpdate.exe
  - \HostMetadata\NVMEHostmetadata.exe
filter_main_null:
  Image: null
filter_main_systemsettings:
  Image: C:\Windows\ImmersiveControlPanel\SystemSettings.exe
filter_main_update:
  Image|startswith: C:\$WinREAgent\Scratch\
filter_optional_github_desktop:
  Image|startswith: C:\Users\
  Image|contains: \AppData\Local\GitHubDesktop\app-
  Image|endswith: \resources\app\git\mingw64\bin\git.exe
filter_optional_nextron:
  Image|startswith: C:\Windows\Temp\asgard2-agent\
  Image|endswith: \thor.exe
filter_optional_Keybase:
  Image|startswith: C:\Users\
  Image|contains: \AppData\Local\Keybase\upd.exe
condition: not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Likely

## References

- https://www.slideshare.net/heirhabarov/hunting-for-credentials-dumping-in-windows-environment

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/raw_access_thread/raw_access_thread_susp_disk_access_using_uncommon_tools.yml)
