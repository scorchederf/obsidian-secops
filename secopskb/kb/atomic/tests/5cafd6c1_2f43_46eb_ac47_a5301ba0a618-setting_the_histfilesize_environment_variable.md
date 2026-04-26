---
atomic_guid: "5cafd6c1-2f43-46eb-ac47-a5301ba0a618"
title: "Setting the HISTFILESIZE environment variable"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.003"
attack_technique_name: "Impair Defenses: Impair Command History Logging"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.003/T1562.003.yaml"
build_date: "2026-04-26 14:38:40"
executor: "bash"
aliases:
  - "5cafd6c1-2f43-46eb-ac47-a5301ba0a618"
  - "Setting the HISTFILESIZE environment variable"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Setting the HISTFILESIZE environment variable

An Adversary may set the bash history files size environment variable (HISTFILESIZE) to zero to prevent the logging of commands to the history file after they log out of the system.

Note: we don't wish to log out, so we are just confirming the value of HISTFILESIZE. In this test we 1. echo HISTFILESIZE 2. set it to zero 3. confirm that HISTFILESIZE is set to zero.

## Metadata

- Atomic GUID: 5cafd6c1-2f43-46eb-ac47-a5301ba0a618
- Technique: T1562.003: Impair Defenses: Impair Command History Logging
- Platforms: linux
- Executor: bash
- Elevation Required: False
- Source Path: atomics/T1562.003/T1562.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.003]]

## Executor

- elevation_required: False
- name: bash

### Command

```bash
TEST=$(echo $HISTFILESIZE)
echo $HISTFILESIZE
export HISTFILESIZE=0
echo "runnning some commands to populate the history"
whoami
groups
if [ $(echo $HISTFILESIZE) -eq 0 ]; then echo "\$HISTFILESIZE is zero"; else HIST_LENGHT=$(wc -l $HISTFILE); echo "\$HISTFILESIZE is not zero, history lenght is $HIST_LENGHT";  fi
```

### Cleanup

```bash
export HISTCONTROL=$(echo $TEST)
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.003/T1562.003.yaml)
