---
atomic_guid: "878794f7-c511-4199-a950-8c28b3ed8e5b"
title: "Clear bash history"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.003"
attack_technique_name: "Impair Defenses: Impair Command History Logging"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.003/T1562.003.yaml"
build_date: "2026-04-26 14:38:40"
executor: "bash"
aliases:
  - "878794f7-c511-4199-a950-8c28b3ed8e5b"
  - "Clear bash history"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Clear bash history

An attacker may clear the bash history cache and the history file as their last act before logging off to remove the record of their command line activities. 

In this test we use the $HISTFILE variable throughout to 1. confirms the $HISTFILE variable is set 2. echo "" into it 3..5 confirm the file is empty 6 clear the history cache 7. confirm the history cache is empty. This is when the attacker would logoff.

## Metadata

- Atomic GUID: 878794f7-c511-4199-a950-8c28b3ed8e5b
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
cp $HISTFILE $HISTFILE.OLD
if ((${#HISTFILE[@]})); then echo $HISTFILE; fi
echo "" > $HISTFILE
if [ $(wc -c <$HISTFILE) -gt 1 ]; then echo "$HISTFILE is larger than 1k"; fi
ls -la $HISTFILE 
cat $HISTFILE
history -c 
if [ $(history |wc -l) -eq 1 ]; then echo "History cache cleared"; fi
```

### Cleanup

```bash
mv -f $HISTFILE.OLD $HISTFILE
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.003/T1562.003.yaml)
