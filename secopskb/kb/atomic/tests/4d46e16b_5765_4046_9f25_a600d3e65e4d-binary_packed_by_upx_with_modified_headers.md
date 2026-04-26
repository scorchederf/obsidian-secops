---
atomic_guid: "4d46e16b-5765-4046-9f25-a600d3e65e4d"
title: "Binary packed by UPX, with modified headers"
framework: "atomic"
generated: "true"
attack_technique_id: "T1027.002"
attack_technique_name: "Obfuscated Files or Information: Software Packing"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027.002/T1027.002.yaml"
build_date: "2026-04-26 14:38:39"
executor: "sh"
aliases:
  - "4d46e16b-5765-4046-9f25-a600d3e65e4d"
  - "Binary packed by UPX, with modified headers"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Binary packed by UPX, with modified headers

Copies and then runs a simple binary (just outputting "the cake is a lie"), that was packed by UPX.

The UPX magic number (`0x55505821`, "`UPX!`") was changed to (`0x4c4f5452`, "`LOTR`"). This prevents the binary from being detected
by some methods, and especially UPX is not able to uncompress it any more.

## Metadata

- Atomic GUID: 4d46e16b-5765-4046-9f25-a600d3e65e4d
- Technique: T1027.002: Obfuscated Files or Information: Software Packing
- Platforms: macos
- Executor: sh
- Source Path: atomics/T1027.002/T1027.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027.002]]

## Input Arguments

### bin_path

- description: Packed binary
- type: path
- default: PathToAtomicsFolder/T1027.002/bin/darwin/test_upx_header_changed

## Executor

- name: sh

### Command

```sh
cp #{bin_path} /tmp/packed_bin && /tmp/packed_bin
```

### Cleanup

```sh
rm /tmp/packed_bin
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027.002/T1027.002.yaml)
