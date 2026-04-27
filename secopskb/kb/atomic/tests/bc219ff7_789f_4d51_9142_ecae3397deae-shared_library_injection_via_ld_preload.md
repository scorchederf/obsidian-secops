---
atomic_guid: "bc219ff7-789f-4d51-9142-ecae3397deae"
title: "Shared Library Injection via LD_PRELOAD"
framework: "atomic"
generated: "true"
attack_technique_id: "T1574.006"
attack_technique_name: "Hijack Execution Flow: LD_PRELOAD"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1574.006/T1574.006.yaml"
build_date: "2026-04-26 17:02:13"
executor: "bash"
aliases:
  - "bc219ff7-789f-4d51-9142-ecae3397deae"
  - "Shared Library Injection via LD_PRELOAD"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Shared Library Injection via LD_PRELOAD

This test injects a shared object library via the LD_PRELOAD environment variable to execute. This technique was used by threat actor Rocke during the exploitation of Linux web servers. This requires the `glibc` package.

Upon successful execution, bash will utilize LD_PRELOAD to load the shared object library `/etc/ld.so.preload`. Output will be via stdout.

## Metadata

- Atomic GUID: bc219ff7-789f-4d51-9142-ecae3397deae
- Technique: T1574.006: Hijack Execution Flow: LD_PRELOAD
- Platforms: linux
- Executor: bash
- Dependency Executor: bash
- Source Path: atomics/T1574.006/T1574.006.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.006]]

## Input Arguments

### path_to_shared_library

- description: Path to a shared library object
- type: path
- default: /tmp/T1574006.so

### path_to_shared_library_source

- description: Path to a shared library source code
- type: path
- default: PathToAtomicsFolder/T1574.006/src/Linux/T1574.006.c

## Dependencies

The shared library must exist on disk at specified location (#{path_to_shared_library})

### Prerequisite Check

```bash
if [ -f #{path_to_shared_library} ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```bash
gcc -shared -fPIC -o #{path_to_shared_library} #{path_to_shared_library_source}
```

## Executor

- name: bash

### Command

```bash
LD_PRELOAD=#{path_to_shared_library} ls
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1574.006/T1574.006.yaml)
