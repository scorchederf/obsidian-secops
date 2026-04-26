---
atomic_guid: "13c5e1ae-605b-46c4-a79f-db28c77ff24e"
title: "Nix File and Directory Discovery 2"
framework: "atomic"
generated: "true"
attack_technique_id: "T1083"
attack_technique_name: "File and Directory Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1083/T1083.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "13c5e1ae-605b-46c4-a79f-db28c77ff24e"
  - "Nix File and Directory Discovery 2"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Nix File and Directory Discovery 2

Find or discover files on the file system

## Metadata

- Atomic GUID: 13c5e1ae-605b-46c4-a79f-db28c77ff24e
- Technique: T1083: File and Directory Discovery
- Platforms: linux, macos
- Executor: sh
- Source Path: atomics/T1083/T1083.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1083-file_and_directory_discovery|T1083]]

## Input Arguments

### output_file

- description: Output file used to store the results.
- type: path
- default: /tmp/T1083.txt

## Executor

- name: sh

### Command

```bash
cd $HOME && find . -print | sed -e 's;[^/]*/;|__;g;s;__|; |;g' > #{output_file}
if [ -f /etc/mtab ]; then cat /etc/mtab >> #{output_file}; fi;
find . -type f -iname *.pdf >> #{output_file}
cat #{output_file}
find . -type f -name ".*"
```

### Cleanup

```bash
rm #{output_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1083/T1083.yaml)
