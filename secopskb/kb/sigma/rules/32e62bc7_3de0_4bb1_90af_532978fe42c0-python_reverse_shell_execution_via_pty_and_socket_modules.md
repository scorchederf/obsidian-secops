---
sigma_id: "32e62bc7-3de0-4bb1-90af-532978fe42c0"
title: "Python Reverse Shell Execution Via PTY And Socket Modules"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_python_reverse_shell.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_python_reverse_shell.yml"
build_date: "2026-04-26 15:01:50"
status: "test"
level: "high"
logsource: "linux / process_creation"
aliases:
  - "32e62bc7-3de0-4bb1-90af-532978fe42c0"
  - "Python Reverse Shell Execution Via PTY And Socket Modules"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Python Reverse Shell Execution Via PTY And Socket Modules

Detects the execution of python with calls to the socket and pty module in order to connect and spawn a potential reverse shell.

## Metadata

- Rule ID: 32e62bc7-3de0-4bb1-90af-532978fe42c0
- Status: test
- Level: high
- Author: @d4ns4n_, Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-04-24
- Modified: 2024-11-04
- Source Path: rules/linux/process_creation/proc_creation_lnx_python_reverse_shell.yml

## Logsource

- category: process_creation
- product: linux

## Detection

```yaml
selection:
  Image|contains: python
  CommandLine|contains|all:
  - ' -c '
  - import
  - pty
  - socket
  - spawn
  - .connect
condition: selection
```

## False Positives

- Unknown

## References

- https://www.revshells.com/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_python_reverse_shell.yml)
