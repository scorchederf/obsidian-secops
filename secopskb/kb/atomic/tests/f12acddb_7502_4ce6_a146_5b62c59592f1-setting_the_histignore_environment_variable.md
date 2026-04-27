---
atomic_guid: "f12acddb-7502-4ce6-a146-5b62c59592f1"
title: "Setting the HISTIGNORE environment variable"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.003"
attack_technique_name: "Impair Defenses: Impair Command History Logging"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.003/T1562.003.yaml"
build_date: "2026-04-27 19:12:28"
executor: "bash"
aliases:
  - "f12acddb-7502-4ce6-a146-5b62c59592f1"
  - "Setting the HISTIGNORE environment variable"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

An Adversary may take advantage of the HISTIGNORE environment variable either to ignore particular commands or all commands. 

In this test we 1. set HISTIGNORE to ignore ls, rm and ssh commands 2. clear this history cache 3..4 execute ls commands 5. confirm that the ls commands are not in the history cache 6. unset HISTIGNORE variable 7.. same again, but ignoring ALL commands.

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses#^t1562003-impair-command-history-logging|T1562.003: Impair Command History Logging]]

## Executor

- elevation_required: False
- name: bash

### Command

```bash
if ((${#HISTIGNORE[@]})); then echo "\$HISTIGNORE = $HISTIGNORE"; else export HISTIGNORE='ls*:rm*:ssh*'; echo "\$HISTIGNORE = $HISTIGNORE"; fi
history -c 
ls -la $HISTFILE
ls -la ~/.bash_logout
if [ $(history |wc -l) -eq 1 ]; then echo "ls commands are not in history"; fi
unset HISTIGNORE
if ((${#HISTIGNORE[@]})); then echo "\$HISTIGNORE = $HISTIGNORE"; else export HISTIGNORE='*'; echo "\$HISTIGNORE = $HISTIGNORE"; fi
history -c 
whoami
groups
if [ $(history |wc -l) -eq 0 ]; then echo "History cache is empty"; fi
```

### Cleanup

```bash
unset HISTIGNORE
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.003/T1562.003.yaml)
