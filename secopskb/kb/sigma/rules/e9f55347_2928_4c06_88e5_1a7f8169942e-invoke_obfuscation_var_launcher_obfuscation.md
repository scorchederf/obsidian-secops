---
sigma_id: "e9f55347-2928-4c06-88e5-1a7f8169942e"
title: "Invoke-Obfuscation VAR++ LAUNCHER OBFUSCATION"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_invoke_obfuscation_via_var.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_invoke_obfuscation_via_var.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "e9f55347-2928-4c06-88e5-1a7f8169942e"
  - "Invoke-Obfuscation VAR++ LAUNCHER OBFUSCATION"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Invoke-Obfuscation VAR++ LAUNCHER OBFUSCATION

Detects Obfuscated Powershell via VAR++ LAUNCHER

## Metadata

- Rule ID: e9f55347-2928-4c06-88e5-1a7f8169942e
- Status: test
- Level: high
- Author: Timur Zinniatullin, oscd.community
- Date: 2020-10-13
- Modified: 2022-11-16
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_invoke_obfuscation_via_var.yml

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
  - '&&set'
  - cmd
  - /c
  - -f
  CommandLine|contains:
  - '{0}'
  - '{1}'
  - '{2}'
  - '{3}'
  - '{4}'
  - '{5}'
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/SigmaHQ/sigma/issues/1009

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_invoke_obfuscation_via_var.yml)
