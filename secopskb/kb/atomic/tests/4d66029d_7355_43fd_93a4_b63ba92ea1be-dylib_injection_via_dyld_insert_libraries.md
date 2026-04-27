---
atomic_guid: "4d66029d-7355-43fd-93a4-b63ba92ea1be"
title: "Dylib Injection via DYLD_INSERT_LIBRARIES"
framework: "atomic"
generated: "true"
attack_technique_id: "T1574.006"
attack_technique_name: "Hijack Execution Flow: LD_PRELOAD"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1574.006/T1574.006.yaml"
build_date: "2026-04-26 17:02:13"
executor: "bash"
aliases:
  - "4d66029d-7355-43fd-93a4-b63ba92ea1be"
  - "Dylib Injection via DYLD_INSERT_LIBRARIES"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Dylib Injection via DYLD_INSERT_LIBRARIES

injects a dylib that opens calculator via env variable

## Metadata

- Atomic GUID: 4d66029d-7355-43fd-93a4-b63ba92ea1be
- Technique: T1574.006: Hijack Execution Flow: LD_PRELOAD
- Platforms: macos
- Executor: bash
- Elevation Required: False
- Dependency Executor: bash
- Source Path: atomics/T1574.006/T1574.006.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.006]]

## Input Arguments

### dylib_file

- description: Path of dylib file
- type: path
- default: /tmp/T1574006MOS.dylib

### file_to_inject

- description: Path of executable to be injected. Mostly works on non-apple default apps.
- type: path
- default: /Applications/Firefox.app/Contents/MacOS/firefox

### source_file

- description: Path of c source file
- type: path
- default: PathToAtomicsFolder/T1574.006/src/MacOS/T1574.006.c

## Dependencies

Compile the dylib from (#{source_file}). Destination is #{dylib_file}

### Prerequisite Check

```bash
gcc -dynamiclib #{source_file} -o #{dylib_file}
```

### Get Prerequisite

```bash
gcc -dynamiclib #{source_file} -o #{dylib_file}
```

## Executor

- elevation_required: False
- name: bash

### Command

```bash
DYLD_INSERT_LIBRARIES=#{dylib_file} #{file_to_inject}
```

### Cleanup

```bash
kill `pgrep Calculator`
kill `pgrep firefox`
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1574.006/T1574.006.yaml)
