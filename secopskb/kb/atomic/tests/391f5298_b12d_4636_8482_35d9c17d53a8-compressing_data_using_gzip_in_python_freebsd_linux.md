---
atomic_guid: "391f5298-b12d-4636-8482-35d9c17d53a8"
title: "Compressing data using GZip in Python (FreeBSD/Linux)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1560.002"
attack_technique_name: "Archive Collected Data: Archive via Library"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1560.002/T1560.002.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "391f5298-b12d-4636-8482-35d9c17d53a8"
  - "Compressing data using GZip in Python (FreeBSD/Linux)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Compressing data using GZip in Python (FreeBSD/Linux)

Uses GZip from Python to compress files

## Metadata

- Atomic GUID: 391f5298-b12d-4636-8482-35d9c17d53a8
- Technique: T1560.002: Archive Collected Data: Archive via Library
- Platforms: linux
- Executor: sh
- Elevation Required: False
- Dependency Executor: sh
- Source Path: atomics/T1560.002/T1560.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1560-archive_collected_data|T1560.002]]

## Input Arguments

### path_to_input_file

- description: Path to the file that you want to compress
- type: path
- default: /etc/passwd

### path_to_output_file

- description: Path of the file that you want your .gz file to be
- type: path
- default: /tmp/passwd.gz

## Dependencies

Requires Python

### Prerequisite Check

```bash
which python || which python3
```

### Get Prerequisite

```bash
echo "please install python to run this test"; exit 1
```

## Executor

- elevation_required: False
- name: sh

### Command

```bash
which_python=`which python || which python3`
$which_python -c "import gzip;input_file=open('#{path_to_input_file}', 'rb');content=input_file.read();input_file.close();output_file=gzip.GzipFile('#{path_to_output_file}','wb',compresslevel=6);output_file.write(content);output_file.close();"
```

### Cleanup

```bash
rm #{path_to_output_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1560.002/T1560.002.yaml)
