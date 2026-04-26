---
sigma_id: "9c14c9fa-1a63-4a64-8e57-d19280559490"
title: "Invoke-Obfuscation Via Stdin"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_invoke_obfuscation_via_stdin.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_invoke_obfuscation_via_stdin.yml"
build_date: "2026-04-26 15:01:45"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "9c14c9fa-1a63-4a64-8e57-d19280559490"
  - "Invoke-Obfuscation Via Stdin"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Invoke-Obfuscation Via Stdin

Detects Obfuscated Powershell via Stdin in Scripts

## Metadata

- Rule ID: 9c14c9fa-1a63-4a64-8e57-d19280559490
- Status: test
- Level: high
- Author: Nikita Nazarov, oscd.community
- Date: 2020-10-12
- Modified: 2024-04-16
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_invoke_obfuscation_via_stdin.yml

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
  CommandLine|re: (?i)(set).*&&\s?set.*(environment|invoke|\$\{?input).*&&.*"
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/SigmaHQ/sigma/issues/1009

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_invoke_obfuscation_via_stdin.yml)
