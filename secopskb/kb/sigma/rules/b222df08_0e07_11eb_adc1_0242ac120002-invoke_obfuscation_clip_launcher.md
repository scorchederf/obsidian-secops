---
sigma_id: "b222df08-0e07-11eb-adc1-0242ac120002"
title: "Invoke-Obfuscation CLIP+ Launcher"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_invoke_obfuscation_clip.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_invoke_obfuscation_clip.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "b222df08-0e07-11eb-adc1-0242ac120002"
  - "Invoke-Obfuscation CLIP+ Launcher"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Invoke-Obfuscation CLIP+ Launcher

Detects Obfuscated use of Clip.exe to execute PowerShell

## Metadata

- Rule ID: b222df08-0e07-11eb-adc1-0242ac120002
- Status: test
- Level: high
- Author: Jonathan Cheong, oscd.community
- Date: 2020-10-13
- Modified: 2022-11-17
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_invoke_obfuscation_clip.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - cmd
  - '&&'
  - 'clipboard]::'
  - -f
  CommandLine|contains:
  - /c
  - /r
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/SigmaHQ/sigma/issues/1009

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_invoke_obfuscation_clip.yml)
