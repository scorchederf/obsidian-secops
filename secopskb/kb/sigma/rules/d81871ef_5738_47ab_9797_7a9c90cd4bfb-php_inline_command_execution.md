---
sigma_id: "d81871ef-5738-47ab-9797-7a9c90cd4bfb"
title: "Php Inline Command Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_php_inline_command_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_php_inline_command_execution.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "d81871ef-5738-47ab-9797-7a9c90cd4bfb"
  - "Php Inline Command Execution"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Php Inline Command Execution

Detects execution of php using the "-r" flag. This is could be used as a way to launch a reverse shell or execute live php code.

## Metadata

- Rule ID: d81871ef-5738-47ab-9797-7a9c90cd4bfb
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-01-02
- Source Path: rules/windows/process_creation/proc_creation_win_php_inline_command_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection_img:
- Image|endswith: \php.exe
- OriginalFileName: php.exe
selection_cli:
  CommandLine|contains: ' -r'
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://www.php.net/manual/en/features.commandline.php
- https://www.revshells.com/
- https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_php_inline_command_execution.yml)
