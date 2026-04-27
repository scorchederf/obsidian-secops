---
sigma_id: "7ab8f73a-fcff-428b-84aa-6a5ff7877dea"
title: "Vim GTFOBin Abuse - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_vim_shell_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_vim_shell_execution.yml"
build_date: "2026-04-27 19:13:58"
status: "test"
level: "high"
logsource: "linux / process_creation"
aliases:
  - "7ab8f73a-fcff-428b-84aa-6a5ff7877dea"
  - "Vim GTFOBin Abuse - Linux"
attack_technique_ids:
  - "T1083"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the use of "vim" and it's siblings commands to execute a shell or proxy commands.
Such behavior may be associated with privilege escalation, unauthorized command execution, or to break out from restricted environments.

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1083-file_and_directory_discovery|T1083: File and Directory Discovery]]

## Detection

```yaml
selection_img:
  Image|endswith:
  - /rvim
  - /vim
  - /vimdiff
  CommandLine|contains:
  - ' --cmd'
  - ' -c '
selection_cli:
  CommandLine|contains:
  - :!/
  - ':lua '
  - ':py '
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

- https://gtfobins.github.io/gtfobins/vim/
- https://gtfobins.github.io/gtfobins/rvim/
- https://gtfobins.github.io/gtfobins/vimdiff/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_vim_shell_execution.yml)
