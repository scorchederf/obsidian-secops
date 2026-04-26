---
sigma_id: "2d2f44ff-4611-4778-a8fc-323a0e9850cc"
title: "Inline Python Execution - Spawn Shell Via OS System Library"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_python_shell_os_system.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_python_shell_os_system.yml"
build_date: "2026-04-26 15:01:45"
status: "test"
level: "high"
logsource: "linux / process_creation"
aliases:
  - "2d2f44ff-4611-4778-a8fc-323a0e9850cc"
  - "Inline Python Execution - Spawn Shell Via OS System Library"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Inline Python Execution - Spawn Shell Via OS System Library

Detects execution of inline Python code via the "-c" in order to call the "system" function from the "os" library, and spawn a shell.

## Metadata

- Rule ID: 2d2f44ff-4611-4778-a8fc-323a0e9850cc
- Status: test
- Level: high
- Author: Li Ling, Andy Parkidomo, Robert Rakowski, Blake Hartstein (Bloomberg L.P.)
- Date: 2024-09-02
- Source Path: rules/linux/process_creation/proc_creation_lnx_python_shell_os_system.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - /python
  - /python2
  - /python3
- Image|contains:
  - /python2.
  - /python3.
selection_cli:
  CommandLine|contains|all:
  - ' -c '
  - os.system(
  CommandLine|contains:
  - /bin/bash
  - /bin/dash
  - /bin/fish
  - /bin/sh
  - /bin/zsh
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://gtfobins.github.io/gtfobins/python/#shell

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_python_shell_os_system.yml)
