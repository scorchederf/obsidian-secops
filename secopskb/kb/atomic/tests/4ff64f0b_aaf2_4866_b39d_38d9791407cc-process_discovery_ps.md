---
atomic_guid: "4ff64f0b-aaf2-4866-b39d-38d9791407cc"
title: "Process Discovery - ps"
framework: "atomic"
generated: "true"
attack_technique_id: "T1057"
attack_technique_name: "Process Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1057/T1057.yaml"
build_date: "2026-04-26 14:38:39"
executor: "sh"
aliases:
  - "4ff64f0b-aaf2-4866-b39d-38d9791407cc"
  - "Process Discovery - ps"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Process Discovery - ps

Utilize ps to identify processes.

Upon successful execution, sh will execute ps and output to /tmp/loot.txt.

## Metadata

- Atomic GUID: 4ff64f0b-aaf2-4866-b39d-38d9791407cc
- Technique: T1057: Process Discovery
- Platforms: linux, macos
- Executor: sh
- Source Path: atomics/T1057/T1057.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1057-process_discovery|T1057]]

## Input Arguments

### output_file

- description: path of output file
- type: path
- default: /tmp/loot.txt

## Executor

- name: sh

### Command

```sh
ps >> #{output_file}
ps aux >> #{output_file}
```

### Cleanup

```sh
rm #{output_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1057/T1057.yaml)
