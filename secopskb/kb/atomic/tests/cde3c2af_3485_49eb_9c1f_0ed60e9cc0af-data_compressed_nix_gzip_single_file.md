---
atomic_guid: "cde3c2af-3485-49eb-9c1f-0ed60e9cc0af"
title: "Data Compressed - nix - gzip Single File"
framework: "atomic"
generated: "true"
attack_technique_id: "T1560.001"
attack_technique_name: "Archive Collected Data: Archive via Utility"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1560.001/T1560.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "cde3c2af-3485-49eb-9c1f-0ed60e9cc0af"
  - "Data Compressed - nix - gzip Single File"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Data Compressed - nix - gzip Single File

An adversary may compress data (e.g., sensitive documents) that is collected prior to exfiltration. This test uses standard gzip compression.

## Metadata

- Atomic GUID: cde3c2af-3485-49eb-9c1f-0ed60e9cc0af
- Technique: T1560.001: Archive Collected Data: Archive via Utility
- Platforms: linux, macos
- Executor: sh
- Elevation Required: False
- Source Path: atomics/T1560.001/T1560.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1560-archive_collected_data|T1560.001]]

## Input Arguments

### input_content

- description: contents of compressed files if file does not already exist. default contains test credit card and social security number
- type: string
- default: confidential! SSN: 078-05-1120 - CCN: 4000 1234 5678 9101

### input_file

- description: Path that should be compressed
- type: path
- default: $HOME/victim-gzip.txt

## Executor

- elevation_required: False
- name: sh

### Command

```sh
test -e #{input_file} && gzip -k #{input_file} || (echo '#{input_content}' >> #{input_file}; gzip -k #{input_file})
```

### Cleanup

```sh
rm -f #{input_file}.gz
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1560.001/T1560.001.yaml)
