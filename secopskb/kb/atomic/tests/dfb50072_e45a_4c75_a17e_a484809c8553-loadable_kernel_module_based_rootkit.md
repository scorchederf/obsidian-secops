---
atomic_guid: "dfb50072-e45a-4c75-a17e-a484809c8553"
title: "Loadable Kernel Module based Rootkit"
framework: "atomic"
generated: "true"
attack_technique_id: "T1014"
attack_technique_name: "Rootkit"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1014/T1014.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "dfb50072-e45a-4c75-a17e-a484809c8553"
  - "Loadable Kernel Module based Rootkit"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Loadable Kernel Module based Rootkit

Loadable Kernel Module based Rootkit

## Metadata

- Atomic GUID: dfb50072-e45a-4c75-a17e-a484809c8553
- Technique: T1014: Rootkit
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Dependency Executor: bash
- Source Path: atomics/T1014/T1014.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1014-rootkit|T1014]]

## Input Arguments

### rootkit_name

- description: Module name
- type: string
- default: T1014

### rootkit_path

- description: Path To rootkit
- type: string
- default: PathToAtomicsFolder/T1014/bin

### rootkit_source_path

- description: Path to the rootkit source. Used when prerequisites are fetched.
- type: path
- default: PathToAtomicsFolder/T1014/src/Linux

## Dependencies

The kernel module must exist on disk at specified location (#{rootkit_path}/#{rootkit_name}.ko)

### Prerequisite Check

```bash
if [ -f #{rootkit_path}/#{rootkit_name}.ko ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```bash
sudo apt install make
sudo apt install gcc
if [ ! -d /tmp/T1014 ]; then mkdir /tmp/T1014; fi;
cp #{rootkit_source_path}/* /tmp/T1014/
cd /tmp/T1014; make
mkdir #{rootkit_path}
mv /tmp/T1014/#{rootkit_name}.ko #{rootkit_path}/#{rootkit_name}.ko
rm -rf /tmp/T1014
```

## Executor

- elevation_required: True
- name: sh

### Command

```bash
sudo insmod #{rootkit_path}/#{rootkit_name}.ko
```

### Cleanup

```bash
sudo rmmod #{rootkit_name}
sudo rm -rf #{rootkit_path}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1014/T1014.yaml)
