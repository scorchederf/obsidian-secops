---
sigma_id: "2d22a514-e024-4428-9dba-41505bd63a5b"
title: "Indirect Command Execution From Script File Via Bash.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_bash_file_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_bash_file_execution.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "2d22a514-e024-4428-9dba-41505bd63a5b"
  - "Indirect Command Execution From Script File Via Bash.EXE"
attack_technique_ids:
  - "T1202"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Indirect Command Execution From Script File Via Bash.EXE

Detects execution of Microsoft bash launcher without any flags to execute the content of a bash script directly.
This can be used to potentially bypass defenses and execute Linux or Windows-based binaries directly via bash.

## Metadata

- Rule ID: 2d22a514-e024-4428-9dba-41505bd63a5b
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-08-15
- Source Path: rules/windows/process_creation/proc_creation_win_bash_file_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Detection

```yaml
selection:
- Image|endswith:
  - :\Windows\System32\bash.exe
  - :\Windows\SysWOW64\bash.exe
- OriginalFileName: Bash.exe
filter_main_cli_flag:
  CommandLine|contains:
  - bash.exe -
  - bash -
filter_main_no_cli:
  CommandLine: null
filter_main_empty:
  CommandLine: ''
filter_main_no_flag:
  CommandLine:
  - bash.exe
  - bash
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Binaries/Bash/
- https://linux.die.net/man/1/bash
- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_bash_file_execution.yml)
