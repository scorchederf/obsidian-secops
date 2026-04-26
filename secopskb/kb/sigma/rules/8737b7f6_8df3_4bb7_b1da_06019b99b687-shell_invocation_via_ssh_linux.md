---
sigma_id: "8737b7f6-8df3-4bb7-b1da-06019b99b687"
title: "Shell Invocation Via Ssh - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_ssh_shell_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_ssh_shell_execution.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "linux / process_creation"
aliases:
  - "8737b7f6-8df3-4bb7-b1da-06019b99b687"
  - "Shell Invocation Via Ssh - Linux"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Shell Invocation Via Ssh - Linux

Detects the use of the "ssh" utility to execute a shell. Such behavior may be associated with privilege escalation, unauthorized command execution, or to break out from restricted environments.

## Metadata

- Rule ID: 8737b7f6-8df3-4bb7-b1da-06019b99b687
- Status: test
- Level: high
- Author: Li Ling, Andy Parkidomo, Robert Rakowski, Blake Hartstein (Bloomberg L.P.)
- Date: 2024-08-29
- Source Path: rules/linux/process_creation/proc_creation_lnx_ssh_shell_execution.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection_img:
  Image|endswith: /ssh
  CommandLine|contains:
  - ProxyCommand=;
  - permitlocalcommand=yes
  - localhost
selection_cli:
  CommandLine|contains:
  - /bin/bash
  - /bin/dash
  - /bin/fish
  - /bin/sh
  - /bin/zsh
  - sh 0<&2 1>&2
  - sh 1>&2 0<&2
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://gtfobins.github.io/gtfobins/ssh/
- https://www.elastic.co/guide/en/security/current/linux-restricted-shell-breakout-via-linux-binary-s.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_ssh_shell_execution.yml)
