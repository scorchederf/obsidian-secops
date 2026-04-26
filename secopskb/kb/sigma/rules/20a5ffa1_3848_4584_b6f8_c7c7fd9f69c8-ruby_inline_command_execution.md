---
sigma_id: "20a5ffa1-3848-4584-b6f8-c7c7fd9f69c8"
title: "Ruby Inline Command Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_ruby_inline_command_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_ruby_inline_command_execution.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "20a5ffa1-3848-4584-b6f8-c7c7fd9f69c8"
  - "Ruby Inline Command Execution"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Ruby Inline Command Execution

Detects execution of ruby using the "-e" flag. This is could be used as a way to launch a reverse shell or execute live ruby code.

## Metadata

- Rule ID: 20a5ffa1-3848-4584-b6f8-c7c7fd9f69c8
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-01-02
- Source Path: rules/windows/process_creation/proc_creation_win_ruby_inline_command_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection_img:
- Image|endswith: \ruby.exe
- OriginalFileName: ruby.exe
selection_cli:
  CommandLine|contains: ' -e'
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet
- https://www.revshells.com/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_ruby_inline_command_execution.yml)
