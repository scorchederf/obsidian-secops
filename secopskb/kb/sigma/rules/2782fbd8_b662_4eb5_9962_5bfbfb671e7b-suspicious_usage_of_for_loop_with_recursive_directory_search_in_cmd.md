---
sigma_id: "2782fbd8-b662-4eb5-9962-5bfbfb671e7b"
title: "Suspicious Usage of For Loop with Recursive Directory Search in CMD"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_cmd_for_loop_execution_with_recursive_directory_search.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_cmd_for_loop_execution_with_recursive_directory_search.yml"
build_date: "2026-04-26 14:14:37"
status: "experimental"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "2782fbd8-b662-4eb5-9962-5bfbfb671e7b"
  - "Suspicious Usage of For Loop with Recursive Directory Search in CMD"
attack_technique_ids:
  - "T1059.003"
  - "T1027.010"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Usage of For Loop with Recursive Directory Search in CMD

Detects suspicious usage of the cmd.exe 'for /f' loop combined with the 'tokens=' parameter and a recursive directory listing.
This pattern may indicate an attempt to discover and execute system binaries dynamically, for example powershell, a technique sometimes used by attackers to evade detection.
This behavior has been observed in various malicious lnk files.

## Metadata

- Rule ID: 2782fbd8-b662-4eb5-9962-5bfbfb671e7b
- Status: experimental
- Level: medium
- Author: Joseliyo Sanchez, @Joseliyo_Jstnk
- Date: 2025-11-12
- Source Path: rules/windows/process_creation/proc_creation_win_susp_cmd_for_loop_execution_with_recursive_directory_search.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.003]]
- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027.010]]

## Detection

```yaml
selection_tokens:
  CommandLine|contains|all:
  - for /f
  - tokens=
  - in (
  - dir
selection_tokens_parent:
  ParentCommandLine|contains|all:
  - for /f
  - tokens=
  - in (
  - dir
condition: 1 of selection_*
```

## False Positives

- Unknown

## References

- https://www.virustotal.com/gui/file/29837d0d3202758063185828c8f8d9e0b7b42b365c8941cc926d2d7c7bae2fb3

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_cmd_for_loop_execution_with_recursive_directory_search.yml)
