---
sigma_id: "899133d5-4d7c-4a7f-94ee-27355c879d90"
title: "Python Inline Command Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_python_inline_command_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_python_inline_command_execution.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "899133d5-4d7c-4a7f-94ee-27355c879d90"
  - "Python Inline Command Execution"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Python Inline Command Execution

Detects execution of python using the "-c" flag. This is could be used as a way to launch a reverse shell or execute live python code.

## Metadata

- Rule ID: 899133d5-4d7c-4a7f-94ee-27355c879d90
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-01-02
- Modified: 2025-10-07
- Source Path: rules/windows/process_creation/proc_creation_win_python_inline_command_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection_img:
- OriginalFileName: python.exe
- Image|endswith:
  - python.exe
  - python3.exe
  - python2.exe
selection_cli:
  CommandLine|contains: ' -c'
filter_main_python_1:
  ParentImage|startswith:
  - C:\Program Files\Python
  - C:\Program Files (x86)\Python
  ParentImage|endswith: \python.exe
  ParentCommandLine|contains: -E -s -m ensurepip -U --default-pip
filter_main_python_trace:
  ParentImage|startswith:
  - C:\Program Files\Python
  - C:\Program Files (x86)\Python
  CommandLine|contains|all:
  - -W ignore::DeprecationWarning
  - '[''install'', ''--no-cache-dir'', ''--no-index'', ''--find-links'','
  - '''--upgrade'', ''pip'''
filter_optional_vscode:
- ParentImage|endswith: \AppData\Local\Programs\Microsoft VS Code\Code.exe
- ParentImage:
  - C:\Program Files\Microsoft VS Code\Code.exe
  - C:\Program Files (x86)\Microsoft VS Code\Code.exe
filter_optional_pip:
  CommandLine|contains|all:
  - <pip-setuptools-caller>
  - exec(compile(
condition: all of selection_* and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Python libraries that use a flag starting with "-c". Filter according to your environment

## References

- https://docs.python.org/3/using/cmdline.html#cmdoption-c
- https://www.revshells.com/
- https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_python_inline_command_execution.yml)
