---
atomic_guid: "e0742e38-6efe-4dd4-ba5c-2078095b6156"
title: "emacs spawning an interactive system shell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.004"
attack_technique_name: "Command and Scripting Interpreter: Bash"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.004/T1059.004.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "e0742e38-6efe-4dd4-ba5c-2078095b6156"
  - "emacs spawning an interactive system shell"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# emacs spawning an interactive system shell

emacs can be used to break out from restricted environments by spawning an interactive system shell. Ref: https://gtfobins.github.io/gtfobins/emacs/

## Metadata

- Atomic GUID: e0742e38-6efe-4dd4-ba5c-2078095b6156
- Technique: T1059.004: Command and Scripting Interpreter: Bash
- Platforms: linux, macos
- Executor: sh
- Elevation Required: True
- Dependency Executor: bash
- Source Path: atomics/T1059.004/T1059.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.004]]

## Dependencies

Check if emacs is installed on the machine.

### Prerequisite Check

```bash
if [ -x "$(command -v emacs)" ]; then echo "emacs is installed"; else echo "emacs is NOT installed"; exit 1; fi
```

### Get Prerequisite

```bash
which apt && apt update && apt install -y emacs || which pkg && pkg update && pkg install -y emacs || which brew && brew update && brew install --quiet emacs
```

## Executor

- elevation_required: True
- name: sh

### Command

```bash
sudo emacs -Q -nw --eval '(term "/bin/sh &")'
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.004/T1059.004.yaml)
