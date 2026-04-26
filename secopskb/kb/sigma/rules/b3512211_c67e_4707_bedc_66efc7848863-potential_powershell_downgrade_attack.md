---
sigma_id: "b3512211-c67e-4707-bedc-66efc7848863"
title: "Potential PowerShell Downgrade Attack"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_downgrade_attack.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_downgrade_attack.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "b3512211-c67e-4707-bedc-66efc7848863"
  - "Potential PowerShell Downgrade Attack"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential PowerShell Downgrade Attack

Detects PowerShell downgrade attack by comparing the host versions with the actually used engine version 2.0

## Metadata

- Rule ID: b3512211-c67e-4707-bedc-66efc7848863
- Status: test
- Level: medium
- Author: Harish Segar (rule)
- Date: 2020-03-20
- Modified: 2023-01-04
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_downgrade_attack.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection:
  Image|endswith: \powershell.exe
  CommandLine|contains:
  - ' -version 2 '
  - ' -versio 2 '
  - ' -versi 2 '
  - ' -vers 2 '
  - ' -ver 2 '
  - ' -ve 2 '
  - ' -v 2 '
condition: selection
```

## False Positives

- Unknown

## References

- http://www.leeholmes.com/blog/2017/03/17/detecting-and-preventing-powershell-downgrade-attacks/
- https://github.com/r00t-3xp10it/hacking-material-books/blob/43cb1e1932c16ff1f58b755bc9ab6b096046853f/obfuscation/simple_obfuscation.md#bypass-or-avoid-amsi-by-version-downgrade-

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_downgrade_attack.yml)
