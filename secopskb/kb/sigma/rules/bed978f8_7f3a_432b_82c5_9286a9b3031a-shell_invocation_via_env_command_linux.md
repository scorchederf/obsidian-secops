---
sigma_id: "bed978f8-7f3a-432b-82c5-9286a9b3031a"
title: "Shell Invocation via Env Command - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_env_shell_invocation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_env_shell_invocation.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "linux / process_creation"
aliases:
  - "bed978f8-7f3a-432b-82c5-9286a9b3031a"
  - "Shell Invocation via Env Command - Linux"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Shell Invocation via Env Command - Linux

Detects the use of the env command to invoke a shell. This may indicate an attempt to bypass restricted environments, escalate privileges, or execute arbitrary commands.

## Metadata

- Rule ID: bed978f8-7f3a-432b-82c5-9286a9b3031a
- Status: test
- Level: high
- Author: Li Ling, Andy Parkidomo, Robert Rakowski, Blake Hartstein (Bloomberg L.P.)
- Date: 2024-09-02
- Source Path: rules/linux/process_creation/proc_creation_lnx_env_shell_invocation.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection:
  Image|endswith: /env
  CommandLine|endswith:
  - /bin/bash
  - /bin/dash
  - /bin/fish
  - /bin/sh
  - /bin/zsh
condition: selection
```

## False Positives

- Github operations such as ghe-backup

## References

- https://gtfobins.github.io/gtfobins/env/#shell
- https://www.elastic.co/guide/en/security/current/linux-restricted-shell-breakout-via-linux-binary-s.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_env_shell_invocation.yml)
