---
sigma_id: "6db5eaf9-88f7-4ed9-af7d-9ef2ad12f236"
title: "Winget Admin Settings Modification"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_winget_admin_settings_tampering.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_winget_admin_settings_tampering.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "low"
logsource: "windows / registry_set"
aliases:
  - "6db5eaf9-88f7-4ed9-af7d-9ef2ad12f236"
  - "Winget Admin Settings Modification"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Winget Admin Settings Modification

Detects changes to the AppInstaller (winget) admin settings. Such as enabling local manifest installations or disabling installer hash checks

## Metadata

- Rule ID: 6db5eaf9-88f7-4ed9-af7d-9ef2ad12f236
- Status: test
- Level: low
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-04-17
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_winget_admin_settings_tampering.yml

## Logsource

- category: registry_set
- product: windows

## Detection

```yaml
selection:
  Image|endswith: \winget.exe
  TargetObject|startswith: \REGISTRY\A\
  TargetObject|endswith: \LocalState\admin_settings
condition: selection
```

## False Positives

- The event doesn't contain information about the type of change. False positives are expected with legitimate changes

## References

- https://github.com/nasbench/Misc-Research/tree/b9596e8109dcdb16ec353f316678927e507a5b8d/LOLBINs/Winget
- https://github.com/microsoft/winget-cli/blob/02d2f93807c9851d73eaacb4d8811a76b64b7b01/src/AppInstallerCommonCore/Public/winget/AdminSettings.h#L13

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_winget_admin_settings_tampering.yml)
