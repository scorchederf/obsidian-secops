---
sigma_id: "259df6bc-003f-4306-9f54-4ff1a08fa38e"
title: "Potential Perl Reverse Shell Execution"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_perl_reverse_shell.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_perl_reverse_shell.yml"
build_date: "2026-04-27 19:13:54"
status: "test"
level: "high"
logsource: "linux / process_creation"
aliases:
  - "259df6bc-003f-4306-9f54-4ff1a08fa38e"
  - "Potential Perl Reverse Shell Execution"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects execution of the perl binary with the "-e" flag and common strings related to potential reverse shell activity

## Logsource

- category: process_creation
- product: linux

## Detection

```yaml
selection_img:
  Image|endswith: /perl
  CommandLine|contains: ' -e '
selection_content:
- CommandLine|contains|all:
  - fdopen(
  - ::Socket::INET
- CommandLine|contains|all:
  - Socket
  - connect
  - open
  - exec
condition: all of selection_*
```

## False Positives

- Unlikely

## References

- https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet
- https://www.revshells.com/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_perl_reverse_shell.yml)
