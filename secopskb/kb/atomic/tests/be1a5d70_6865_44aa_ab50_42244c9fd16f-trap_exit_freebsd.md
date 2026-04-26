---
atomic_guid: "be1a5d70-6865-44aa-ab50-42244c9fd16f"
title: "Trap EXIT (freebsd)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.005"
attack_technique_name: "Event Triggered Execution: Trap"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.005/T1546.005.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "be1a5d70-6865-44aa-ab50-42244c9fd16f"
  - "Trap EXIT (freebsd)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Trap EXIT (freebsd)

Launch bash shell with command arg to create TRAP on EXIT.
The trap executes script that writes to /tmp/art-fish.txt

## Metadata

- Atomic GUID: be1a5d70-6865-44aa-ab50-42244c9fd16f
- Technique: T1546.005: Event Triggered Execution: Trap
- Platforms: linux
- Executor: sh
- Dependency Executor: sh
- Source Path: atomics/T1546.005/T1546.005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.005]]

## Dependencies

Check if bash is installed.

### Prerequisite Check

```bash
if [ ! -x "$(command -v bash)" ]; then exit 1; else exit 0; fi;
```

### Get Prerequisite

```bash
(which pkg && pkg install -y bash)
```

## Executor

- name: sh

### Command

```bash
bash -c 'trap "nohup sh $PathToAtomicsFolder/T1546.005/src/echo-art-fish.sh" EXIT'
```

### Cleanup

```bash
rm -f /tmp/art-fish.txt
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.005/T1546.005.yaml)
