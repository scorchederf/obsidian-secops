---
sigma_id: "5edc2273-c26f-406c-83f3-f4d948e740dd"
title: "Indirect Inline Command Execution Via Bash.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_bash_command_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_bash_command_execution.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "5edc2273-c26f-406c-83f3-f4d948e740dd"
  - "Indirect Inline Command Execution Via Bash.EXE"
attack_technique_ids:
  - "T1202"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Indirect Inline Command Execution Via Bash.EXE

Detects execution of Microsoft bash launcher with the "-c" flag.
This can be used to potentially bypass defenses and execute Linux or Windows-based binaries directly via bash.

## Metadata

- Rule ID: 5edc2273-c26f-406c-83f3-f4d948e740dd
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-11-24
- Modified: 2023-08-15
- Source Path: rules/windows/process_creation/proc_creation_win_bash_command_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - :\Windows\System32\bash.exe
  - :\Windows\SysWOW64\bash.exe
- OriginalFileName: Bash.exe
selection_cli:
  CommandLine|contains: ' -c '
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Binaries/Bash/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_bash_command_execution.yml)
