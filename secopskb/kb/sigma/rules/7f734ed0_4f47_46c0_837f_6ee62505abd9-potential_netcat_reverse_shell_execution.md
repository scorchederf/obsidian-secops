---
sigma_id: "7f734ed0-4f47-46c0-837f-6ee62505abd9"
title: "Potential Netcat Reverse Shell Execution"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_netcat_reverse_shell.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_netcat_reverse_shell.yml"
build_date: "2026-04-27 19:13:54"
status: "test"
level: "high"
logsource: "linux / process_creation"
aliases:
  - "7f734ed0-4f47-46c0-837f-6ee62505abd9"
  - "Potential Netcat Reverse Shell Execution"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects execution of netcat with the "-e" flag followed by common shells. This could be a sign of a potential reverse shell setup.

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]

## Detection

```yaml
selection_nc:
  Image|endswith:
  - /nc
  - /ncat
selection_flags:
  CommandLine|contains:
  - ' -c '
  - ' -e '
selection_shell:
  CommandLine|contains:
  - ' ash'
  - ' bash'
  - ' bsh'
  - ' csh'
  - ' ksh'
  - ' pdksh'
  - ' sh'
  - ' tcsh'
  - /bin/ash
  - /bin/bash
  - /bin/bsh
  - /bin/csh
  - /bin/ksh
  - /bin/pdksh
  - /bin/sh
  - /bin/tcsh
  - /bin/zsh
  - $IFSash
  - $IFSbash
  - $IFSbsh
  - $IFScsh
  - $IFSksh
  - $IFSpdksh
  - $IFSsh
  - $IFStcsh
  - $IFSzsh
condition: all of selection_*
```

## False Positives

- Unlikely

## References

- https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet
- https://www.revshells.com/
- https://www.hackingtutorials.org/networking/hacking-netcat-part-2-bind-reverse-shells/
- https://www.infosecademy.com/netcat-reverse-shells/
- https://man7.org/linux/man-pages/man1/ncat.1.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_netcat_reverse_shell.yml)
