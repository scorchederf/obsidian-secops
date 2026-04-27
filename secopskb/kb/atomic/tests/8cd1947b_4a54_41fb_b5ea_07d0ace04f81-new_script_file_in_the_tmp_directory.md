---
atomic_guid: "8cd1947b-4a54-41fb-b5ea-07d0ace04f81"
title: "New script file in the tmp directory"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.004"
attack_technique_name: "Command and Scripting Interpreter: Bash"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.004/T1059.004.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "8cd1947b-4a54-41fb-b5ea-07d0ace04f81"
  - "New script file in the tmp directory"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# New script file in the tmp directory

An attacker may create script files in the /tmp directory using the mktemp utility and execute them. The following commands creates a temp file and places a pointer to it in the variable $TMPFILE, echos the string id into it, and then executes the file using bash, which results in the id command being executed.

## Metadata

- Atomic GUID: 8cd1947b-4a54-41fb-b5ea-07d0ace04f81
- Technique: T1059.004: Command and Scripting Interpreter: Bash
- Platforms: linux
- Executor: sh
- Elevation Required: False
- Source Path: atomics/T1059.004/T1059.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.004]]

## Executor

- elevation_required: False
- name: sh

### Command

```bash
TMPFILE=$(mktemp)
echo "id" > $TMPFILE
bash $TMPFILE
```

### Cleanup

```bash
rm $TMPFILE
unset TMPFILE
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.004/T1059.004.yaml)
