---
atomic_guid: "c75612b2-9de0-4d7c-879c-10d7b077072d"
title: "Compressing data using bz2 in Python (FreeBSD/Linux)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1560.002"
attack_technique_name: "Archive Collected Data: Archive via Library"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1560.002/T1560.002.yaml"
build_date: "2026-04-27 19:12:28"
executor: "sh"
aliases:
  - "c75612b2-9de0-4d7c-879c-10d7b077072d"
  - "Compressing data using bz2 in Python (FreeBSD/Linux)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Uses bz2 from Python to compress files

## ATT&CK Mapping

- [[kb/attack/techniques/T1560-archive_collected_data#^t1560002-archive-via-library|T1560.002: Archive via Library]]

## Input Arguments

### path_to_input_file

- description: Path to the file that you want to compress
- type: path
- default: /etc/passwd

### path_to_output_file

- description: Path of the file that you want your .bz2 file to be
- type: path
- default: /tmp/passwd.bz2

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
$which_python -c "import bz2;input_file=open('#{path_to_input_file}','rb');content=input_file.read();input_file.close();bz2content=bz2.compress(content,compresslevel=9);output_file=open('#{path_to_output_file}','w+');output_file.write(str(bz2content));output_file.close();"
```

### Cleanup

```bash
rm #{path_to_output_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1560.002/T1560.002.yaml)
