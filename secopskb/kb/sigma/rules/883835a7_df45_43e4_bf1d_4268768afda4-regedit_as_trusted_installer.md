---
sigma_id: "883835a7-df45-43e4-bf1d-4268768afda4"
title: "Regedit as Trusted Installer"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_regedit_trustedinstaller.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_regedit_trustedinstaller.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "883835a7-df45-43e4-bf1d-4268768afda4"
  - "Regedit as Trusted Installer"
attack_technique_ids:
  - "T1548"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Regedit as Trusted Installer

Detects a regedit started with TrustedInstaller privileges or by ProcessHacker.exe

## Metadata

- Rule ID: 883835a7-df45-43e4-bf1d-4268768afda4
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2021-05-27
- Modified: 2022-10-09
- Source Path: rules/windows/process_creation/proc_creation_win_regedit_trustedinstaller.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548]]

## Detection

```yaml
selection:
  Image|endswith: \regedit.exe
  ParentImage|endswith:
  - \TrustedInstaller.exe
  - \ProcessHacker.exe
condition: selection
```

## False Positives

- Unlikely

## References

- https://twitter.com/1kwpeter/status/1397816101455765504

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_regedit_trustedinstaller.yml)
