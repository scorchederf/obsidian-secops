---
sigma_id: "f0ca6c24-3225-47d5-b1f5-352bf07ecfa7"
title: "PUA - DefenderCheck Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_defendercheck.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_defendercheck.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "f0ca6c24-3225-47d5-b1f5-352bf07ecfa7"
  - "PUA - DefenderCheck Execution"
attack_technique_ids:
  - "T1027.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PUA - DefenderCheck Execution

Detects the use of DefenderCheck, a tool to evaluate the signatures used in Microsoft Defender. It can be used to figure out the strings / byte chains used in Microsoft Defender to detect a tool and thus used for AV evasion.

## Metadata

- Rule ID: f0ca6c24-3225-47d5-b1f5-352bf07ecfa7
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-08-30
- Modified: 2023-02-04
- Source Path: rules/windows/process_creation/proc_creation_win_pua_defendercheck.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027.005]]

## Detection

```yaml
selection:
- Image|endswith: \DefenderCheck.exe
- Description: DefenderCheck
condition: selection
```

## False Positives

- Unlikely

## References

- https://github.com/matterpreter/DefenderCheck

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_defendercheck.yml)
