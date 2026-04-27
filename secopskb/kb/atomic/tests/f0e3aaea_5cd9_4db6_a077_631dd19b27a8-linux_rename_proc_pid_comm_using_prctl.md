---
atomic_guid: "f0e3aaea-5cd9-4db6-a077-631dd19b27a8"
title: "linux rename /proc/pid/comm using prctl"
framework: "atomic"
generated: "true"
attack_technique_id: "T1036.004"
attack_technique_name: "Masquerading: Masquerade Task or Service"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036.004/T1036.004.yaml"
build_date: "2026-04-27 19:12:25"
executor: "sh"
aliases:
  - "f0e3aaea-5cd9-4db6-a077-631dd19b27a8"
  - "linux rename /proc/pid/comm using prctl"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Runs a C program that calls prctl(PR_SET_NAME) to modify /proc/pid/comm value to "totally_legit".  This will show up as process name in simple 'ps' listings.

## ATT&CK Mapping

- [[kb/attack/techniques/T1036-masquerading#^t1036004-masquerade-task-or-service|T1036.004: Masquerade Task or Service]]

## Input Arguments

### exe_path

- description: Output Binary Path
- type: path
- default: /tmp/T1036_004_prctl_rename

## Dependencies

#{exe_path} must be exist on system.

### Prerequisite Check

```bash
stat #{exe_path}
```

### Get Prerequisite

```bash
cc -o #{exe_path} PathToAtomicsFolder/T1036.004/src/prctl_rename.c
```

## Executor

- name: sh

### Command

```bash
#{exe_path} & ps
TMP=`ps | grep totally_legit`
if [ -z "${TMP}" ] ; then echo "renamed process NOT FOUND in process list" && exit 1; fi
exit 0
```

### Cleanup

```bash
rm -f #{exe_path}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036.004/T1036.004.yaml)
