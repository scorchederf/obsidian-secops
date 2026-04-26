---
sigma_id: "47b3bbd4-1bf7-48cc-84ab-995362aaa75a"
title: "Shell Execution via Git - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_git_shell_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_git_shell_execution.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "linux / process_creation"
aliases:
  - "47b3bbd4-1bf7-48cc-84ab-995362aaa75a"
  - "Shell Execution via Git - Linux"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Shell Execution via Git - Linux

Detects the use of the "git" utility to execute a shell. Such behavior may be associated with privilege escalation, unauthorized command execution, or to break out from restricted environments.

## Metadata

- Rule ID: 47b3bbd4-1bf7-48cc-84ab-995362aaa75a
- Status: test
- Level: high
- Author: Li Ling, Andy Parkidomo, Robert Rakowski, Blake Hartstein (Bloomberg L.P.)
- Date: 2024-09-02
- Source Path: rules/linux/process_creation/proc_creation_lnx_git_shell_execution.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection:
  ParentImage|endswith: /git
  ParentCommandLine|contains|all:
  - ' -p '
  - help
  CommandLine|contains:
  - bash 0<&1
  - dash 0<&1
  - sh 0<&1
condition: selection
```

## False Positives

- Unknown

## References

- https://gtfobins.github.io/gtfobins/git/#shell

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_git_shell_execution.yml)
