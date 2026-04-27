---
atomic_guid: "386d3850-2ce7-4508-b56b-c0558922c814"
title: "Setting the HISTSIZE environment variable"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.003"
attack_technique_name: "Impair Defenses: Impair Command History Logging"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.003/T1562.003.yaml"
build_date: "2026-04-27 19:12:28"
executor: "sh"
aliases:
  - "386d3850-2ce7-4508-b56b-c0558922c814"
  - "Setting the HISTSIZE environment variable"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

An Adversary may set the sh history files size environment variable (HISTSIZE) to zero to prevent the logging of commands to the history file after they log out of the system.

Note: we don't wish to log out, so we are just confirming the value of HISTSIZE. In this test we 1. echo HISTSIZE 2. set it to zero 3. confirm that HISTSIZE is set to zero.

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses#^t1562003-impair-command-history-logging|T1562.003: Impair Command History Logging]]

## Executor

- elevation_required: False
- name: sh

### Command

```bash
echo $HISTSIZE
export HISTSIZE=0
echo "runnning some commands to populate the history"
whoami
groups
if [ $(echo $HISTSIZE) -eq 0 ]; then echo "\$HISTSIZE is zero"; else HIST_LENGTH=$(wc -l $HISTFILE); echo "\$HISTSIZE is not zero, history size is $HIST_LENGTH";  fi
```

### Cleanup

```bash
export HISTSIZE=100
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.003/T1562.003.yaml)
