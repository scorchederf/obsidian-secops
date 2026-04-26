---
atomic_guid: "f4391089-d3a5-4dd1-ab22-0419527f2672"
title: "MacOS - Load Kernel Module via kextload and kmutil"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.006"
attack_technique_name: "Boot or Logon Autostart Execution: Kernel Modules and Extensions"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.006/T1547.006.yaml"
build_date: "2026-04-26 17:02:13"
executor: "bash"
aliases:
  - "f4391089-d3a5-4dd1-ab22-0419527f2672"
  - "MacOS - Load Kernel Module via kextload and kmutil"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# MacOS - Load Kernel Module via kextload and kmutil

This test uses the kextload and kmutil commands to load and unload a MacOS kernel module.

## Metadata

- Atomic GUID: f4391089-d3a5-4dd1-ab22-0419527f2672
- Technique: T1547.006: Boot or Logon Autostart Execution: Kernel Modules and Extensions
- Platforms: macos
- Executor: bash
- Elevation Required: True
- Dependency Executor: bash
- Source Path: atomics/T1547.006/T1547.006.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.006]]

## Input Arguments

### module_path

- description: Folder used to store the module.
- type: path
- default: /Library/Extensions/SoftRAID.kext

## Dependencies

The kernel module must exist on disk at specified location

### Prerequisite Check

```bash
if [ -d #{module_path} ] ; then exit 0; else exit 1 ; fi
```

### Get Prerequisite

```bash
exit 1
```

## Executor

- elevation_required: True
- name: bash

### Command

```bash
set -x
sudo kextload #{module_path}
kextstat 2>/dev/null | grep SoftRAID
sudo kextunload #{module_path}
sudo kmutil load -p #{module_path}
kextstat 2>/dev/null | grep SoftRAID
sudo kmutil unload -p #{module_path}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.006/T1547.006.yaml)
