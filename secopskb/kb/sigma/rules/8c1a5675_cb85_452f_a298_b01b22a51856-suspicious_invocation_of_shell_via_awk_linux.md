---
sigma_id: "8c1a5675-cb85-452f-a298-b01b22a51856"
title: "Suspicious Invocation of Shell via AWK - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_awk_shell_spawn.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_awk_shell_spawn.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "linux / process_creation"
aliases:
  - "8c1a5675-cb85-452f-a298-b01b22a51856"
  - "Suspicious Invocation of Shell via AWK - Linux"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Invocation of Shell via AWK - Linux

Detects the execution of "awk" or it's sibling commands, to invoke a shell using the system() function.
This behavior is commonly associated with attempts to execute arbitrary commands or escalate privileges, potentially leading to unauthorized access or further exploitation.

## Metadata

- Rule ID: 8c1a5675-cb85-452f-a298-b01b22a51856
- Status: test
- Level: high
- Author: Li Ling, Andy Parkidomo, Robert Rakowski, Blake Hartstein (Bloomberg L.P.)
- Date: 2024-09-02
- Source Path: rules/linux/process_creation/proc_creation_lnx_awk_shell_spawn.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection_img:
  Image|endswith:
  - /awk
  - /gawk
  - /mawk
  - /nawk
  CommandLine|contains: BEGIN {system
selection_cli:
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

- https://gtfobins.github.io/gtfobins/awk/#shell
- https://gtfobins.github.io/gtfobins/gawk/#shell
- https://gtfobins.github.io/gtfobins/nawk/#shell
- https://gtfobins.github.io/gtfobins/mawk/#shell

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_awk_shell_spawn.yml)
