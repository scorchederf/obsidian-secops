---
sigma_id: "9b5de532-a757-4d70-946c-1f3e44f48b4d"
title: "Shell Execution GCC  - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_gcc_shell_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_gcc_shell_execution.yml"
build_date: "2026-04-26 15:01:51"
status: "test"
level: "high"
logsource: "linux / process_creation"
aliases:
  - "9b5de532-a757-4d70-946c-1f3e44f48b4d"
  - "Shell Execution GCC  - Linux"
attack_technique_ids:
  - "T1083"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Shell Execution GCC  - Linux

Detects the use of the "gcc" utility to execute a shell. Such behavior may be associated with privilege escalation, unauthorized command execution, or to break out from restricted environments.

## Metadata

- Rule ID: 9b5de532-a757-4d70-946c-1f3e44f48b4d
- Status: test
- Level: high
- Author: Li Ling, Andy Parkidomo, Robert Rakowski, Blake Hartstein (Bloomberg L.P.)
- Date: 2024-09-02
- Source Path: rules/linux/process_creation/proc_creation_lnx_gcc_shell_execution.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1083-file_and_directory_discovery|T1083]]

## Detection

```yaml
selection_img:
  Image|endswith:
  - /c89
  - /c99
  - /gcc
  CommandLine|contains: -wrapper
selection_cli:
  CommandLine|contains:
  - /bin/bash,-s
  - /bin/dash,-s
  - /bin/fish,-s
  - /bin/sh,-s
  - /bin/zsh,-s
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://gtfobins.github.io/gtfobins/gcc/#shell
- https://gtfobins.github.io/gtfobins/c89/#shell
- https://gtfobins.github.io/gtfobins/c99/#shell
- https://www.elastic.co/guide/en/security/current/linux-restricted-shell-breakout-via-linux-binary-s.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_gcc_shell_execution.yml)
