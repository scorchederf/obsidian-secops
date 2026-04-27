---
atomic_guid: "f7308845-6da8-468e-99f2-4271f2f5bb67"
title: "Setting the HISTFILE environment variable (freebsd)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.003"
attack_technique_name: "Impair Defenses: Impair Command History Logging"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.003/T1562.003.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "f7308845-6da8-468e-99f2-4271f2f5bb67"
  - "Setting the HISTFILE environment variable (freebsd)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Setting the HISTFILE environment variable (freebsd)

An Adversary may clear, unset or redirect the history environment variable HISTFILE to prevent logging of commands to the history file after they log out of the system.

Note: we don't wish to log out, so we are just confirming the value of HISTFILE. In this test we 1. echo HISTFILE 2. set it to /dev/null 3. confirm that HISTFILE is set to /dev/null.

## Metadata

- Atomic GUID: f7308845-6da8-468e-99f2-4271f2f5bb67
- Technique: T1562.003: Impair Defenses: Impair Command History Logging
- Platforms: linux
- Executor: sh
- Elevation Required: False
- Source Path: atomics/T1562.003/T1562.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.003]]

## Executor

- elevation_required: False
- name: sh

### Command

```bash
echo $HISTFILE
export HISTFILE="/dev/null"
if [ $(echo $HISTFILE) == "/dev/null" ]; then echo "\$HISTFILE is /dev/null"; fi
```

### Cleanup

```bash
export HISTFILE=~/.sh_history
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.003/T1562.003.yaml)
