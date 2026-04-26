---
sigma_id: "e1561947-b4e3-4a74-9bdd-83baed21bdb5"
title: "Invoke-Obfuscation Via Use Clip"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_invoke_obfuscation_via_use_clip.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_invoke_obfuscation_via_use_clip.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "e1561947-b4e3-4a74-9bdd-83baed21bdb5"
  - "Invoke-Obfuscation Via Use Clip"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Invoke-Obfuscation Via Use Clip

Detects Obfuscated Powershell via use Clip.exe in Scripts

## Metadata

- Rule ID: e1561947-b4e3-4a74-9bdd-83baed21bdb5
- Status: test
- Level: high
- Author: Nikita Nazarov, oscd.community
- Date: 2020-10-09
- Modified: 2024-04-15
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_invoke_obfuscation_via_use_clip.yml

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
  CommandLine|re: (?i)echo.*clip.*&&.*(Clipboard|i`?n`?v`?o`?k`?e`?)
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/SigmaHQ/sigma/issues/1009

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_invoke_obfuscation_via_use_clip.yml)
