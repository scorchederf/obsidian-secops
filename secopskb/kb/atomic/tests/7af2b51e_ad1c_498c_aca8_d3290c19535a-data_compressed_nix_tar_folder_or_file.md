---
atomic_guid: "7af2b51e-ad1c-498c-aca8-d3290c19535a"
title: "Data Compressed - nix - tar Folder or File"
framework: "atomic"
generated: "true"
attack_technique_id: "T1560.001"
attack_technique_name: "Archive Collected Data: Archive via Utility"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1560.001/T1560.001.yaml"
build_date: "2026-04-27 19:12:28"
executor: "sh"
aliases:
  - "7af2b51e-ad1c-498c-aca8-d3290c19535a"
  - "Data Compressed - nix - tar Folder or File"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

An adversary may compress data (e.g., sensitive documents) that is collected prior to exfiltration. This test uses standard gzip compression.

## ATT&CK Mapping

- [[kb/attack/techniques/T1560-archive_collected_data#^t1560001-archive-via-utility|T1560.001: Archive via Utility]]

## Input Arguments

### input_file_folder

- description: Path that should be compressed
- type: path
- default: $HOME/$USERNAME

### output_file

- description: File that should be output
- type: path
- default: $HOME/data.tar.gz

## Dependencies

Folder to zip must exist (#{input_file_folder})

### Prerequisite Check

```untitled
test -e #{input_file_folder}
```

### Get Prerequisite

```untitled
mkdir -p #{input_file_folder} && touch #{input_file_folder}/file1
```

## Executor

- elevation_required: False
- name: sh

### Command

```bash
tar -cvzf #{output_file} #{input_file_folder}
```

### Cleanup

```bash
rm -f #{output_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1560.001/T1560.001.yaml)
