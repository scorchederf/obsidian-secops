---
sigma_id: "c6714a24-d7d5-4283-a36b-3ffd091d5f7e"
title: "Potential PHP Reverse Shell"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_php_reverse_shell.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_php_reverse_shell.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "linux / process_creation"
aliases:
  - "c6714a24-d7d5-4283-a36b-3ffd091d5f7e"
  - "Potential PHP Reverse Shell"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Potential PHP Reverse Shell

Detects usage of the PHP CLI with the "-r" flag which allows it to run inline PHP code. The rule looks for calls to the "fsockopen" function which allows the creation of sockets.
Attackers often leverage this in combination with functions such as "exec" or "fopen" to initiate a reverse shell connection.

## Metadata

- Rule ID: c6714a24-d7d5-4283-a36b-3ffd091d5f7e
- Status: test
- Level: high
- Author: @d4ns4n_
- Date: 2023-04-07
- Source Path: rules/linux/process_creation/proc_creation_lnx_php_reverse_shell.yml

## Logsource

- category: process_creation
- product: linux

## Detection

```yaml
selection:
  Image|contains: /php
  CommandLine|contains|all:
  - ' -r '
  - fsockopen
  CommandLine|contains:
  - ash
  - bash
  - bsh
  - csh
  - ksh
  - pdksh
  - sh
  - tcsh
  - zsh
condition: selection
```

## False Positives

- Unknown

## References

- https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet
- https://www.revshells.com/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_php_reverse_shell.yml)
