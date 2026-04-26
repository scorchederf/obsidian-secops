---
sigma_id: "b8bdac18-c06e-4016-ac30-221553e74f59"
title: "Potential Ruby Reverse Shell"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_ruby_reverse_shell.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_ruby_reverse_shell.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "b8bdac18-c06e-4016-ac30-221553e74f59"
  - "Potential Ruby Reverse Shell"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Ruby Reverse Shell

Detects execution of ruby with the "-e" flag and calls to "socket" related functions. This could be an indication of a potential attempt to setup a reverse shell

## Metadata

- Rule ID: b8bdac18-c06e-4016-ac30-221553e74f59
- Status: test
- Level: medium
- Author: @d4ns4n_
- Date: 2023-04-07
- Source Path: rules/linux/process_creation/proc_creation_lnx_ruby_reverse_shell.yml

## Logsource

- category: process_creation
- product: linux

## Detection

```yaml
selection:
  Image|contains: ruby
  CommandLine|contains|all:
  - ' -e'
  - rsocket
  - TCPSocket
  CommandLine|contains:
  - ' ash'
  - ' bash'
  - ' bsh'
  - ' csh'
  - ' ksh'
  - ' pdksh'
  - ' sh'
  - ' tcsh'
condition: selection
```

## False Positives

- Unknown

## References

- https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet
- https://www.revshells.com/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_ruby_reverse_shell.yml)
