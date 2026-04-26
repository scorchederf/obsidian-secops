---
sigma_id: "27aec9c9-dbb0-4939-8422-1742242471d0"
title: "Invoke-Obfuscation VAR+ Launcher"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_invoke_obfuscation_var.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_invoke_obfuscation_var.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "27aec9c9-dbb0-4939-8422-1742242471d0"
  - "Invoke-Obfuscation VAR+ Launcher"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Invoke-Obfuscation VAR+ Launcher

Detects Obfuscated use of Environment Variables to execute PowerShell

## Metadata

- Rule ID: 27aec9c9-dbb0-4939-8422-1742242471d0
- Status: test
- Level: high
- Author: Jonathan Cheong, oscd.community
- Date: 2020-10-15
- Modified: 2024-04-15
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_invoke_obfuscation_var.yml

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
  CommandLine|re: cmd.{0,5}(?:/c|/r)(?:\s|)\"set\s[a-zA-Z]{3,6}.*(?:\{\d\}){1,}\\\"\s+?\-f(?:.*\)){1,}.*\"
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/SigmaHQ/sigma/issues/1009

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_invoke_obfuscation_var.yml)
