---
sigma_id: "e2326866-609f-4015-aea9-7ec634e8aa04"
title: "Shell Execution via Rsync - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_rsync_shell_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_rsync_shell_execution.yml"
build_date: "2026-04-27 19:13:56"
status: "experimental"
level: "high"
logsource: "linux / process_creation"
aliases:
  - "e2326866-609f-4015-aea9-7ec634e8aa04"
  - "Shell Execution via Rsync - Linux"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the use of the "rsync" utility to execute a shell. Such behavior may be associated with privilege escalation, unauthorized command execution, or to break out from restricted environments.

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]

## Detection

```yaml
selection_img:
  Image|endswith:
  - /rsync
  - /rsyncd
  CommandLine|contains: ' -e '
selection_cli:
  CommandLine|contains:
  - '/ash '
  - '/bash '
  - '/dash '
  - '/csh '
  - '/sh '
  - '/zsh '
  - '/tcsh '
  - '/ksh '
  - '''ash '
  - '''bash '
  - '''dash '
  - '''csh '
  - '''sh '
  - '''zsh '
  - '''tcsh '
  - '''ksh '
condition: all of selection_*
```

## False Positives

- Legitimate cases in which "rsync" is used to execute a shell

## References

- https://gtfobins.github.io/gtfobins/rsync/#shell

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_rsync_shell_execution.yml)
