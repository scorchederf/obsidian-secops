---
sigma_id: "a31eeaed-3fd5-478e-a8ba-e62c6b3f9ecc"
title: "Raccine Uninstall"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_disable_raccine.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_disable_raccine.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "a31eeaed-3fd5-478e-a8ba-e62c6b3f9ecc"
  - "Raccine Uninstall"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Raccine Uninstall

Detects commands that indicate a Raccine removal from an end system. Raccine is a free ransomware protection tool.

## Metadata

- Rule ID: a31eeaed-3fd5-478e-a8ba-e62c6b3f9ecc
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2021-01-21
- Modified: 2022-10-09
- Source Path: rules/windows/process_creation/proc_creation_win_susp_disable_raccine.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection1:
  CommandLine|contains|all:
  - 'taskkill '
  - RaccineSettings.exe
selection2:
  CommandLine|contains|all:
  - reg.exe
  - delete
  - Raccine Tray
selection3:
  CommandLine|contains|all:
  - schtasks
  - /DELETE
  - Raccine Rules Updater
condition: 1 of selection*
```

## False Positives

- Legitimate deinstallation by administrative staff

## References

- https://github.com/Neo23x0/Raccine

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_disable_raccine.yml)
