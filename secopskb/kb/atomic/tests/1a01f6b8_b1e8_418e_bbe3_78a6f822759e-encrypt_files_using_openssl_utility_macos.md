---
atomic_guid: "1a01f6b8-b1e8-418e-bbe3-78a6f822759e"
title: "Encrypt files using openssl utility - macOS"
framework: "atomic"
generated: "true"
attack_technique_id: "T1486"
attack_technique_name: "Data Encrypted for Impact"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1486/T1486.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "1a01f6b8-b1e8-418e-bbe3-78a6f822759e"
  - "Encrypt files using openssl utility - macOS"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Encrypt files using openssl utility - macOS

This test encrypts the file(s) using the openssl utility

## Metadata

- Atomic GUID: 1a01f6b8-b1e8-418e-bbe3-78a6f822759e
- Technique: T1486: Data Encrypted for Impact
- Platforms: macos
- Executor: sh
- Elevation Required: False
- Source Path: atomics/T1486/T1486.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1486-data_encrypted_for_impact|T1486]]

## Input Arguments

### encryption_option

- description: Specifiy the required encryption option
- type: string
- default: -pbkdf2

### input_file_path

- description: Path to the file that you want to encrypt
- type: path
- default: ~/test.txt

### output_file_name

- description: Path to the file that you want to encrypt
- type: string
- default: ARTFile

## Executor

- elevation_required: False
- name: sh

### Command

```bash
openssl enc #{encryption_option} -in #{input_file_path} -out #{output_file_name}
```

### Cleanup

```bash
rm #{output_file_name}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1486/T1486.yaml)
