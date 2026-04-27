---
sigma_id: "99c4658d-2c5e-4d87-828d-7c066ca537c3"
title: "Disable-WindowsOptionalFeature Command PowerShell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_disable_windows_optional_feature.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_disable_windows_optional_feature.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "99c4658d-2c5e-4d87-828d-7c066ca537c3"
  - "Disable-WindowsOptionalFeature Command PowerShell"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detect built in PowerShell cmdlet Disable-WindowsOptionalFeature, Deployment Image Servicing and Management tool.
Similar to DISM.exe, this cmdlet is used to enumerate, install, uninstall, configure, and update features and packages in Windows images

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]

## Detection

```yaml
selection_cmd:
  ScriptBlockText|contains|all:
  - Disable-WindowsOptionalFeature
  - -Online
  - -FeatureName
selection_feature:
  ScriptBlockText|contains:
  - Windows-Defender-Gui
  - Windows-Defender-Features
  - Windows-Defender
  - Windows-Defender-ApplicationGuard
condition: all of selection*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/5b67c9b141fa3918017f8fa44f2f88f0b1ecb9e1/atomics/T1562.001/T1562.001.md
- https://learn.microsoft.com/en-us/powershell/module/dism/disable-windowsoptionalfeature?view=windowsserver2022-ps

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_disable_windows_optional_feature.yml)
