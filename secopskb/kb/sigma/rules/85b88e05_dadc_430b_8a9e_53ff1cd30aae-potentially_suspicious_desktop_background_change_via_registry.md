---
sigma_id: "85b88e05-dadc-430b-8a9e-53ff1cd30aae"
title: "Potentially Suspicious Desktop Background Change Via Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_desktop_background_change.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_desktop_background_change.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "85b88e05-dadc-430b-8a9e-53ff1cd30aae"
  - "Potentially Suspicious Desktop Background Change Via Registry"
attack_technique_ids:
  - "T1112"
  - "T1491.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potentially Suspicious Desktop Background Change Via Registry

Detects registry value settings that would replace the user's desktop background.
This is a common technique used by malware to change the desktop background to a ransom note or other image.

## Metadata

- Rule ID: 85b88e05-dadc-430b-8a9e-53ff1cd30aae
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), Stephen Lincoln @slincoln-aiq (AttackIQ)
- Date: 2023-12-21
- Modified: 2025-10-17
- Source Path: rules/windows/registry/registry_set/registry_set_desktop_background_change.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]
- [[kb/attack/techniques/T1491-defacement|T1491.001]]

## Detection

```yaml
selection_keys:
  TargetObject|contains:
  - Control Panel\Desktop
  - CurrentVersion\Policies\ActiveDesktop
  - CurrentVersion\Policies\System
selection_values_1:
  TargetObject|endswith: NoChangingWallpaper
  Details: DWORD (0x00000001)
selection_values_2:
  TargetObject|endswith: \Wallpaper
selection_values_3:
  TargetObject|endswith: \WallpaperStyle
  Details: '2'
filter_main_svchost:
  Image|endswith: \svchost.exe
filter_main_empty:
  TargetObject|endswith: \Control Panel\Desktop\Wallpaper
  Details: (Empty)
filter_main_explorer:
  Image|endswith: C:\Windows\Explorer.EXE
filter_optional_ec2launch:
  Image:
  - C:\Program Files\Amazon\EC2Launch\EC2Launch.exe
  - C:\Program Files (x86)\Amazon\EC2Launch\EC2Launch.exe
  TargetObject|endswith: \Control Panel\Desktop\Wallpaper
condition: selection_keys and 1 of selection_values_* and not 1 of filter_main_* and
  not 1 of filter_optional_*
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

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_desktop_background_change.yml)
