---
sigma_id: "e173ad47-4388-4012-ae62-bd13f71c18a8"
title: "Potential DLL Sideloading Via DeviceEnroller.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_deviceenroller_dll_sideloading.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_deviceenroller_dll_sideloading.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "e173ad47-4388-4012-ae62-bd13f71c18a8"
  - "Potential DLL Sideloading Via DeviceEnroller.EXE"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential DLL Sideloading Via DeviceEnroller.EXE

Detects the use of the PhoneDeepLink parameter to potentially sideload a DLL file that does not exist. This non-existent DLL file is named "ShellChromeAPI.dll".
Adversaries can drop their own renamed DLL and execute it via DeviceEnroller.exe using this parameter

## Metadata

- Rule ID: e173ad47-4388-4012-ae62-bd13f71c18a8
- Status: test
- Level: medium
- Author: @gott_cyber
- Date: 2022-08-29
- Modified: 2023-02-04
- Source Path: rules/windows/process_creation/proc_creation_win_deviceenroller_dll_sideloading.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection_img:
- Image|endswith: \deviceenroller.exe
- OriginalFileName: deviceenroller.exe
selection_cli:
  CommandLine|contains: /PhoneDeepLink
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://mobile.twitter.com/0gtweet/status/1564131230941122561
- https://strontic.github.io/xcyclopedia/library/DeviceEnroller.exe-24BEF0D6B0ECED36BB41831759FDE18D.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_deviceenroller_dll_sideloading.yml)
