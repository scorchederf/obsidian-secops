---
atomic_guid: "f0007753-beb3-41ea-9948-760785e4c1e5"
title: "MacOS - Load Kernel Module via KextManagerLoadKextWithURL()"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.006"
attack_technique_name: "Boot or Logon Autostart Execution: Kernel Modules and Extensions"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.006/T1547.006.yaml"
build_date: "2026-04-26 17:02:13"
executor: "bash"
aliases:
  - "f0007753-beb3-41ea-9948-760785e4c1e5"
  - "MacOS - Load Kernel Module via KextManagerLoadKextWithURL()"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# MacOS - Load Kernel Module via KextManagerLoadKextWithURL()

This test uses the IOKit API to load a kernel module for macOS.
Harcoded to use SoftRAID kext

## Metadata

- Atomic GUID: f0007753-beb3-41ea-9948-760785e4c1e5
- Technique: T1547.006: Boot or Logon Autostart Execution: Kernel Modules and Extensions
- Platforms: macos
- Executor: bash
- Elevation Required: True
- Dependency Executor: bash
- Source Path: atomics/T1547.006/T1547.006.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.006]]

## Input Arguments

### exe_path

- description: Folder used to store the module.
- type: path
- default: /tmp/T1547006_iokit_loader

### src_path

- description: Folder used to store the module.
- type: path
- default: PathToAtomicsFolder/T1547.006/src/macos_kextload.c

## Dependencies

The kernel module must exist on disk at specified location

### Prerequisite Check

```bash
if [ -f "#{exe_path}" ]; then exit 0 ; else exit 1; fi
```

### Get Prerequisite

```bash
cc -o #{exe_path} #{src_path} -framework IOKit -framework Foundation
```

## Executor

- elevation_required: True
- name: bash

### Command

```bash
sudo #{exe_path}
kextstat 2>/dev/null | grep SoftRAID
sudo kextunload /Library/Extensions/SoftRAID.kext
```

### Cleanup

```bash
rm -f #{exe_path}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.006/T1547.006.yaml)
