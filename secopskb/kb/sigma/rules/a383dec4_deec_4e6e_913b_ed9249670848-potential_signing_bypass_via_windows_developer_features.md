---
sigma_id: "a383dec4-deec-4e6e-913b-ed9249670848"
title: "Potential Signing Bypass Via Windows Developer Features"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_systemsettingsadminflows_turn_on_dev_features.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_systemsettingsadminflows_turn_on_dev_features.yml"
build_date: "2026-04-27 19:13:54"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "a383dec4-deec-4e6e-913b-ed9249670848"
  - "Potential Signing Bypass Via Windows Developer Features"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects when a user enable developer features such as "Developer Mode" or "Application Sideloading". Which allows the user to install untrusted packages.

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_img:
- Image|endswith: \SystemSettingsAdminFlows.exe
- OriginalFileName: SystemSettingsAdminFlows.EXE
selection_flag:
  CommandLine|contains: TurnOnDeveloperFeatures
selection_options:
  CommandLine|contains:
  - DeveloperUnlock
  - EnableSideloading
condition: all of selection_*
```

## False Positives

- Unknown

## References

- Internal Research
- https://www.sentinelone.com/labs/inside-malicious-windows-apps-for-malware-deployment/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_systemsettingsadminflows_turn_on_dev_features.yml)
