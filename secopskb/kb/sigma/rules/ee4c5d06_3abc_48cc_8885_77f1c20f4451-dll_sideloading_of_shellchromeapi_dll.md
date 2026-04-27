---
sigma_id: "ee4c5d06-3abc-48cc-8885-77f1c20f4451"
title: "DLL Sideloading Of ShellChromeAPI.DLL"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_shell_chrome_api.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_shell_chrome_api.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / image_load"
aliases:
  - "ee4c5d06-3abc-48cc-8885-77f1c20f4451"
  - "DLL Sideloading Of ShellChromeAPI.DLL"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# DLL Sideloading Of ShellChromeAPI.DLL

Detects processes loading the non-existent DLL "ShellChromeAPI". One known example is the "DeviceEnroller" binary in combination with the "PhoneDeepLink" flag tries to load this DLL.
Adversaries can drop their own renamed DLL and execute it via DeviceEnroller.exe using this parameter

## Metadata

- Rule ID: ee4c5d06-3abc-48cc-8885-77f1c20f4451
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-12-01
- Source Path: rules/windows/image_load/image_load_side_load_shell_chrome_api.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  ImageLoaded|endswith: \ShellChromeAPI.dll
condition: selection
```

## False Positives

- Unknown

## References

- https://mobile.twitter.com/0gtweet/status/1564131230941122561
- https://strontic.github.io/xcyclopedia/library/DeviceEnroller.exe-24BEF0D6B0ECED36BB41831759FDE18D.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_shell_chrome_api.yml)
