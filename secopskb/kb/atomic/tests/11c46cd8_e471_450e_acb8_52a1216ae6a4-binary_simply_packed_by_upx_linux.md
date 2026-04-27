---
atomic_guid: "11c46cd8-e471-450e-acb8-52a1216ae6a4"
title: "Binary simply packed by UPX (linux)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1027.002"
attack_technique_name: "Obfuscated Files or Information: Software Packing"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027.002/T1027.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "11c46cd8-e471-450e-acb8-52a1216ae6a4"
  - "Binary simply packed by UPX (linux)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Binary simply packed by UPX (linux)

Copies and then runs a simple binary (just outputting "the cake is a lie"), that was packed by UPX.
No other protection/compression were applied.

## Metadata

- Atomic GUID: 11c46cd8-e471-450e-acb8-52a1216ae6a4
- Technique: T1027.002: Obfuscated Files or Information: Software Packing
- Platforms: linux
- Executor: sh
- Source Path: atomics/T1027.002/T1027.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027.002]]

## Input Arguments

### bin_path

- description: Packed binary
- type: path
- default: PathToAtomicsFolder/T1027.002/bin/linux/test_upx

## Executor

- name: sh

### Command

```bash
cp #{bin_path} /tmp/packed_bin && /tmp/packed_bin
```

### Cleanup

```bash
rm /tmp/packed_bin
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027.002/T1027.002.yaml)
