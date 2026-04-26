---
sigma_id: "c4042d54-110d-45dd-a0e1-05c47822c937"
title: "Python Spawning Pretty TTY Via PTY Module"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_python_pty_spawn.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_python_pty_spawn.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "c4042d54-110d-45dd-a0e1-05c47822c937"
  - "Python Spawning Pretty TTY Via PTY Module"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Python Spawning Pretty TTY Via PTY Module

Detects a python process calling to the PTY module in order to spawn a pretty tty which could be indicative of potential reverse shell activity.

## Metadata

- Rule ID: c4042d54-110d-45dd-a0e1-05c47822c937
- Status: test
- Level: medium
- Author: Nextron Systems
- Date: 2022-06-03
- Modified: 2024-11-04
- Source Path: rules/linux/process_creation/proc_creation_lnx_python_pty_spawn.yml

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
selection_cli_import:
  CommandLine|contains:
  - import pty
  - 'from pty '
selection_cli_spawn:
  CommandLine|contains: spawn
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://www.volexity.com/blog/2022/06/02/zero-day-exploitation-of-atlassian-confluence/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_python_pty_spawn.yml)
