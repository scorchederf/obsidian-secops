---
atomic_guid: "c51cec55-28dd-4ad2-9461-1eacbc82c3a0"
title: "Data Compressed - nix - zip"
framework: "atomic"
generated: "true"
attack_technique_id: "T1560.001"
attack_technique_name: "Archive Collected Data: Archive via Utility"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1560.001/T1560.001.yaml"
build_date: "2026-04-27 19:12:28"
executor: "bash"
aliases:
  - "c51cec55-28dd-4ad2-9461-1eacbc82c3a0"
  - "Data Compressed - nix - zip"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

An adversary may compress data (e.g., sensitive documents) that is collected prior to exfiltration. This test uses standard zip compression.

## ATT&CK Mapping

- [[kb/attack/techniques/T1560-archive_collected_data#^t1560001-archive-via-utility|T1560.001: Archive via Utility]]

## Input Arguments

### input_files

- description: Path that should be compressed into our output file, may include wildcards
- type: path
- default: /var/log/{w,b}tmp

### output_file

- description: Path that should be output as a zip archive
- type: path
- default: $HOME/data.zip

## Dependencies

Files to zip must exist (#{input_files})

### Prerequisite Check

```untitled
if [ $(ls #{input_files} | wc -l) > 0 ] && [ -x $(which zip) ] ; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```untitled
(which yum && yum -y install epel-release zip)||(which apt-get && apt-get install -y zip)
echo Please set input_files argument to include files that exist
```

## Executor

- elevation_required: True
- name: bash

### Command

```bash
zip #{output_file} #{input_files}
```

### Cleanup

```bash
rm -f #{output_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1560.001/T1560.001.yaml)
