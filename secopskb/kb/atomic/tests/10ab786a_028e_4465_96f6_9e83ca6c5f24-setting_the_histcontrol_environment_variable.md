---
atomic_guid: "10ab786a-028e-4465-96f6-9e83ca6c5f24"
title: "Setting the HISTCONTROL environment variable"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.003"
attack_technique_name: "Impair Defenses: Impair Command History Logging"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.003/T1562.003.yaml"
build_date: "2026-04-27 19:12:28"
executor: "bash"
aliases:
  - "10ab786a-028e-4465-96f6-9e83ca6c5f24"
  - "Setting the HISTCONTROL environment variable"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

An attacker may exploit the space before a command (e.g. " ls") or the duplicate command suppression feature in Bash history to prevent their commands from being recorded in the history file or to obscure the order of commands used. 

In this test we 1. sets $HISTCONTROL to ignoreboth 2. clears the history cache 3. executes ls -la with a space in-front of it 4. confirms that ls -la is not in the history cache 5. sets $HISTCONTROL to erasedups 6. clears the history cache 7..9 executes ls -la $HISTFILE 3 times 10. confirms that their is only one command in history

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses#^t1562003-impair-command-history-logging|T1562.003: Impair Command History Logging]]

## Executor

- elevation_required: False
- name: bash

### Command

```bash
TEST=$(echo $HISTCONTROL)
if [ "$HISTCONTROL" != "ignoreboth" ]; then export HISTCONTROL="ignoreboth"; fi
history -c 
ls -la $HISTFILE # " ls -la $HISTFILE"
if [ $(history |wc -l) -eq 1 ]; then echo "ls -la is not in history cache"; fi
if [ "$HISTCONTROL" != "erasedups" ]; then export HISTCONTROL="erasedups"; fi
history -c 
ls -la $HISTFILE
ls -la $HISTFILE
ls -la $HISTFILE
if [ $(history |wc -l) -eq 2 ]; then echo "Their is only one entry for ls -la $HISTFILE"; fi
```

### Cleanup

```bash
export HISTCONTROL=$(echo $TEST)
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.003/T1562.003.yaml)
