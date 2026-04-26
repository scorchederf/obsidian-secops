---
atomic_guid: "b3dacb6c-a9e3-44ec-bf87-38db60c5cad1"
title: "Setting the HISTFILE environment variable"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.003"
attack_technique_name: "Impair Defenses: Impair Command History Logging"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.003/T1562.003.yaml"
build_date: "2026-04-26 17:02:13"
executor: "bash"
aliases:
  - "b3dacb6c-a9e3-44ec-bf87-38db60c5cad1"
  - "Setting the HISTFILE environment variable"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Setting the HISTFILE environment variable

An Adversary may clear, unset or redirect the history environment variable HISTFILE to prevent logging of commands to the history file after they log out of the system.

Note: we don't wish to log out, so we are just confirming the value of HISTFILE. In this test we 1. echo HISTFILE 2. set it to /dev/null 3. confirm that HISTFILE is set to /dev/null.

## Metadata

- Atomic GUID: b3dacb6c-a9e3-44ec-bf87-38db60c5cad1
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
TEST=$(echo $HISTFILE)
echo $HISTFILE
export HISTFILE="/dev/null"
echo "runnning some commands to populate the history"
whoami
groups
if [ $(echo $HISTFILE) == "/dev/null" ]; then echo "\$HISTFILE is /dev/null"; else HIST_LENGHT=$(wc -l $HISTFILE); echo "\$HISTFILE is not /dev/null, history lenght is $HIST_LENGHT";  fi
```

### Cleanup

```bash
export HISTFILE=$(echo $TEST)
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.003/T1562.003.yaml)
