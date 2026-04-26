---
atomic_guid: "e86f1b4b-fcc1-4a2a-ae10-b49da01458db"
title: "Compressing data using tarfile in Python (FreeBSD/Linux)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1560.002"
attack_technique_name: "Archive Collected Data: Archive via Library"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1560.002/T1560.002.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "e86f1b4b-fcc1-4a2a-ae10-b49da01458db"
  - "Compressing data using tarfile in Python (FreeBSD/Linux)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Compressing data using tarfile in Python (FreeBSD/Linux)

Uses tarfile from Python to compress files

## Metadata

- Atomic GUID: e86f1b4b-fcc1-4a2a-ae10-b49da01458db
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

- description: Path of the file that you want your .tar.gz file to be
- type: path
- default: /tmp/passwd.tar.gz

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
$which_python -c "import tarfile; output_file = tarfile.open('#{path_to_output_file}','w'); output_file.add('#{path_to_input_file}'); output_file.close()"
```

### Cleanup

```bash
rm #{path_to_output_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1560.002/T1560.002.yaml)
