---
sigma_id: "3a9fa2ec-30bc-4ebd-b49e-7c9cff225502"
title: "VsCode Powershell Profile Modification"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_susp_vscode_powershell_profile.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_vscode_powershell_profile.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "3a9fa2ec-30bc-4ebd-b49e-7c9cff225502"
  - "VsCode Powershell Profile Modification"
attack_technique_ids:
  - "T1546.013"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# VsCode Powershell Profile Modification

Detects the creation or modification of a vscode related powershell profile which could indicate suspicious activity as the profile can be used as a mean of persistence

## Metadata

- Rule ID: 3a9fa2ec-30bc-4ebd-b49e-7c9cff225502
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-24
- Modified: 2023-01-06
- Source Path: rules/windows/file/file_event/file_event_win_susp_vscode_powershell_profile.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.013]]

## Detection

```yaml
selection:
  TargetFilename|endswith: \Microsoft.VSCode_profile.ps1
condition: selection
```

## False Positives

- Legitimate use of the profile by developers or administrators

## References

- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_profiles?view=powershell-7.2

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_vscode_powershell_profile.yml)
