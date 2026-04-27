---
sigma_id: "fdc88d25-96fb-4b7c-9633-c0e417fdbd4e"
title: "Linux Command History Tampering"
framework: "sigma"
generated: "true"
source_path: "rules/linux/builtin/lnx_shell_clear_cmd_history.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/lnx_shell_clear_cmd_history.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "linux"
aliases:
  - "fdc88d25-96fb-4b7c-9633-c0e417fdbd4e"
  - "Linux Command History Tampering"
attack_technique_ids:
  - "T1070.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Linux Command History Tampering

Detects commands that try to clear or tamper with the Linux command history.
This technique is used by threat actors in order to evade defenses and execute commands without them being recorded in files such as "bash_history" or "zsh_history".

## Metadata

- Rule ID: fdc88d25-96fb-4b7c-9633-c0e417fdbd4e
- Status: test
- Level: high
- Author: Patrick Bareiss
- Date: 2019-03-24
- Modified: 2024-04-17
- Source Path: rules/linux/builtin/lnx_shell_clear_cmd_history.yml

## Logsource

- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070.003]]

## Detection

```yaml
keywords:
- cat /dev/null >*sh_history
- cat /dev/zero >*sh_history
- chattr +i*sh_history
- echo "" >*sh_history
- empty_bash_history
- export HISTFILESIZE=0
- history -c
- history -w
- ln -sf /dev/null *sh_history
- ln -sf /dev/zero *sh_history
- rm *sh_history
- shopt -ou history
- shopt -uo history
- shred *sh_history
- truncate -s0 *sh_history
condition: keywords
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1070.003/T1070.003.md
- https://www.hackers-arise.com/post/2016/06/20/covering-your-bash-shell-tracks-antiforensics
- https://www.cadosecurity.com/spinning-yarn-a-new-linux-malware-campaign-targets-docker-apache-hadoop-redis-and-confluence/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/lnx_shell_clear_cmd_history.yml)
