---
atomic_guid: "75483ef8-f10f-444a-bf02-62eb0e48db6f"
title: "Loadable Kernel Module based Rootkit"
framework: "atomic"
generated: "true"
attack_technique_id: "T1014"
attack_technique_name: "Rootkit"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1014/T1014.yaml"
build_date: "2026-04-27 19:12:25"
executor: "sh"
aliases:
  - "75483ef8-f10f-444a-bf02-62eb0e48db6f"
  - "Loadable Kernel Module based Rootkit"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Loadable Kernel Module based Rootkit

## ATT&CK Mapping

- [[kb/attack/techniques/T1014-rootkit|T1014: Rootkit]]

## Input Arguments

### rootkit_name

- description: Module name
- type: string
- default: T1014

### rootkit_source_path

- description: Path to the rootkit source. Used when prerequisites are fetched.
- type: path
- default: PathToAtomicsFolder/T1014/src/Linux

## Dependencies

The kernel module must exist on disk at specified location (#{rootkit_source_path}/#{rootkit_name}.ko)

### Prerequisite Check

```bash
if [ -f /lib/modules/$(uname -r)/#{rootkit_name}.ko ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```bash
sudo apt install make
sudo apt install gcc
if [ ! -d /tmp/T1014 ]; then mkdir /tmp/T1014; touch /tmp/T1014/safe_to_delete; fi;
cp #{rootkit_source_path}/* /tmp/T1014
cd /tmp/T1014; make        
sudo cp /tmp/T1014/#{rootkit_name}.ko /lib/modules/$(uname -r)/
[ -f /tmp/T1014/safe_to_delete ] && rm -rf /tmp/T1014
sudo depmod -a
```

## Executor

- elevation_required: True
- name: sh

### Command

```bash
sudo modprobe #{rootkit_name}
```

### Cleanup

```bash
sudo modprobe -r #{rootkit_name}
sudo rm /lib/modules/$(uname -r)/#{rootkit_name}.ko
sudo depmod -a
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1014/T1014.yaml)
