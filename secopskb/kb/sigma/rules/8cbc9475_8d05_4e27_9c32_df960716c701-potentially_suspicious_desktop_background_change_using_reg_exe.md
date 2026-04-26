---
sigma_id: "8cbc9475-8d05-4e27-9c32-df960716c701"
title: "Potentially Suspicious Desktop Background Change Using Reg.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_reg_desktop_background_change.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_desktop_background_change.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "8cbc9475-8d05-4e27-9c32-df960716c701"
  - "Potentially Suspicious Desktop Background Change Using Reg.EXE"
attack_technique_ids:
  - "T1112"
  - "T1491.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potentially Suspicious Desktop Background Change Using Reg.EXE

Detects the execution of "reg.exe" to alter registry keys that would replace the user's desktop background.
This is a common technique used by malware to change the desktop background to a ransom note or other image.

## Metadata

- Rule ID: 8cbc9475-8d05-4e27-9c32-df960716c701
- Status: test
- Level: medium
- Author: Stephen Lincoln @slincoln-aiq (AttackIQ)
- Date: 2023-12-21
- Source Path: rules/windows/process_creation/proc_creation_win_reg_desktop_background_change.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]
- [[kb/attack/techniques/T1491-defacement|T1491.001]]

## Detection

```yaml
selection_reg_img:
- Image|endswith: \reg.exe
- OriginalFileName: reg.exe
selection_reg_flag:
  CommandLine|contains: add
selection_keys:
  CommandLine|contains:
  - Control Panel\Desktop
  - CurrentVersion\Policies\ActiveDesktop
  - CurrentVersion\Policies\System
selection_cli_reg_1:
  CommandLine|contains|all:
  - /v NoChangingWallpaper
  - /d 1
selection_cli_reg_2:
  CommandLine|contains|all:
  - /v Wallpaper
  - /t REG_SZ
selection_cli_reg_3:
  CommandLine|contains|all:
  - /v WallpaperStyle
  - /d 2
condition: all of selection_reg_* and selection_keys and 1 of selection_cli_reg_*
```

## False Positives

- Administrative scripts that change the desktop background to a company logo or other image.

## References

- https://www.attackiq.com/2023/09/20/emulating-rhysida/
- https://research.checkpoint.com/2023/the-rhysida-ransomware-activity-analysis-and-ties-to-vice-society/
- https://www.trendmicro.com/en_us/research/23/h/an-overview-of-the-new-rhysida-ransomware.html
- https://www.virustotal.com/gui/file/a864282fea5a536510ae86c77ce46f7827687783628e4f2ceb5bf2c41b8cd3c6/behavior
- https://admx.help/?Category=Windows_10_2016&Policy=Microsoft.Policies.WindowsDesktop::Wallpaper
- https://admx.help/?Category=Windows_10_2016&Policy=Microsoft.Policies.ControlPanelDisplay::CPL_Personalization_NoDesktopBackgroundUI

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_desktop_background_change.yml)
