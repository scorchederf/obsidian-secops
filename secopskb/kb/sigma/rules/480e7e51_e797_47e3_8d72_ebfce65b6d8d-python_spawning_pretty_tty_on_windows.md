---
sigma_id: "480e7e51-e797-47e3-8d72-ebfce65b6d8d"
title: "Python Spawning Pretty TTY on Windows"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_python_pty_spawn.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_python_pty_spawn.yml"
build_date: "2026-04-27 19:13:55"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "480e7e51-e797-47e3-8d72-ebfce65b6d8d"
  - "Python Spawning Pretty TTY on Windows"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects python spawning a pretty tty

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]

## Detection

```yaml
selection_img:
  Image|endswith:
  - python.exe
  - python3.exe
  - python2.exe
selection_cli_1:
  CommandLine|contains|all:
  - import pty
  - .spawn(
selection_cli_2:
  CommandLine|contains: from pty import spawn
condition: selection_img and 1 of selection_cli_*
```

## False Positives

- Unknown

## References

- https://www.volexity.com/blog/2022/06/02/zero-day-exploitation-of-atlassian-confluence/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_python_pty_spawn.yml)
