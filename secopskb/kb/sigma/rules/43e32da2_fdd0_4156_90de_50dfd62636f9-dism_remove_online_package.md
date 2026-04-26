---
sigma_id: "43e32da2-fdd0-4156-90de-50dfd62636f9"
title: "Dism Remove Online Package"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_dism_remove.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dism_remove.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "43e32da2-fdd0-4156-90de-50dfd62636f9"
  - "Dism Remove Online Package"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Dism Remove Online Package

Deployment Image Servicing and Management tool. DISM is used to enumerate, install, uninstall, configure, and update features and packages in Windows images

## Metadata

- Rule ID: 43e32da2-fdd0-4156-90de-50dfd62636f9
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-01-16
- Modified: 2022-08-26
- Source Path: rules/windows/process_creation/proc_creation_win_dism_remove.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection_dismhost:
  Image|endswith: \DismHost.exe
  ParentCommandLine|contains|all:
  - /Online
  - /Disable-Feature
selection_dism:
  Image|endswith: \Dism.exe
  CommandLine|contains|all:
  - /Online
  - /Disable-Feature
condition: 1 of selection_*
```

## False Positives

- Legitimate script

## Simulation

### Disable Windows Defender with DISM

- atomic_guid: 871438ac-7d6e-432a-b27d-3e7db69faf58
- name: Disable Windows Defender with DISM
- technique: T1562.001
- type: atomic-red-team

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1562.001/T1562.001.md#atomic-test-26---disable-windows-defender-with-dism
- https://www.trendmicro.com/en_us/research/22/h/ransomware-actor-abuses-genshin-impact-anti-cheat-driver-to-kill-antivirus.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dism_remove.yml)
