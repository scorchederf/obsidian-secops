---
sigma_id: "093d68c7-762a-42f4-9f46-95e79142571a"
title: "Shell Execution via Nice - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_nice_shell_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_nice_shell_execution.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "linux / process_creation"
aliases:
  - "093d68c7-762a-42f4-9f46-95e79142571a"
  - "Shell Execution via Nice - Linux"
attack_technique_ids:
  - "T1083"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Shell Execution via Nice - Linux

Detects the use of the "nice" utility to execute a shell. Such behavior may be associated with privilege escalation, unauthorized command execution, or to break out from restricted environments.

## Metadata

- Rule ID: 093d68c7-762a-42f4-9f46-95e79142571a
- Status: test
- Level: high
- Author: Li Ling, Andy Parkidomo, Robert Rakowski, Blake Hartstein (Bloomberg L.P.)
- Date: 2024-09-02
- Source Path: rules/linux/process_creation/proc_creation_lnx_nice_shell_execution.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1083-file_and_directory_discovery|T1083]]

## Detection

```yaml
selection:
  Image|endswith: /nice
  CommandLine|endswith:
  - /bin/bash
  - /bin/dash
  - /bin/fish
  - /bin/sh
  - /bin/zsh
condition: selection
```

## False Positives

- Unknown

## References

- https://gtfobins.github.io/gtfobins/nice/#shell
- https://www.elastic.co/guide/en/security/current/linux-restricted-shell-breakout-via-linux-binary-s.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_nice_shell_execution.yml)
