---
atomic_guid: "001a042b-859f-44d9-bf81-fd1c4e2200b0"
title: "Compressing data using zipfile in Python (FreeBSD/Linux)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1560.002"
attack_technique_name: "Archive Collected Data: Archive via Library"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1560.002/T1560.002.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "001a042b-859f-44d9-bf81-fd1c4e2200b0"
  - "Compressing data using zipfile in Python (FreeBSD/Linux)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Compressing data using zipfile in Python (FreeBSD/Linux)

Uses zipfile from Python to compress files

## Metadata

- Atomic GUID: 001a042b-859f-44d9-bf81-fd1c4e2200b0
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

- description: Path of the file that you want your .zip file to be
- type: path
- default: /tmp/passwd.zip

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
$which_python -c "from zipfile import ZipFile; ZipFile('#{path_to_output_file}', mode='w').write('#{path_to_input_file}')"
```

### Cleanup

```bash
rm #{path_to_output_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1560.002/T1560.002.yaml)
