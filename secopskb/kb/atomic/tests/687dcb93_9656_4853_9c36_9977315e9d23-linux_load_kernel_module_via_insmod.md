---
atomic_guid: "687dcb93-9656-4853-9c36-9977315e9d23"
title: "Linux - Load Kernel Module via insmod"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.006"
attack_technique_name: "Boot or Logon Autostart Execution: Kernel Modules and Extensions"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.006/T1547.006.yaml"
build_date: "2026-04-27 19:12:27"
executor: "bash"
aliases:
  - "687dcb93-9656-4853-9c36-9977315e9d23"
  - "Linux - Load Kernel Module via insmod"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test uses the insmod command to load a kernel module for Linux.

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution#^t1547006-kernel-modules-and-extensions|T1547.006: Kernel Modules and Extensions]]

## Input Arguments

### module_name

- description: Name of the kernel module name.
- type: string
- default: T1547006

### module_path

- description: Folder used to store the module.
- type: path
- default: /tmp/T1547.006/T1547006.ko

### module_source_path

- description: Path to download Gsecdump binary file
- type: path
- default: PathToAtomicsFolder/T1547.006/src

### temp_folder

- description: Temp folder used to compile the code.
- type: path
- default: /tmp/T1547.006

## Dependencies

The kernel module must exist on disk at specified location

### Prerequisite Check

```bash
if [ -f #{module_path} ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```bash
if [ ! -d #{temp_folder} ]; then mkdir #{temp_folder}; touch #{temp_folder}/safe_to_delete; fi;
cp #{module_source_path}/* #{temp_folder}/
cd #{temp_folder}; make
if [ ! -f #{module_path} ]; then mv #{temp_folder}/#{module_name}.ko #{module_path}; fi;
```

## Executor

- elevation_required: True
- name: bash

### Command

```bash
sudo insmod #{module_path}
```

### Cleanup

```bash
sudo rmmod #{module_name}
[ -f #{temp_folder}/safe_to_delete ] && rm -rf #{temp_folder}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.006/T1547.006.yaml)
