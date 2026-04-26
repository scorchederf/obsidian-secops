---
sigma_id: "cd951fdc-4b2f-47f5-ba99-a33bf61e3770"
title: "Always Install Elevated Windows Installer"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_always_install_elevated_windows_installer.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_always_install_elevated_windows_installer.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "cd951fdc-4b2f-47f5-ba99-a33bf61e3770"
  - "Always Install Elevated Windows Installer"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Always Install Elevated Windows Installer

Detects Windows Installer service (msiexec.exe) trying to install MSI packages with SYSTEM privilege

## Metadata

- Rule ID: cd951fdc-4b2f-47f5-ba99-a33bf61e3770
- Status: test
- Level: medium
- Author: Teymur Kheirkhabarov (idea), Mangatas Tondang (rule), oscd.community
- Date: 2020-10-13
- Modified: 2024-12-01
- Source Path: rules/windows/process_creation/proc_creation_win_susp_always_install_elevated_windows_installer.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Detection

```yaml
selection_user:
  User|contains:
  - AUTHORI
  - AUTORI
selection_image_1:
  Image|contains|all:
  - \Windows\Installer\
  - msi
  Image|endswith: tmp
selection_image_2:
  Image|endswith: \msiexec.exe
  IntegrityLevel:
  - System
  - S-1-16-16384
filter_installer:
  ParentImage: C:\Windows\System32\services.exe
filter_repair:
- CommandLine|endswith: \system32\msiexec.exe /V
- ParentCommandLine|endswith: \system32\msiexec.exe /V
filter_sophos:
  ParentImage|startswith: C:\ProgramData\Sophos\
filter_avira:
  ParentImage|startswith: C:\ProgramData\Avira\
filter_avast:
  ParentImage|startswith:
  - C:\Program Files\Avast Software\
  - C:\Program Files (x86)\Avast Software\
filter_google_update:
  ParentImage|startswith:
  - C:\Program Files\Google\Update\
  - C:\Program Files (x86)\Google\Update\
condition: 1 of selection_image_* and selection_user and not 1 of filter_*
```

## False Positives

- System administrator usage
- Anti virus products
- WindowsApps located in "C:\Program Files\WindowsApps\"

## References

- https://image.slidesharecdn.com/kheirkhabarovoffzonefinal-181117201458/95/hunting-for-privilege-escalation-in-windows-environment-48-638.jpg

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_always_install_elevated_windows_installer.yml)
